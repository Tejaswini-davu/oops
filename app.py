class student:
    """
    In Python, a constructor is a special method that is called automatically when an object is created from a class.
    Its main role is to initialize the object by setting up its attributes or state.
    The method __new__ is the constructor that creates a new instance of the class, while __init__ is the initializer that sets up 
    the instance’s attributes after creation. These methods work together to manage object creation and initialization.
    """
    def __init__(self):
        self.id = 19,
        self.name= "soumith",
        self.marks = 89

    def sem(self,marks):
       print(f"i got 25 marks in {marks} exam ")   

school = student()
print(school.id)
school.sem("English")

