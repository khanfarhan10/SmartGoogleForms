# SMART-Google-Forms
`Search Map AutoGrading-Based Recurrent-Network Trained (SMART) Google Forms` 

<p align="center">
  <img width="300" height="250" src="https://i.ibb.co/sHF9d7k/Smart-GForms.png">
</p>

<p align="center">
<a href="LICENSE"><img alt="GitHub" src="https://img.shields.io/github/license/soumya997/Smart-Exam-Form?style=for-the-badge"></a>
  <img src="https://forthebadge.com/images/badges/built-with-love.svg">     <img src="https://forthebadge.com/images/badges/made-with-python.svg">    <img src="https://forthebadge.com/images/badges/open-source.svg">
</p>

by `Team MLXTREME` (Team Machine Learning eXceptional Technological Resolutions Engineering and Managerial Enterprises) 

- Ever Faced Issues Grading Thousands of Long Answers from your Community? 
- Wanted to fully Automate the process of Form Fillups? 

<p align="center"> Don't worry, <b>SMART-Google-Forms</b> has you covered. </p>
 
<h4 align="center">
Smart Google Forms provides AutoGrading Solutions for all Type of Long Answer-Type Questions.<br>
Rebuilding Forms, powered by <b>Artificial Intelligence Technologies</b>.
</h4>

---

## Why SMART-Google-Forms (Inspiration/Problem Statement)

- Various Grading Technologies exist for Simple Forms with MCQs (Objective Answer Type), but there are no such known Technologies that can Grade Long (Subjective Answer Type) Questions.
- Teachers often spend many hours Grading Student Response Sheets, and this can be Automated to provide Assistive Technology for better Education. 


## What it does (Proposed Solution)

- With Smart-Google-Forms Teachers don't have to check each Answer, rather they can provide a generalized Answer for Questions and our Natural Language Processing (NLP) based Predictions will Score them on the basis of the Sample Answers provided by the Teacher. 
- Saves Time, Easy to Use, User Friendly Platform that provides a UI similar to the popular Google Forms.

## How we built it (Technological Stack Used)
- FrontEnd : `CSS`, `HTML`, `VanillaJavaScript`
- Backend : `Python`,`Flask`, `SQLLite3`,`Natural Language ToolKit (NLTK)`, `GenSim`, `Rapid Automatic Keyword Extraction (RAKE)`,`tensorflow`,`sklearn`

## Challenges we ran into (Problems Faced)
- Creating a robust UI that was exactly similar to Google-Forms was an amazingly difficult task.
- Score Prediction Model Retraining was a Primary Scalability Concern.

## Accomplishments that we're proud of (Acheivements)
Here are some of the reviews that we received from the Teachers who tested the system initially :

> **SMART-Google-Forms**  provides the complete package for Grading Assesments and provides a hassle free Teaching Experience, I would definitely integrate this in my ClassRooms. - Dibakar RoyChoudhury, Professor, Department of Basic Science and Humanities, Institute of Engineering & Management, Kolkata.

> A very Accurate system that provides Excellent Predictions, this Tool is very useful for all Teaching Assistance. I recommend **SMART-Google-Forms** for better educational facilities. - Tamesh Halder, PhD Scholar, Department of Mining Engineering, Indian Institute Technology, Kharagpur.

## What we learned (Learning Outcomes)
- Advanced Natural Language Processing
- Web Application Scalability 
- Responsive System Design

# ML workflow:

<p align="center">
  <img width="1000" height="400" src="https://i.ibb.co/qkB1DQ2/Screenshot-1124.png">
</p>

The whole ML workflow is devided into two parts, one is ML/DL prediction and another is Similarity score estimation. Reason behind using ML into this is to capture the propper construction and the grammatical flow of sentences. And by using tf-idf based similarity score we get the contextual information from the given text. As its mentioned above that the the teacher will provide a sample answer and with respect to that we will be evaluating the answers of the students. Now, lets discuss both of the parts separately,

## ML/DL prediction:
we had 8.5k+ data points to train on, so data points were much lesser because of that LSTM model was performing poorly as val_loss was coming 56% in average. So we moved from DL to ML. In ML we ried with random forest, random forest with `RandomizedSearchCV` so by using that we got upto 60% accurecy although is not a good metric to follow incase of classification so we tried with kappa score too which was giving us ~0.92 kappa value which is really a good score.

## tf-idf based similarity score:
`TF-IDF approach`
1. Make a text corpus containing all words of documents . You have to use tokenisation and stop word removal . NLTK library provides all .
2. Convert the documents into tf-idf vectors .
3. Find the cosine-similarity between them or any new document for similarity measure.

## ML file structure:
All the files lies into the `ML area` folder.
1. [`LSTM_56_percent.ipynb`](https://github.com/khanfarhan10/SMART-GForms/blob/main/ML_area/LSTM_56_percent.ipynb) here LSTM model git trained with embedding layer.
2. [autograding-using-lstm-tf-keras_high_kappa.ipynb](https://github.com/khanfarhan10/SMART-GForms/blob/main/ML_area/autograding-using-lstm-tf-keras_high_kappa.ipynb) here lstm MODEL WAS TRAINED WITH 5 FOLD CV and normal word vectors.this is the file which shows the high kappa score.
3. [model building.ipynb](https://github.com/khanfarhan10/SMART-GForms/blob/main/ML_area/model%20building.ipynb) this file shows the training of random forest and random forest with `RandomizedSearchCV`. 
4. [similarity score estimation.ipynb](https://github.com/khanfarhan10/SMART-GForms/blob/main/ML_area/similarity%20score%20estimation.ipynb) this file gives the similarity score.
5. [get_final_score.py](https://github.com/khanfarhan10/SMART-GForms/blob/main/ML_area/get_final_score.py) implements the a simple average score out of all other models and the similarity score.

## What's next for SMART Google Forms (Future Prospectives)
- Google Forms API Integration for Open Access
- OAuth Login (Integrated with Google, GitHub etc)
- More Complex Neural Network Predictive Analysis
- Advanced Analytics for Project Results 

## The MLXTREME Team
`Team Machine Learning eXceptional Technological Resolutions Engineering and Managerial Enterprises`

- Soumydip Sarkar, Department of Electrical Engineering (3rd year), Institute of Engineering & Management, Kolkata, West Bengal, soumya997.sarkar@gmail.com.
- Nirmalya Misra, Department of Information Technology (2nd year), Institute of Engineering & Management, Kolkata, West Bengal, nirmalya14misra@gmail.com.
- Damik Dhar, Department of Information Technology (2nd year), Institute of Engineering & Management, Kolkata, West Bengal, damikdhar@gmail.com.
- Farhan Hai Khan, Department of Electrical Engineering (3rd year), Institute of Engineering & Management, Kolkata, West Bengal, njrfarhandasilva10@gmail.com.
