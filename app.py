"""
Smart G-Forms is an initiative by Team MLXTREME for the Hackathon
HackOff v3.0. It is basically an alternative for Google Forms, with
some additional features such as seeing previously filled forms, and
most importantly, an "AUTOGRADER" for long answer questions. Previously,
we have seen Multiple Choice Questions being graded and long answers
being graded manually. Our form is an attempt to automate this process.
To get a demo, Run app.py and visit the link which comes up.
Regards,
Team MLXTREME
python app.py
"""

# import Flask Library
import os
from flask import Flask, render_template, request, url_for


ROOT_DIR = os.getcwd()


app = Flask(__name__, static_folder="assets")


@app.route('/')
def login():
    return render_template('SigninPage.html')


@app.route('/home', methods=['POST'])
def index():
    return render_template('index.html')



if __name__ == "__main__":
    # import sys
    # print(sys.version)
    # 3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)]
    app.run(debug=True)
    # open
    # maybe it runs now!
