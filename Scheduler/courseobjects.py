'''creates the objects for a course

TO-DO:
reformat fetchcourses.py to split start & end times? OR
just indicate where to start reading characters in table

'''


class Course(object):
    def __init__(self, num, title, day, timeperiod, prof): #add credits, startTime, endTime
        #constructs the course
        #self.dept = str(dept)
        self.num = str(num)
        self.title = str(title)
        self.timeperiod = str(timeperiod)
        self.sections = []
        self.prof = str(prof)
        self.day = str(day)

    def __repr__(self):
        #return '%s: %s, %s, %s, %s, %s' % (num, title, day, timeperiod, prof)
        return self.num
        
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
        #return list of sections '''
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
'''
class Classtime(object):
    def __init__(self,name,timeslot):
        self.name = str(name)
        self.timeslot = timeslot

    def findName(self):
        return self.name
    def findTimeslot(self):
        return self.timeslot
    def findDays(self):
        return self.timeslot.findDays()
    def findStart(self):
        return self.timeslot.findStart
    def findEnd(self):
        return self.timeslot.findEnd()

class Section(Classtime): #labs, lecture, studio, etc
    def __init__(self,name,timeslot):
        super(Section,self).__init__(name,timeslot)
        self.labs = []
        self.lectures = [] #not needed per say
        self.studio = [] #not needed per say either

    def findLabs(self):
        return self.labs

    def LabsTotal(self):
        return len(self.labs)

    def addLab(self,lab):
        if type(lab) == Lab:
            self.labs.append(lab)
            return True
        return False

    def deleteLab(self,lab):
        self.labs.remove(lab)
        if len(self.labs) == 1:
            return -1
        return 0

    def setupLabs(self, newLabs):
        self.labs = newLabs

class Lab(Classtime):
    def __init__(self,name,timeslot):
        super(Lab, self).__init__(name,timeslot)

    #need equivalence test --> no duplicates

    def __hash__(self): #for dictionairy keys
        return hash((self.findDays(), self.findStart(),self.findEnd()))

class Timeslot(object):
    def __init__(self,day,start,end):
        self.day = str(day)
        self.start = self.string2military(start)
        self.end = self.string2military(end)

    #need equivalence test --> no duplicates

    def findDays(self):
        return self.days

    def findStart(self):
        return self.start
    def findEnd(self):
        return self.end
    def string2military(self, t): #string to military time
        #http://stackoverflow.com/questions/19229190/convert-12-hour-into-24-hour-times
        currenttime = datetime.datetime.now().time.strftime(%H:%M")
        time2 = time #from sheet
        time2cut = time2.split(":")
        if currenttime >= "10:00" and currenttime <= "13:00":
            if time2 >= "10:00" and time2 >= "12:00":
                time2 = ("""%s%s""" % (time2, "AM"))
            else:
                time2 = ("""%s%s""" % (time2, "PM"))
        else:
            time2 = ("""%s%s""" % (time2, "PM"))
        time2 = datetime.datetime.strptime(time2, '%I:%M %p')
        time2 = time2.strftime("%H:%M %p")
        time2 = time2[:-3]
        print time2

'''
