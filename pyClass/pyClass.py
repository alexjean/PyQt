class MyClass:
    count=0
    name='DefaultName'

    def __init__(self,name):
        self.name=name
        print('class name=%s\nInstance name=%s' % (MyClass.name,self.name))

    def setCount(self,count):
        self.count=count

    def getCount(self):
        return self.count

if __name__ == "__main__":
    cls=MyClass('lisi')
    cls.setCount(10)
    print('count=%d' % cls.getCount())
