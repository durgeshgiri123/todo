from flask import Flask, request, render_template
from datetime import datetime
import requests
BACKEND_URL = 'http://127.0.0.1:9000'
app = Flask(__name__)
@app.route('/')
def home ():
    return render_template('todo.html')
@app.route('/submittodoitem', methods=['POST'])
def submit ():
    form_data = dict(request.form)
    requests.post(BACKEND_URL + '/submit', json=form_data)
    return ' To Do item Data submitted successfully'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)