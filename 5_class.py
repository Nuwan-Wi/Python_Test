class Add2Num:
    def show (self,a,b) :
        print(f'{a} + {b} = ', a+b)
        print(a, '+' , b, '-', a-b) 

a=int(input ('enter first number : '))
b=int(input('enter first number : '))

obj = Add2Num()
print(obj.show(a,b))
