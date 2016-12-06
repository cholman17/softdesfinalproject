from flask import Flask, render_template, request
import fnmatch
from audit import audit
from fetchcourses import *
from fetchcourses import *

app=Flask(__name__)


@app.route('/')
def index():
    #form = InputForm(request.form) #added
    #print form
    return render_template('index.html') # form=form)

@app.route('/audit_results', methods=['POST'])
def get_classes():
    response = request.form["response"].encode('utf-8')
    print response
    print len(response)
    remaining = audit(response)
    print '****** GOT REMAINING **********'

    matches = findMatch(remaining)
    print len(matches)
    print '*********** FOUND MATCHES ***************'

    b = request.form["cat"].encode('utf-8')
    print b
    print '********* FOUND b *************'
    c = request.form["label"].encode('utf-8')
    print c
    print '************* FOUND c ************'

    filters = filtering(b,c)
    print len(filters)
    print '*********** FILTERING ********* '

    return render_template('audit_results.html', response=remaining,match=matches,filter=filters) #response=remaining), match =
    print '*********** SENT LOCALS ************'

if __name__ == '__main__':
    app.run(debug=True)
