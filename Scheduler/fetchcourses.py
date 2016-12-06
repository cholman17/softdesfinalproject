''' fetches course listings and places into txt file '''
import urllib2
from bs4 import BeautifulSoup
import re
import csv
from itertools import izip
from audit import *
from creatingwebsite import *
from courseobjects import *
from courseobjects import Course

#Should make all one object class (Information)?
#def __init__(self): pass
#def getCourseInfo(....):
filename = "courseListing.txt"
thefile = open("remaining.txt","r")
f = open(filename,"w")

base_url = "https://fusionmx.babson.edu/CourseListing/index.cfm?fuseaction=CourseListing.DisplayCourseListing&blnShowHeader=false&program=Undergraduate&semester=Spring+2017&sort_by=course_number&btnSubmit=Display+Courses"
page = urllib2.urlopen(base_url)
soup = BeautifulSoup(page, "lxml")

leftovers = thefile.read().split() #['ACC1000', 'FME1000', 'CVA2034', 'ECN2000'] #change to open(file_reqs)
print len(leftovers)

#print soup.prettify()
courseNum = []
courseTitle = []
courseDay = []
courseTime = []
courseProf = []
courseCredits = []
allCourses = []

match = []

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
            time = str("")

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

    for x in range(len(courseNum)):
        allCourses.append( Course(courseNum[x], courseTitle[x], courseDay[x], courseTime[x], courseProf[x]) )
    print 'Made course objects'
    print len(allCourses)
    print allCourses[:3]

#filter.fnmatch(names, pattern) #comparinng codes to courseList
#iterate for the each/length of classes leftover
#matches = [] #list of section lists
def findMatch(response):


    charstoremove = ['[',']','.','"','?','!']
    for code in reqs: #iterate for each requirement
        ##new = code.translate(None,''.join(charstoremove)
        results = filter(lambda x:str(code) in x.num, allCourses)
        print 'Found %s sections for course: %s' % (len(results), code)
        match.append(results)
    for x in range(len(match)):
            return match[x]

def filtering(): # the list, attribute, criteria
    #search through list of objects to group sections together
    b = raw_input('What do you want to filter by: num, title, day, time, prof? ')
    c = raw_input('What is the criteria?: ')
    #d = [] #list of section lists
    #for x in xrange(len(a)):
    try:
        results = filter(lambda x:str(c) in getattr(x,b), allCourses)
        print 'Found %s classes for %s: %s' % (len(results), b, c)
    except NameError:
        print 'Wrong property! Try again.'
        #d.append(results)
