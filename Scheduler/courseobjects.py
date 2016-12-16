'''creates the objects for a course

TO-DO:
reformat fetchcourses.py to split start & end times? OR
just indicate where to start reading characters in table

'''


class Course(object):
    def __init__(self, num, sect, title, day, startTime, endTime, prof, stress): #add credits, startTime, endTime
        #constructs the course
        #self.dept = str(dept)
        self.num = str(num)
        self.sect = str(sect)
        self.title = str(title)
        self.startTime = str(startTime)
        self.endTime = str(endTime)
        self.sections = []
        self.prof = str(prof)
        self.stress =str(stress)
        self.day = str(day)

    def showdets(self):
        return '%s-%s: %s, %s, %s-%s, %s' % (self.num,self.sect, self.title, self.day, self.startTime, self.endTime, self.prof)

    def __str__(self):
        return '%s-%s' % (self.num,self.sect)

    def findTitle(self):
        #returns the string for courseTitle
        return self.title

    def findDept(self):
        #return the department name'''
        return self.dept

    def findNum(self):
        #find course number '''
        return self.num

    def findSections(self):
        return self.sect
        pass

    def SectionsTotal(self):
        #displays number of sections offered'''
        return len(self.sections)

    def addSection(self,section):
        #add to list of sections for specific course '''
        if type(section) == Section:
            self.sections.append(section)
            return True
        return False

    def deleteSection(self, section):
        self.sections.remove(section)
        if len(self.sections) == 0:
            return -1
        return 0

    def setupSections(self,newSections):
        self.sections = newSections
