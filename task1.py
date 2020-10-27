#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grade - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:
    name = ""
    studentNumber = ""
    grade = int()
    courses = []
    grades = []
    
    def getCourses(self,courses):
        self.courses = courses

    def getGrades(self,grade1=0, grade2=0, grade3=0, grade4=0, grade5=0, grade6=0, grade7=0):
       lisgrade = []
       lisgrade.insert(0,grade1)
       lisgrade.insert(1,grade2)
       lisgrade.insert(2,grade3)
       lisgrade.insert(3,grade4)
       lisgrade.insert(4,grade5)
       lisgrade.insert(5,grade6)
       lisgrade.insert(6,grade7)
       self.grades = lisgrade

    def __init__(self,name,studentNumber,grade): # You will need to create your own input parameters for all methods
        self.name = name
        self.studentNumber = studentNumber
        self.grade = grade
    
    def showCourses(self):
        lis = print(self.courses)
        return lis
    
    def showGrades(self, ind):
        classe = self.courses[ind]
        marks = self.grades[ind]
        text = print(self.name + "has an average of "+marks + "% /in " +classe + " .")
        return text

    def average(self):
        length = len(self.grades)
        a = sum(self.grades)
        average  = a/length
        return average
        
    def getHonorRoll (self):
        lisgrades = self.grades
        lisgrades.sort(reverse=True)
        length = len(lisgrades)
        if length >= 5:
            x = lisgrades[0]
            x1 = lisgrades[1]
            x2 = lisgrades[2]
            x3 = lisgrades[3]
            x4 = lisgrades[4]
            hr = (x + x1 + x2 + x3 + x4)/5
            if hr >= 86:
                return True
            else:
                return False
        else:
            text = print("The student is not taking enough courses.")
            return text


    def __del__(self):
        x = print("Thank you for viewing the profile of " + self.name)


def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades([91, 94, 87, 99, 82, 100, 73])

    st2 = student("Joe Lunchbox","12346", 11)
    st1.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st1.getGrades( [71, 98, 93, 95, 68, 81, 71])


main()
