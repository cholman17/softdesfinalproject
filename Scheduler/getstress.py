def matching(lect):
    stress = {}
    with open('fall_classes_stress.csv') as f:
        for line in f:
            line = line.strip()
            (key, val) = line.split(",")
            stress[key] = val
    #print stress.items()[0]

    '''for course in f:
        course = course.strip().split(',')
        stress.append(course) #list of classes'''

    val = stress.get(str(lect),"NA")
    return val

#print matching('ACC1000')
