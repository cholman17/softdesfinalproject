def matching(schedule):
    f = open('fall_classes_stress.csv')
    stress = []
    for course in f:
        course = course.strip().split(',')
        stress.append(course)

    for classes in stress:
        if classes[0] == schedule:
            return classes[1]
    return 'NA'
