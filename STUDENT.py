class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def honorRoll(self):
        if self.gpa >= 3.5:
            return ("Yes") 
    
        else:
            return ("No") 
            
         


       

        