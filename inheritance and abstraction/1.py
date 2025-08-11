class Person(object):
    def __init__(self, name, idnumber):
        self.name= name
        self.idnumber= idnumber
    
    def display(self):
        print("Name:", self.name)
        print("ID number:", self.idnumber)

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)
        self.salary= salary
        self.post= post

    def details(self):
        print("Salary:", self.salary)
        print("Post:", self.post)

ob = Employee('Mark', '20250958', '20000', 'Junior')
ob.display()
ob.details()