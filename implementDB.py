"""
python implementDB.py
"""
import os
import pandas as pd
from pandas import ExcelWriter

# import sqllite3


ROOT_DIR = os.getcwd()
DataBaseName = "data.xlsx"
DataBasePath = os.path.join(ROOT_DIR, "Databases", DataBaseName)
"""
isUser
createUser
username	password
khanfarhan10	swagger101
"""
UserData = pd.read_excel(
    DataBasePath, sheet_name="UserData", engine='openpyxl')
"""
- createForm
- readCreatedForm
showFormResponses
FormID	FormOwner	FormData
1	khanfarhan10	list([FormTitle:str,FormDescription:str,(Questions,Type) - dict,(Questions,list(SampleAnswers)) - dict])
"""
CreatedForms = pd.read_excel(
    DataBasePath, sheet_name="CreatedForms", engine='openpyxl')
"""
- fillForm
- readfilledForm
- evaluateForm
FormID	FormOwner	FormResponseID	FormResponses
1	khanfarhan10	54	            (Questions , Answers) - dict
"""
FilledForms = pd.read_excel(
    DataBasePath, sheet_name="FilledForms", engine='openpyxl')


def createUniqueFormID():
    x = list(CreatedForms["FormID"])
    return max(x)+1


def createForm(FormOwner, FormTitle, FormDescription, QuestionType, QuestionAns):
    global CreatedForms
    FormData = [FormTitle, FormDescription, QuestionType, QuestionAns]
    FormID = createUniqueFormID()
    to_add = merge_list_to_dict(["FormID", "FormOwner", "FormData"], [
                                FormID, FormOwner, FormData])
    CreatedForms = CreatedForms.append(to_add, ignore_index=True)
    return FormID


def readCreatedForm(FormID):
    listofFormIDs = CreatedForms["FormID"]
    get_index = listofFormIDs.index(FormID)
    newFormID, FormOwner, FormData = CreatedForms.loc[get_index, :]
    FormTitle, FormDescription, QuestionType, QuestionAns = FormData
    return FormOwner, FormTitle, FormDescription, QuestionType, QuestionAns


def fillForm(FormID, FormOwner, FormResponses):
    global FilledForms
    FormResponseID = createUniqueFormResponses()
    to_add = merge_list_to_dict(["FormID", "FormOwner", "FormResponseID", "FormResponses"],
                                [FormID, FormOwner, FormResponseID, FormResponses])
    FilledForms = FilledForms.append(to_add, ignore_index=True)
    return FormResponseID


def createUniqueFormResponses():
    x = list(FilledForms["FormResponseID"])
    return max(x)+1


def readfilledForm(FormResponseID=None, FormID=None):
    listofFormResponseIDs = FilledForms["FormResponseID"]
    get_index = listofFormResponseIDs.index(FormResponseID)
    FormID, FormOwner, FormResponseID, FormResponses = FilledForms.loc[get_index, :]
    return FormID, FormOwner, FormResponseID, FormResponses
    # if FormID is not None :

# evaluateForm


def getdictsForm(FormResponseID=None):
    FormID, FormOwner, FormResponseID, FormResponses = readfilledForm(
        FormResponseID)
    FormOwner, FormTitle, FormDescription, QuestionType, QuestionAns = readCreatedForm(
        FormID)
    return QuestionAns, FormResponses


def logger(line):
    with open('data_log.txt', 'a+') as f:
        f.write(str(line)+"\n")


def merge_list_to_dict(test_keys, test_values):
    """Using dictionary comprehension to merge two lists to dictionary"""
    merged_dict = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
    return merged_dict


def createUSER(username, password):
    global UserData
    isaUser = isUSER(username, password)
    # print(UserData.head())
    # print(username, password)
    # print(isaUser)
    if isaUser[0] == True:
        return False
    UserInfo = merge_list_to_dict(
        ["username", "password"], [username, password])
    UserData = UserData.append(UserInfo, ignore_index=True)
    return True


def isUSER(username, password):
    """
    returns isUSERNAME correct, isPASSWORD correct
    """
    usr = UserData["username"].to_dict()
    listofUsers = list(UserData["username"])
    if username in listofUsers:
        # print('Is a User')
        getindex = listofUsers.index(username)
        listofPasswords = list(UserData["password"])
        # print(getindex)
        if listofPasswords[getindex] == password:
            # print('Password Correct')
            return True, True
        return True, False
    return False, False


def saveDataFrame():
    dfs = [UserData, CreatedForms, FilledForms]
    dfnames = ["UserData", "CreatedForms", "FilledForms"]
    writer = ExcelWriter(DataBasePath)
    for df, dfname in zip(dfs, dfnames):
        df.to_excel(writer, dfname, index=False)
    writer.save()


if __name__ == "__main__":
    logger(createUSER(username="khanfarhan10", password="habijabi"))
    logger(createUSER(username="damik", password="abcd"))
    createForm(FormOwner="damikdhar", FormTitle="Main", FormDescription="some txt here",
               QuestionType={"Q1": "Long", "Q2": "MCQ"},
               QuestionAns={"Q1": "aNS1", "Q2": "aNS2"})

    saveDataFrame()
    print("DB Updated")
