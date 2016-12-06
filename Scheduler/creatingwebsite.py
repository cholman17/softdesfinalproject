from flask import Flask, render_template, request
import fnmatch
import fetchcourses
from audit import audit
from re import split

app=Flask(__name__)

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
    #print matches[:-3]
    print '__________ FILTER LENGTH___________'
    filters = everything[1]
    print len(filters)
    #filters = split(r'(?<=\]),(?=\[)', str(everything[1]))
    #print filters[0]

    return render_template('audit_results.html', response=remaining,match=matches,filter=filters) #response=remaining), match =
    print '*********** SENT ALLL VARS ************'

if __name__ == '__main__':
    app.run(debug=True)
