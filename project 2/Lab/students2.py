from dataclasses import dataclass

@dataclass
class Student: # this will hold all the info of a students information
    name: str #this is the name in a str 
    school_id: str #this is the school ID in a str 
    gpa: float #gpa in float 

    def __str__(self): # this will return the input for the print 
        return f'Student name: {self.name}, School ID: {self.school_id}, GPA: {self.gpa}'


def main(): #main function that will hold the created names and string 
    alex = Student('Alex', 'abcdef', 3.6)
    print(alex.name) 
    print(alex.school_id)
    print(alex)

    sam = Student('Sam', 'ghijkl', 3.7)
    print(sam)

main()
