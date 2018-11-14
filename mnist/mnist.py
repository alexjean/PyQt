# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 上午 8:28
# @Author  : AlexJean
import sys
import os
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

INPUT_NODE = 784
OUTPUT_NODE = 10
LAYER1_NODE = 500
BATCH_SIZE = 100

LEARNING_RATE_BASE = 0.8
LEARNING_RATE_DECAY = 0.99
REGULARIZATION_RATE = 0.0001
TRAINING_STEPS = 30000
MOVING_AVERAGE_DECAY = 0.99
MODEL_SAVE_PATH = "./model/"
MODEL_NAME = "model.ckpt"


class Mnist:
    @staticmethod
    def tfVersion():
        return tf.VERSION

    @staticmethod
    def inputData():
        return input_data.read_data_sets("MNIST_data/", one_hot=True)

    @staticmethod
    def getWeights(shape, regularizer):
        weights = tf.get_variable("weights", shape, initializer=tf.truncated_normal_initializer(stddev=0.1))
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(weights))
        return weights

    @staticmethod
    def inference(inputTensor, regularizer):
        with tf.variable_scope('layer1'):
            weights = Mnist.getWeights([INPUT_NODE, LAYER1_NODE], regularizer)
            biases = tf.get_variable("biases", [LAYER1_NODE], initializer=tf.constant_initializer(0.0))
            layer1 = tf.nn.relu(tf.matmul(inputTensor, weights) + biases)

        with tf.variable_scope('layer2'):
            weights = Mnist.getWeights([LAYER1_NODE, OUTPUT_NODE], regularizer)
            biases = tf.get_variable("biases", [OUTPUT_NODE], initializer=tf.constant_initializer(0.0))
            layer2 = tf.matmul(layer1, weights) + biases

        return layer2

    @staticmethod
    def train(mnistData):
        x = tf.placeholder(tf.float32, [None, INPUT_NODE], name='x-input')
        y_ = tf.placeholder(tf.float32, [None, OUTPUT_NODE], name='y-input')
        regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)
        y = Mnist.inference(x, regularizer)
        globalStep = tf.Variable(0, trainable=False)
        expMovingAve = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, globalStep)
        variableAverageOp = expMovingAve.apply(tf.trainable_variables())
        crossEntropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))
        crossEntropyMean = tf.reduce_mean(crossEntropy)
        loss = crossEntropyMean + tf.add_n(tf.get_collection('losses'))
        learningRate = tf.train.exponential_decay(LEARNING_RATE_BASE, globalStep,
                                                  mnistData.train.num_examples, LEARNING_RATE_DECAY)
        trainStep = tf.train.GradientDescentOptimizer(learningRate).minimize(loss, global_step=globalStep)
        with tf.control_dependencies([trainStep, variableAverageOp]):
            trainOp = tf.no_op(name='train')
        saver = tf.train.Saver()
        with tf.Session() as sess:
            tf.global_variables_initializer().run()
            for i in range(TRAINING_STEPS):
                xs, ys = mnistData.train.next_batch(BATCH_SIZE)
                _, lossValue, step = sess.run([trainOp, loss, globalStep], feed_dict={x: xs, y_: ys})
                if i % 1000 == 0:
                    print("After %d training steps , loss on training batch is %g." % (step, lossValue))
                    saver.save(sess, os.path.join(MODEL_SAVE_PATH, MODEL_NAME), global_step=globalStep)
        return

    @staticmethod
    def inference1(inputTensor, avgClass, weights1, biases1, weights2, biases2):
        if avgClass is None:
            layer1 = tf.nn.relu(tf.matmul(inputTensor, weights1) + biases1)
            #  没有加softmax, 因为计算损失函数時...sparse_softmax_cross_entropy_with_logits
            return tf.matmul(layer1, weights2) + biases2
        else:
            layer1 = tf.nn.relu(tf.matmul(inputTensor, avgClass.average(weights1)) + avgClass.average(biases1))
            return tf.matmul(layer1, avgClass.average(weights2)) + avgClass.average(biases2)

    @staticmethod
    def train1(mnistData):
        x = tf.placeholder(tf.float32, [None, INPUT_NODE], name='x-input')
        y_ = tf.placeholder(tf.float32, [None, OUTPUT_NODE], name='y-input')
        weights1 = tf.Variable(tf.truncated_normal([INPUT_NODE, LAYER1_NODE], stddev=0.1))
        biases1 = tf.Variable(tf.constant(0.1, shape=[LAYER1_NODE]))
        weights2 = tf.Variable(tf.truncated_normal([LAYER1_NODE, OUTPUT_NODE], stddev=0.1))
        biases2 = tf.Variable(tf.constant(0.1, shape=[OUTPUT_NODE]))

        y = Mnist.inference1(x, None, weights1, biases1, weights2, biases2)

        globalStep = tf.Variable(0, trainable=False)
        expMovingAve = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, globalStep)
        # 在所有trainable变量上使用移动平均
        variableAverageOp = expMovingAve.apply(tf.trainable_variables())
        averageY = Mnist.inference1(x, expMovingAve, weights1, biases1, weights2, biases2)

        # sm=nn.softmax(y)
        # onehot=tf.sparse_to_dense(tf.argmax(y_,1))
        # nn.sparse_cross_entropy(sm,onehot)
        crossEntropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))

        crossEntropyMean = tf.reduce_mean(crossEntropy)
        regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)
        regularization = regularizer(weights1) + regularizer(weights2)
        loss = crossEntropyMean + regularization

        learningRate = tf.train.exponential_decay(LEARNING_RATE_BASE, globalStep,
                                                  mnistData.train.num_examples / BATCH_SIZE, LEARNING_RATE_DECAY)
        trainStep = tf.train.GradientDescentOptimizer(learningRate).minimize(loss, global_step=globalStep)

        with tf.control_dependencies([trainStep, variableAverageOp]):
            trainOp = tf.no_op(name='train')
        correctPrediction = tf.equal(tf.argmax(averageY, 1), tf.argmax(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correctPrediction, tf.float32))

        with tf.Session() as sess:
            tf.global_variables_initializer().run()
            validateFeed = {x: mnistData.validation.images, y_: mnistData.validation.labels}
            testFeed = {x: mnistData.test.images, y_: mnistData.test.labels}

            for i in range(TRAINING_STEPS):
                if i % 100 == 0:
                    validateAcc = sess.run(accuracy, feed_dict=validateFeed)
                    print("After %d training steps, validation accuracy "
                          "using average model is %g " % (i, validateAcc))

                xs, ys = mnistData.train.next_batch(BATCH_SIZE)
                sess.run(trainOp, feed_dict={x: xs, y_: ys})

            testAcc = sess.run(accuracy, feed_dict=testFeed)
            message = ("After %d training steps, \nAverage accuracy is %g "
                       % (TRAINING_STEPS, testAcc))
            print(message)
            return message
