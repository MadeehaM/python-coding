class student:
    school = "Aun"
    name = "Cara"

    def intro(self):
        print("Hi, I am a student of", self.school)

    def details(self):
        print("My name is", self.name)
    
    def additional(self,year):
       
        print("I am a", year, "student")

ob=student()
ob.intro()
ob.details()
ob.additional("1st year")
