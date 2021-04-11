"""
python hack_app.py
"""

import re
import os

from flask import Flask, render_template, request, url_for
from implementDB import *


"""
python studTeach.py
"""
newCounter = {"c": 0}
CurrentUser = dict()
TEMPLATE_FOLDER = "templates_final"
app = Flask(__name__, template_folder=TEMPLATE_FOLDER,
            static_folder="assets_final")

# app = Flask(__name__, static_folder="assets_final",
#           template_folder="templates_final")
ROOT_DIR = os.getcwd()
rewriteFileName = 'TF.html'
rewriteFilePath = os.path.join(ROOT_DIR, TEMPLATE_FOLDER, rewriteFileName)


def getshortString(ID=1, iterator=None):
    ShortStr = f"""
    <!--Add a Short BoxID{ID}-->
            <div class="margin-top-bottom box question-box question" data-id="881">
                <input type="text" data-id="881" class="question-title edit-on-click input-question"
                    name="ShortQuestion{iterator}" value="Short Question Here">
                <b>Type :</b> Short
                <div class="answers" data-id="882">
                    <textarea class="long-answer" placeholder="Short Answer Type" name="ShortAnswer{iterator}">
                    </textarea>
                </div>
            </div>
    <!--End a BoxID{ID}-->
    """
    return ShortStr


def getlongString(ID=2, iterator=None):
    LongStr = f"""
        <!--Add another BoxID{ID}-->
            <div class="margin-top-bottom box question-box question" data-id="882">
                <input type="text" data-id="882" class="question-title edit-on-click input-question"
                    value="Long Question Here" name="LongQuestion{iterator}">
                <b>Type :</b> Long
                <div class="answers" data-id="885">
                    <textarea class="long-answer" placeholder="Long Answer Type" name="LongAnswer{iterator}"></textarea>
                </div>
            </div>
        <!--End another BoxID{ID}-->
    """
    return LongStr


def getCheckString(ID=3, iterator=None):

    CheckStr = f"""
        <!--Add another BoxID{ID}-->
        <div class="margin-top-bottom box question-box question" data-id="884">
            <input type="text" data-id="884" class="question-title edit-on-click input-question"
                value="Radio Button Question Here" name="RadioQuestion{iterator}">
            <b>Type :</b> Radio

            <div class="choices" data-id="884">

                    <input type="radio" id="937" name="RadioVal{iterator}" value="1">
                    <label for="933">
                        <input type="text" data-id="937" class="edit-choice" value="Option 1" name  = "RadioVal{ID}Head1">
                    </label> <br>

                    <input type="radio" id="930" name="RadioVal{iterator}" value="2">
                    <label for="933">
                        <input type="text" data-id="930" class="edit-choice" value="Option 2" name="RadioVal{ID}Head2">
                    </label> <br>

                    <input type="radio" id="933" name="RadioVal{iterator}" value="3">
                    <label for="933">
                        <input type="text" data-id="933" class="edit-choice" value="Option 3" name="RadioVal{ID}Head3">
                    </label> <br>
 
                    <input type="radio" id="933" name = "RadioVal{iterator}" value="4">
                    <label for="933">
                        <input type="text" data-id="933" class="edit-choice" value="Option 4" name="RadioVal{ID}Head4">
                    </label> <br>
            </div>
        </div>
        <!--End another BoxID{ID}-->
    """
    return CheckStr


def rewriteHTML(ID=1, iterator=1, str_to_add=None):
    choice = {1: getshortString, 2: getlongString, 3: getCheckString}
    chosenFunc = choice[ID]

    str_to_add = chosenFunc(iterator=iterator)
    txt = readHTML(rewriteFilePath)
    linesadded = findLineNumber(txt, "<!--End")
    print(linesadded)
    addtoHTMLFile(txt, pos=linesadded[-1]+1, str_to_add=str_to_add)
    return 1


def readHTML(FilePath):
    with open(FilePath, "r") as f:
        return f.readlines()


def writeHTML(FilePath, txt):
    with open(FilePath, "w") as f:
        for row in txt:
            if not str(row).strip() == "":
                f.write(str(row) + '\n')


