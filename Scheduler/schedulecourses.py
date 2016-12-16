''' COMPUTE THE SCHEDULE '''
import fetchcourses
from fetchcourses import *
import itertools
from itertools import groupby
from courseobjects import *
import pprint
import random

'''
DONT FORGET: How to implement '???' classes for matches/remaining

(1) using matches --> list of potential schedules of 5 classes
    - import itertools
    - import fetchcourses
    - simple string == clause

(2) add rule to check for course.time attribute
    - need to setup startTime and endTime attributes ==> Course()

(3) add stressLevel (points) --> rule factor for randomization

'''

list_op = [] #not sure yet
#section = raw_input('Enter all the sections of a course: ')
new = []
selec = []
potential = []
options = []
SectionS = []
looK = []
look = []
selecting = []

def conflict(choice, selections):
    for lect in selections:
        print '++++ A SELECTION ++++'
        print lect
        if choice.num != lect.num:
            print 'Not Same Title'
            if choice.day == lect.day:
                if choice.startTime == lect.startTime:
                    return True
                if choice.endTime == lect.endTime:
                    return True
    return False

def simpleRand(listSections, tot): #listSections): #list of lists (sections)
    SectionS = []
    new = []
    potential = []
    options = []
    SectionS = []
    looK = []
    look = []
    selecting = []
    selec = []

    refresh()

    lazy = None
    File = open("selection.txt", "w")
    FILE = open("looK_list.txt", "w")

    for lst in listSections:
        for code in lst:
            for item in code:
                for label in item:
                    pass
    #print listSections

    print '++++++++++ STRING ++++++++++++++'
    a=0
    for lst[0] in listSections[0]:
        for code[0] in lst[0]:
            for item in code[0]:
                if a < 3:
                    a += 1
                    '''print '00000000000000000000000000000000000000'
                    print item.num'''
                    lazy = item
                else: break
            break
        break

    print str(type(lazy)) ##<class 'courseobjects.Course'>

    if  '<cla' in str(type(lazy)):
        print '+++++++ TRUE: COURSE OBJECT+++++++++++'
        #for x in xrange(0, len(listSections)):
        for n in listSections: #[ [p p p ], [m m m ], [o,o o] ]
            for m in n: #[ p p p ]
                for item in m:
                    for label in item:
                        #print type(label)
                        #print label.num
                        new.append(item)
                        SectionS.append(label) #item.num)
            print 'CHECKING SEPARATOR'
            #SectionS.append(item.num)
            #print SectionS[0:2]

    SectionS = [ list(g) for k, g in groupby(SectionS, key=lambda x: x) ]
    print SectionS[0]

    print '++++ FINDING COMBINATIONS +++++'
    sample = random.sample(SectionS,10)
    print sample[0]

    randomSlots = random.sample(range(0, len(sample)), 5) #10, 12, 30, 31, 34, 50
    #print randomSlots
    print sample[randomSlots[0]]

    Combo = list(itertools.product( sample[i] for i in randomSlots) )
    #print Combo[0]
    #pprint.pprint(Combo)
    print '++++ FOUND COMBINATIONS +++++'

    combo = sorted( Combo, key=lambda x:x[0] ) #combo.sort(key=lambda x: x[0])


    for code in combo: #Tuple
        for item in code: #List of CourseNum
            for label in item:
                #print label #COURSE NUM
                pass
    #print len(combo[0])

    for codes in tot:
        for code in codes:
            looK.append(code)
    #print looK[0]

    for items in looK:
        look.append(items)
    #print len(look)
    #print type(look[0]) #objct course !!

    '''for code in look:
        #print 'TYPE: '+str(type(code))
        FILE.write("{};{}   ".format(code.num,code.sect))'''
    FILE.close

    print '    +++++ RES FILTER +++++++++++++ '

    for code in combo: #iterate for each requirement
        for item in code: ##new = code.translate(None,''.join(charstoremove)
            for label in item:
                src = label
                #print str(src)[:7]
                src = str(src)[:7]
                #print label.num
                print '+++++++++allCourses+++++++++'
                res = filter(lambda x:str(src) in x.num, look)
                if res:
                    print '\n Found %s MATCH in allCourses' % (len(res))
                    list_op.append(res)
                    for code in res:
                        #print 'TYPE: '+str(type(code))
                        File.write("{};{}   ".format(code.num,code.sect))
    print len(list_op)

    File.close
#Make separate fxn
    print '      ++++++++++ COMBO +++++++++++++++        '

    y = 0

    for course in random.sample(list_op, len(list_op)):
        for section in course:
            print '+++++++++SELECTING++++++++++'
            if not conflict(section,selecting):
                selecting.append(section)
                print '__________ NO CONFLICT __________'
                print section
                print section.day, section.startTime
                break
    print type(selecting)
    print selecting

    try:
        selecting = set(selecting)
    except TypeError:
        print 'EXCEPT'
        for i in selecting:
            if i not in selec:
                selec.append(i)
        selecting = selec
    print len(selecting)
    print len(selec)
    #options.append(selec)
    #potential.append(options)

    print '   +++++++++++++++ OPTIONS[i] ++++++++++++++    '

    a=0
    #dets =[]
    for lect in selecting:
        print '++++++++++++++++++++'
        print lect.num
        print lect.day
        print lect.startTime
        print lect.endTime

    return selecting

def refresh():
    new[:] = []
    selec[:] =[]
    potential[:] = []
    options[:] = []
    SectionS[:] = []
    looK[:] = []
    look[:] = []
    selecting[:] = []
    list_op[:] = []

listSec = [ #for texting

                ['ACC1000-01 ACC1000-02 ACC1000-03 ACC1000-04 ACC1000-05 ACC1000-06 ACC1000-07 ACC1000-08 ACC1000-09 ACC1000-10 ACC1000-11'],
                ['LAW1000-01 LAW1000-02 LAW1000-03 LAW1000-04 LAW1000-05 LAW1000-06 LAW1000-07 LAW1000-08 LAW1000-09 LAW1000-10 LAW1000-11'],
                ['QTM1000-01 QTM1000-02 QTM1000-03 QTM1000-04 QTM1000-05'], ['RHT1000-01 RHT1000-02 RHT1000-03 RHT1000-04 RHT1000-05'],
                ['FYS1000-01 FYS1000-02 FYS1000-03'], ['SME2041-01'], ['QTM2000-01 QTM2000-02 QTM2000-03']

                ]
