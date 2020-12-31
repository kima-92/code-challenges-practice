"""
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. 
All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. 
At each step:

    - If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
    - Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in 
the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial 
queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.
"""

class Solution:
    
    students = []
    sandwiches = []
    
    def countStudents(self, students, sandwiches):
        
        self.students = students
        self.sandwiches = sandwiches
        
        if not self.arraysNotEmpty():
            return 0 
        
        # students are in a QUEUE
        # sandwiches are un a STACK
        
        # If the next student prefers the sandwich that is on the TOP of the stack, they take it and leave
        # Else, the student goes back to the end of the queue (doesn't take the sandwich)
        # Sandwiches DON'T ROTATE

        # When none of the remaining students are able to eat, return the num of students remaining



        while self.arraysNotEmpty() and self.anyoneWantsNextSandwich():
            if self.nextStudentWantsNextSandwich():
                self.removeStudentAndSandwhich()
            else:
                self.sendStudentToTheEnd()

        return len(self.students)


    # send students to the back of the queue
    def sendStudentToTheEnd(self):
        stundet = self.students.pop(0)
        self.students.append(stundet)

    # check if the next student wants the next sandwich
    def nextStudentWantsNextSandwich(self):
        if self.students[0] == self.sandwiches[0]:
            return True
        return False

    # remove happy student and correct sandwich from arrays
    def removeStudentAndSandwhich(self):
        self.students.pop(0)
        self.sandwiches.pop(0)

    def anyoneWantsNextSandwich(self):
        if self.sandwiches[0] in self.students:
            return True
        return False

    # Check if either array is empty
    def arraysNotEmpty(self):
        if self.students == [] or self.sandwiches == [] or self.students == None or self.sandwiches == None:
            return False
        return True





# TESTING
s = Solution()
s.sandwiches = [1,0,0,0,1,1]
s.students = [1,1,1,0,0,1]
#s.sandwiches = []
#s.students = None
print(f"\nOriginal Students: {s.students}\n")

print(s.countStudents(s.students, s.sandwiches))
#s.sendStudentToTheEnd()
#print(s.students)

#print(s.nextStudentWantsNextSandwich())
#print(s.nextStudentWantsNextSandwich())