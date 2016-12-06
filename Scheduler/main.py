''' main.py '''
from audit import *
from courseobjects import *
from fetchcourses import *
#from schedulecourses import *
from creatingwebsite import *

def main():
    print '+++++++ AUDITING ++++++++'
    audit()
    print '++++++++ GRAB INFO ++++++++'
    getCourseInfo()
    print '++++++++++ FILTERS +++++++++++'
    filtering()
    print '++++++++++ MATCHES +++++++++++'
    findMatch(leftovers)
    app.run()

main()