def addtoHTMLFile(txt, pos, str_to_add, fpath=rewriteFilePath):
    sub_txt = txt[:pos]
    sub_txt.extend(str_to_add.split('\n'))
    sub_txt.extend(txt[pos:])
    writeHTML(fpath, sub_txt)
    # return sub_txt


def deletefromHTMLFile(ID=1, fpath=rewriteFilePath, removeAll=False):
    """
    First get start and end
    """
    txt = readHTML(rewriteFilePath)
    if removeAll == False:
        string_to_search = "BoxID{0}-->".format(ID)
    else:
        string_to_search = "BoxID"
    lines_found = findLineNumber(txt, string_to_search)
    to_remove = []
    for start, stop in zip(lines_found[::2], lines_found[1::2]):
        for i in range(start, stop+1):
            print(i)
            to_remove.append(i)
    deleted_txt = [i for j, i in enumerate(txt) if j not in to_remove]
    writeHTML(fpath, deleted_txt)
    return 1


def findLineNumber(main_lst, search_string):
    """
    x = re.search("<!--Add a Box-->", txt)
    """
    Lines = []
    for i, each in enumerate(main_lst):
        if re.search(search_string, each):
            Lines.append(i)
            # yield i

    return Lines


def logger(line):
    with open('dyn_log.txt', 'a+') as f:
        f.write(str(line)+"\n")


@app.route('/getinfo', methods=["POST", "GET"])
def no():
    # print(request.form)
    resp = request.form
    deletefromHTMLFile(removeAll=True)
    resp = dict(resp)
    print(resp)
    for each in resp:
        resp[each] = "".join(resp[each]).strip()
    return render_template('form_submit.html')


@app.route('/index2.html')
def create():
    return render_template(rewriteFileName)


@app.route('/CreateAForm.html')
def create2():
    return render_template(rewriteFileName)


@app.route('/reset')
def reset():
    deletefromHTMLFile(removeAll=True)
    return render_template(rewriteFileName)


counter = {1: 0, 2: 0, 3: 0}


@app.route('/addshort')
def addshort():
    ID = 1
    counter[ID] += 1
    x = rewriteHTML(ID=ID, iterator=counter[ID])
    return render_template(rewriteFileName)


@app.route('/addlong')
def addlong():
    ID = 2
    counter[ID] += 1
    x = rewriteHTML(ID=ID, iterator=counter[ID])
    return render_template(rewriteFileName)


@app.route('/addcheck')
def addcheck():
    ID = 3
    counter[ID] += 1
    x = rewriteHTML(ID=ID, iterator=counter[ID])
    return render_template(rewriteFileName)


@app.route('/', methods=['POST', 'GET'])
def login():
    """
    username = request.form["username"]
    password = request.form["password"]
    CurrentUser["username"] = username
    CurrentUser["password"] = password
    """
    return render_template('loginPage.html')


@app.route('/home', methods=['POST'])
def homepage():
    return render_template('index.html')


@app.route('/index.html')  # ,methods=['POST'])
def homepage2():
    return render_template('index.html')


@app.route('/AlreadyFilledForms.html')
def AlreadyFilledForms():
    return render_template('AlreadyFilledForms.html')


@app.route('/viewscore1', methods=['POST'])
def submitsuccess():
    return render_template('sucess.html')


@app.route('/viewscore', methods=['POST'])
def score():
    sval = newCounter["c"]
    newCounter["c"] += 1
    if sval % 2:
        sval = 9
    else:
        sval = 3
    return render_template('viewscore.html', s=sval)


@app.route('/CreatedForms.html')
def CreatedForms():
    return render_template('CreatedForms.html')


@app.route('/filledform1', methods=['POST'])
def filledalready():
    return render_template('DisplayAlreadyFilledForms.html')


@app.route('/createdform1', methods=['POST'])
def createdshow():
    return render_template('DisplayCreatedForms.html')

###
@app.route('/fillaform')
def fillaform():
    return render_template('Studentsform.html')


@app.route('/Fillaform.html')
def fillourform():
    return render_template('Studentsform.html')


# @app.route('/CreateAForm.html')  # , methods=['POST'])
# def createform():
#    return render_template('TeachersForm.html')


if __name__ == "__main__":
    app.run(debug=True)
