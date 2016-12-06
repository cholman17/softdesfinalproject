''' main.py '''
from audit import *
from courseobjects import *
from fetchcourses import *
#from schedulecourses import *
from creatingwebsite import *

def main():
    print '+++++++++ WEBSITE +++++++++++'
    app.run()

    print '++++++++ GRAB INFO ++++++++'
    getCourseInfo()
    print '\n++++++++++ FILTERS +++++++++++'
    filtering()
    print '++++++++++ MATCHES +++++++++++'
    findMatch(response)

main()
