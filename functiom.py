# '''A function is a piece of code that is called by name. 
# It can be passed data to operate on (i.e., the parameters) and can optionally return data 
# (the return value). All data that is passed to a function is explicitly passed'''

# def sum(num1, num2):  # This is a function
#     num3 = num1 + num2
#     print(num3)

# sum(4, 6)  # Function call

# class student:
#     def sum2(self, num4, num5):  # This is a method
#         num6 = num4 + num5
#         print(num6)

# ob = student()  # Object of class 'student'
# ob.sum2(6, 9)  # Method call


'''Magic Methods (also called dunder methods, short for double underscore methods) are special methods in Python that start and end with double underscores (__), such as __init__, __str__, and __add__.'''


# class f:
#     def p(self, name):
#         self.name = name  # Set the attribute 'name'

# t = f()        # Create an instance of the class
# t.p("kanna")   # Call the method to set the 'name' attribute
# print(t.name)  # Print the 'name' attribute

#Attribute defined inside the class
class g:
    def __init__(self, name):  # Corrected __init__ syntax
        self.name = name       # Initialize name attribute

h = g("Abi")  # Pass 'name' argument when creating the object
h.age = "ram"  # Add attribute 'age' dynamically

print(h.name, h.age)  # Access and print the attributes








