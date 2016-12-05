''' fetches course listings and places into txt file '''
import urllib2
from bs4 import BeautifulSoup
import re
import csv
from itertools import izip
#from courseobjects import *
#from courseobjects import Course

#courseObj = Course()
# I think we should make all one object class (Information)
#def __init__(self): pass
#def getCourseInfo(....):
class Course(object):
    def __init__(self, num, title, day, timeperiod, prof): #add credits, startTime, endTime
        '''constructs the course '''
        #self.dept = str(dept)
        self.num = str(num)
        self.title = str(title)
        self.timeperiod = str(timeperiod)
        self.day = str(day)
        self.sections = []
        self.prof = str(prof)

    def __repr__(self):
        return '%s: %s, %s, %s, %s \n' % (self.num, self.title, self.day, self.timeperiod, self.prof)

    def findTitle(self):
        ''' returns the string for courseTitle '''
        return self.title

    def findDept(self):
        ''' return the department name'''
        return self.dept

    def findNum(self):
        ''' find course number '''
        return self.num

    def findSections(self):
        ''' return list of sections '''

    def SectionsTotal(self):
        ''' displays number of sections offered'''
        return len(self.sections)

    def addSection(self,section):
        '''add to list of sections for specific course '''
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

filename = "courseListing.txt"
f = open(filename,"w")

base_url = "https://fusionmx.babson.edu/CourseListing/index.cfm?fuseaction=CourseListing.DisplayCourseListing&blnShowHeader=false&program=Undergraduate&semester=Spring+2017&sort_by=course_number&btnSubmit=Display+Courses"
page = urllib2.urlopen(base_url)
soup = BeautifulSoup(page, "lxml")

#print soup.prettify()
courseNum = []
courseTitle = []
courseDay = []
courseTime = []
courseProf = []
courseCredits = []
allCourses = []

def getCourseInfo():
    tables = soup.findChildren('table')
    courseListing = tables[1]
    rows = courseListing.findChildren('tr', {"valign" : "top"})

    for row in rows: #should be all rows
        hits = []
        for hit in row.findChildren('td', {"width": "85"}):
            #print hit.contents[0].strip()
            Num = hit.contents[0].strip()
            courseNum.append(Num)
        for hit in row.findChildren('td', {"width": "250"}):
            #print hit.contents[0].text
            Title = hit.contents[0].text
            courseTitle.append(Title)
        hits = row.findChildren('td', {"width": "140"})
        #print hits[0].text
        sched = hits[0].text.strip() #contents[0].strip() #time, day, professor
        dates = re.split(r'\s{2,}', sched)
        day = dates[0]
        day = day.replace(" ","")
        #except (IndexError, TypeError, ValueError):
            #day = str("N?A")
        try:
            time = dates[1].replace(" ","")
        except (IndexError, TypeError, ValueError):
            time = str("N?A")

        courseDay.append(day)
        courseTime.append(time)

        """print '\n******************'
        print Num,
        print day, time
        print '******************\n' """

        #print hits[1].contents[0].strip()
        prof = hits[1].text.strip() #contents[0].strip()
        prof = prof.replace(r'\s{2,}',"")
        courseProf.append(prof)
        info = str(Num)+"   "+str(Title)+"  "+str(day)+"    "+str(time)+"   "+str(prof)
        f.write(str(info)+'\n')

    f.close()

#allCourses= zip(courseNum,courseTitle,courseDay,courseTime,courseProf,courseCredits)

FILE = open("AllCourses.csv", "w")
for i in xrange(len(courseNum)):
    FILE.write("{};{};{};{};{}\n".format(courseNum[i],courseTitle[i],courseDay[i],courseTime[i],courseProf[i]))
FILE.close


def main():
    getCourseInfo()
    for x in range(len(courseNum)):
        allCourses.append( Course(courseNum[x], courseTitle[x], courseDay[x], courseTime[x], courseProf[x]) )
    print 'Made course objects'
    print len(allCourses)
    print allCourses[:3]

main()
