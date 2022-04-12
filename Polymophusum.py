# def add (a,b,c=0):
#     return a+b+c

# print('10 + 20 =',add(10,20))
# print('10 + 20 + 30 =',add(10,20,30))
# print('v+i+r = ',add('v','i','r'))

class Hill:
    def height(self):
        hight = 100
        print(f'The height of the hill is {hight}')

    def location(self):
        town = 'Badulla'
        print(f'The hill is located in {town}')

class Tower:
    def height(self):
        hight = 200
        print(f'The height of the tower is {hight}')

    def location(self):
        town = 'Colombo'
        print(f'The tower is located in {town}')

# car1=Hill()
# car2=Tower()
# car1.height()
# car1.location()
# car2.height()
# car2.location()

    
li = [Hill(), Tower()]
for i in li:
    i.height()
    i.location()