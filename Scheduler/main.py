''' main.py '''
from audit import *
from courseobjects import *
from fetchcourses import *
from creatingwebsite import *

def main():
    print '+++++++++ WEBSITE +++++++++++'
    app.run()

    print '++++++++ GRAB INFO ++++++++'
    took = raw_input('List of classes you have taken, separate by space, e.g. FME1000 FME1001: \n')
    audit(took)
    print '\n++++++++++ FILTER & MATCH +++++++++++'
    fetchAll()

main()
