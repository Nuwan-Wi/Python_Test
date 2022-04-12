# 4 pillars of OOP

# 1. abstraction
# 2. inheritance
# 3. ecapsulation
# 4. polymorphism

# inheritance
#     is the ability or property of a class to derive properties from a previously defined class.
#     son class can have parent class's properties.

class Mother:
    msg_m = "I'm the mother"
    money = 1250

class Daughter(Mother):
    msg_d = "I'm the daughter"
    # money = 100

obj_daughter = Daughter()

print(obj_daughter.msg_d)
print(obj_daughter.msg_m)
print(obj_daughter.money)