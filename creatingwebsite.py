from flask import Flask, render_template, request
import fnmatch
from audit import audit

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/audit_results', methods=['POST'])
def get_classes():
    response = request.form["response"].encode('utf-8')
    audit(response)
    return render_template('audit_results.html')

if __name__ == '__main__':
    app.run()
