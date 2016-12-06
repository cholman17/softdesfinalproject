'''  ATTEMPT #2 -- making a class
fetches course listings and places into txt file
'''
import urllib2
from bs4 import BeautifulSoup
import re
import csv
from itertools import izip
from courseobjects import *

base_url = "https://fusionmx.babson.edu/CourseListing/index.cfm?fuseaction=CourseListing.DisplayCourseListing&blnShowHeader=false&program=Undergraduate&semester=Spring+2017&sort_by=course_number&btnSubmit=Display+Courses"
filename = "courseListing.txt"

courseObj = Course()

class Information(object):
    def __init__(self):
        self.courseNum = []
        self.courseTitle = []
        self.courseDay = []
        self.courseTime = []
        self.courseProf = []
        self.courseCredits = []
        self.allCourses - []

    def getCourseInfo(....): #which variables?
        f = open(filename,"w")

        page = urllib2.urlopen(base_url)
        soup = BeautifulSoup(page, "lxml")

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

        FILE = open("AllCourses.csv", "w")
        for i in xrange(len(courseNum)):
            FILE.write("{};{};{};{};{}\n".format(courseNum[i],courseTitle[i],courseDay[i],courseTime[i],courseProf[i]))
        FILE.close

    def parseCourseInfo(....): #
        ''' sets up list of objects '''
        allCourses.append( courseObj(courseNum, courseTitle, courseDay, courseTime, courseProf) )

    def parse SectionInfo(...):

        pass

    def parseLabInfo(....):

        pass

#allCourses= zip(courseNum,courseTitle,courseDay,courseTime,courseProf,courseCredits)
def main():
    Information.getCourseInfo()
    Information.parseCourseInfo()
    print allCourses[:3]

main()
