class Student:
    class_ = "student"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def average_score(self):
        self.score_1 = int(input("Enter first test score:"))
        self.score_2 = int(input("Enter second test score:"))
        self.score_3 = int(input("Enter third test score:"))
        average = (self.score_1 + self.score_2 + self.score_3)/3
        return f"{self.name} scored an avergage of {average}"



John = Student("John", "21")
Jane = Student("Jane", "22")

print(John.average_score())
print(Jane.average_score())
