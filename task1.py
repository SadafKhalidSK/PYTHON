class Student:
    def __init__(self, name, age, grade): 
        self.name= name
        self.age= age
        self.grade= grade

    def display_details(self):
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print(f"Name: {self.name}")


student1 = Student("Alice",14,"9th")
student1.display_details()


# class Student:
#     def __init__(self, name, age, grade): 
#         self.name = name
#         self.age = age
#         self.grade = grade

    # def display_details(self):
    #     print(f"Age: {self.age}")
    #     print(f"Grade: {self.grade}")
    #     print(f"Name: {self.name}")

# Create an object and call the method
# student1 = Student("Alice", 14, "9th")
# student1.display_details()
