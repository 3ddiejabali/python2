class student:
    def __init__(self,firstname,course,gender):
        self.firstname=firstname
        self.course=course
        self.gender=gender

    def study(self):
        print(self.firstname, "is studying")

student1 = student("sam","cybersecurity","male")
student2 = student("Neema","Datascience","Female")
student3 = student("Makena","MIT","Female")

student1.study()
student2.study()
student3.study()