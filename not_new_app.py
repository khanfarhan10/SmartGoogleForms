"""
python not_new_app.py
"""

from flask import *


app = Flask(__name__,template_folder="templates_old")

@app.route('/')
def create():
    return render_template('not_index.html')


def logger(line):
    with open('log.txt','a+') as f:
        f.write(str(line)+"\n")

@app.route('/no',methods=["POST","GET"])
def no():
    resp = request.form['feedurl[]']
    logger(request.form.getlist('feedurl[]'))
    print(request.form.getlist('feedurl[]'))
    #questions array 
    #sample answers array 
    # form id || questions array  || sample answers array || responses 
    return str(request.form.getlist('feedurl[]'))

if __name__ == "__main__":
    app.run(debug=True)