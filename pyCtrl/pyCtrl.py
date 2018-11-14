print('\n#2,elif')
x,y,z=10,20,5
if x>y:
    print('x>y')
elif x>z:
    print('x>z')
else:
    print('else')

print('\n#3,while')
while x>0:
    print(x)
    x-=1

print('\n#4,for')
xlst=['1','b','xxx']
for x in xlst:
    print(x)