import fnmatch

still_need = []
response = raw_input("Enter classes taken by course code, separated by a space ex, e.g. 'FME1000 FME1001 ECN2000' \n")
def audit():
    thefile = open('remaining.txt','w')
    req = []
    f = open('babson_requirements.csv')
    for line in f:
        line = line.split()
        req.append(line)

    remaining = []
    classes = response.split()
    have = classes
    needed = req

    charstoremove = ['[',']','.','"','?','!']

    for code_lst in needed:
        is_present = False
        for requirement in code_lst:
            if requirement in have or fnmatch.filter(have, requirement):
                is_present = True

                for i in range(len(have)):
                    if [have[i]] == (fnmatch.filter([have[i]], requirement)):
                        have = have[:i]+ have[i+1:]
                        break
                    break
        if is_present == False:
            remaining.append(code_lst)
            still_need.append(code_lst)
            #print remaining

    for item in still_need:
        for code in item:
            #still_need.translate(None,''.join(charstoremove))
            #new = code.translate(None,''.join('?'))
            thefile.write("%s \n" % code)

    return remaining

audit()
