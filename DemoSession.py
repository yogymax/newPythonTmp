
class Course :

    def __init__(self,cid,cname,fees = 10000):
        self.courseId = int(cid)
        self.courseName = cname
        self.courseFees = fees

    def __str__(self):
        return '\n CourseId : {}, CourseName : {} , CourseFees : {}'.format(self.courseId,self.courseName,self.courseFees)

    def __repr__(self):
        return str(self)

    def __gt__(self, other):
        return self.courseName < other.courseName



c1 = Course(12,'Abc')
c2 = Course(122,'ZyAtbc',23123)
c3 = Course(142,'tArbc',12412)
c4 = Course(612,'fAbc',41455)
c5 = Course(712,'asAbc',4312)



listOfCouses = [c1,c2,c3,c4,c5]

listOfCouses.sort()
print(listOfCouses)