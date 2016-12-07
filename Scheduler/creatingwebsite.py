from flask import Flask, render_template, request
import fnmatch
import fetchcourses
from fetchcourses import *
import schedulecourses
from schedulecourses import *
from audit import audit
from re import split

app=Flask(__name__)
randLst = []
total = []

@app.route('/')
def index():
    return render_template('index.html') # form=form)

@app.route('/audit_results', methods=['POST'])
def get_classes():
    response = request.form["response"].encode('utf-8')
    print response
    print len(response)
    remaining = audit(response)
    print '****** GOT REMAINING **********'

    b = request.form["cat"].encode('utf-8')
    #print b
    #print '********* FOUND b *************'
    c = request.form["label"].encode('utf-8')
    #print c
    #print '************* FOUND c ************'

    everything = fetchcourses.fetchAll(b,c)
    matches = everything[0]
    randLst.append(everything[0])
    #print matches[:-3]
    print '__________ FILTER LENGTH___________'
    filters = everything[1]
    print len(filters)
    #filters = split(r'(?<=\]),(?=\[)', str(everything[1]))
    #print filters[0]

    return render_template('audit_results.html', response=remaining,match=matches,filter=filters) #response=remaining), match =
    print '*********** SENT ALLL VARS ************'

@app.route('/create_schedule', methods=['POST'])
def make_schedule():
    tot = fetchcourses.allCourses
    total.append(tot[0:])

    print len(tot)
    print len(total)
    listSect = randLst
    print listSect

    option = schedulecourses.simpleRand(listSect, total)
    options = []
    for id in option:
        b=id.split(",")
        print b
        c=";".join(b)
        print c
        options.append(str(c))

    print '++++++++++ FLASK DETS ++++++++++++++++'
    print len(options)
    print options[0]

    return render_template('create_schedule.html',sets=options)


if __name__ == '__main__':
    app.run(debug=True)
