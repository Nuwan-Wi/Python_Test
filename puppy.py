class Dog():
    def __init__(self):
        print('Dog is sleepng.')
    
    def awake(self):
        print('Dog wakes up but unresponsive.')

class Puppy(Dog):
    def __init__(self):
        super().__init__()

    def puppy_bark(self):
        print('Puppy is barking.................')

puppy = Puppy()
puppy.awake()
puppy.puppy_bark()