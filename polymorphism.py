# Parent class instance
class Human():
    name = ''
    species = ''
    legs = 2
    arms = 2
    origin = "Earth"

    def information(self):
        msg = "\nName: {},\nSpecies: {}\nLegs: {}\nArms: {}".format(self.name,self.species,self.legs,self.arms)
        return msg

   

   

# Child class instance
class Teacher(Human):
    name = 'Tom'
    species = 'Homosapien'
    age = 30
    specialty = 'German'
    
  
    
    def information(self):
        msg = "{}, age {}, spends most of the day teaching their students about the world and how to succeed in it. Their speciality is {} ".format(self.name,self.age,self.specialty)
        return msg
        
# Child class instance
class Student(Human):
    name = 'Fred'
    species = 'Homosapien'
    major = 'Biology'
    minor = 'History'

    
    def information(self):
        msg = "{}, {} major, works day and night on homework to ace their final exam!".format(self.name, self.major)
        print(msg)


if __name__ == "__main__":
    
     teacher = Teacher()
     
     print(teacher.information())
     
     
    
     

     student = Student()
     
     print(student.information())
     
     
