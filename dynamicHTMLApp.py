"""
python dynamicHTMLApp.py
"""

from flask import Flask, render_template, request, url_for
import os
import re

TEMPLATE_FOLDER = "templates_rewrite"
app = Flask(__name__, template_folder=TEMPLATE_FOLDER)


ROOT_DIR = os.getcwd()
rewriteFileName = 'not_index.html'
rewriteFilePath = os.path.join(ROOT_DIR, TEMPLATE_FOLDER, rewriteFileName)


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


def deletefromHTMLFile(ID=1234, fpath=rewriteFilePath):
    """
    First get start and end
    """
    txt = readHTML(rewriteFilePath)
    string_to_search = "BoxID{0}-->".format(ID)

    lines_found = findLineNumber(txt, string_to_search)
    to_remove = []
    for start, stop in zip(lines_found[::2], lines_found[1::2]):
        for i in range(start, stop+1):
            to_remove.append(i)
    deleted_txt = [i for j, i in enumerate(txt) if j not in to_remove]
    writeHTML(fpath, deleted_txt)
    return 1


def findLineNumber(main_lst, search_string):
    """
    x = re.search("<!--Add", txt)
    """
    Lines = []
    for i, each in enumerate(main_lst):
        if re.search(search_string, each):
            Lines.append(i)
            # yield i

    return Lines


def rewriteHTML(ID=1234):
    txt = readHTML(rewriteFilePath)
    linesadded = findLineNumber(txt, "<!--End a Box-->")
    print(linesadded)
    str_to_add = """
    <!--Add another BoxID{0}-->
    <tr>
        <td valign=top> Feed URL (s):</td>
        <td valign=top>
            <div id="newlink">
                <div class="feed">
                <input type="text" name="feedurl[]"  >
                </div>
            </div>
        </td>
    </tr>
    <!--End another BoxID{1}-->
    """.format(ID, ID)
    addtoHTMLFile(txt, pos=linesadded[0]+1, str_to_add=str_to_add)


def logger(line):
    with open('dyn_log.txt', 'a+') as f:
        f.write(str(line)+"\n")


@app.route('/getinfo', methods=["POST", "GET"])
def no():
    resp = request.form['feedurl[]']
    logger(request.form.getlist('feedurl[]'))
    print(request.form.getlist('feedurl[]'))
    return "10"


@app.route('/')
def create():
    return render_template(rewriteFileName)


@app.route('/reset')
def reset():
    deletefromHTMLFile()
    return render_template(rewriteFileName)


@app.route('/add')
def add():
    rewriteHTML()
    return render_template(rewriteFileName)


if __name__ == "__main__":
    app.run(debug=True)
    # rewriteHTML()
