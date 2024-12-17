class i:
    @staticmethod
    def add(num1,num2):
        sum = num1+num2
        print(sum)
y=i()
y.add(7,8)
   
class i:
    @staticmethod
    def add(num1, num2):
        sum_result = num1 + num2
        return sum_result  # Returning the sum instead of printing it directly

y = i()
result = y.add(7, 8)  # Calling the static method
print("The sum is:", result)  # Print the result outside the method

