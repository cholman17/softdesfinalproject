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
def simpleRand(listSections, tot): #listSections): #list of lists (sections)
    new = []
    potential = []
    options = []
    SectionS = []
    lazy = None

    for lst in listSections:
        for code in lst:
            for item in code:
                for label in item:
                    pass

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
        for n in listSections: #[ [p p p ], [m m m ], [o,o o] ]
            for m in n: #[ p p p ]
                for item in m:
                    for label in item:
                        new.append(label)
                        SectionS.append(label.num)
            print 'CHECKING SEPARATOR'
            #SectionS.append(item.num)
            #print SectionS[0:2]

    SectionS = [ list(g) for k, g in groupby(SectionS, key=lambda x: x[:8]) ]
    #print SectionS[0]

    print '++++ FINDING COMBINATIONS +++++'
    sample = random.sample(SectionS,10)
    print sample[0]

    randomSlots = random.sample(range(0, len(sample)), 5) #10, 12, 30, 31, 34, 50
    #print randomSlots
    print sample[randomSlots[0]]

    Combo = list(itertools.product( sample[i] for i in randomSlots) )
    print Combo[0]
    #pprint.pprint(Combo)
    print '++++ FOUND COMBINATIONS +++++'

    combo = sorted( Combo, key=lambda x:x[0] ) #combo.sort(key=lambda x: x[0])
    #print combo[0]

    for code in combo: #
        for item in code: #List of CourseNum
            for label in item:
                print label #COURSE NUM
    print len(combo[0])

    looK = []
    for codes in tot:
        for code in codes:
            looK.append(code)
    print looK[0]

    look = []
    for items in looK:
        look.append(items)
    print len(look)
    print type(look[0]) #objct course !!

    for code in combo: #iterate for each requirement
        for item in code: ##new = code.translate(None,''.join(charstoremove)
            for label in item:
                src = label
                print type(src)
                print '+++++++++allCourses+++++++++'
                res = filter(lambda x:str(src) in x.num, look)
                if res:
                    print '\n Found %s MATCH in allCourses' % (len(res))
                    list_op.append(res)
    print len(list_op)

    print '      ++++++++++ COMBO +++++++++++++++        '

    y = 0
    selec = random.sample(list_op, 5)
    for item in selec:
        for ids in item:
            print ids.num
    options.append(selec)
    potential.append(options)

    print '+++++++++++++++ OPTIONS[i] ++++++++++++++'

    a=0
    dets =[]
    for lst in options:
        for ids in lst:
            for labels in ids:
                print '\n '
                print labels.num
                b = str(Course.showdets(labels))
                dets.append(b)
    print len(dets)
    for n in dets:
        print n
    return dets

listSec = [ #for texting

                ['ACC1000-01 ACC1000-02 ACC1000-03 ACC1000-04 ACC1000-05 ACC1000-06 ACC1000-07 ACC1000-08 ACC1000-09 ACC1000-10 ACC1000-11'],
                ['LAW1000-01 LAW1000-02 LAW1000-03 LAW1000-04 LAW1000-05 LAW1000-06 LAW1000-07 LAW1000-08 LAW1000-09 LAW1000-10 LAW1000-11'],
                ['QTM1000-01 QTM1000-02 QTM1000-03 QTM1000-04 QTM1000-05'], ['RHT1000-01 RHT1000-02 RHT1000-03 RHT1000-04 RHT1000-05'],
                ['FYS1000-01 FYS1000-02 FYS1000-03'], ['SME2041-01'], ['QTM2000-01 QTM2000-02 QTM2000-03']

                ]
