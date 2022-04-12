class Dog:
    def __init__(self):
        print("Dog is sleeping.")
    
    def awake(self):
        print("Dog is awake but unresponsive.")

    def dog_bark(self):
        print("Dog is barking.")


class Puppy(Dog): 
    def __init__(self):
        super().__init__()

    def puppy_bark(self):
        print("Puppy is barking....")



puppy = Puppy()
puppy.awake()
puppy.dog_bark()
puppy.puppy_bark()