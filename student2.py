class Add2Num:
    def show(self ,a,b):
        print(f'{a} + {b} = ',a+b)
        print(a, '+' , b, '=', a+b)

a=int(input("Enter First number : "))
b=int(input("Enter First number : "))

obj= Add2Num()
obj.show(a,b)