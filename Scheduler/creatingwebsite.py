from flask import Flask, render_template, request
import fnmatch
from audit import audit
from main import main

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/audit_results', methods=['POST'])
def get_classes():
    response = request.form["response"].encode('utf-8')
    remaining = audit(response)
    return render_template('audit_results.html',response=remaining)

def make_schedule():
    sample_schedule = main()
    return render_template('create_schedule.html', response=sample_schedule)

if __name__ == '__main__':
    app.run()
