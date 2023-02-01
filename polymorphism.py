# Parent class instance
class Human():
    name = ''
    species = ''
    legs = 2
    arms = 2
    origin = "Earth"

    def information(self):
        msg = "\nName: {},\nSpecies: {}\nLegs: {}\nArms: {}\nOrigin: {}".format(self.name,self.species,self.legs,self.arms,self.origin)
        return msg

   

# Child class instance
class Teacher(Human):
    name = 'Tom'
    species = 'Homosapien'
    
  
    
    def teaching(self):
        msg = "\nSpends most of the day teaching their students about the world and how to succeed in it."
        print(msg)
        
# Child class instance
class Student(Human):
    name = 'Fred'
    species = 'Homosapien'
    major = 'Biology'

    
    def study(self):
        msg = "\nWorks day and night on homework to ace final exam!"
        print(msg)


if __name__ == "__main__":
    
     teacher = Teacher()
     
     print(teacher.teaching())
     print(teacher.information())
    
     

     student = Student()
     
     print(student.study())
     print(student.information())
