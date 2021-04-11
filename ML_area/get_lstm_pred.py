from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Dense
import numpy as np                                  #for large and multi-dimensional arrays
import pandas as pd                                 #for data manipulation and analysis
import nltk                                         #Natural language processing tool-kit
import re
from nltk.corpus import stopwords                   #Stopwords corpus
from nltk.stem import PorterStemmer     

import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import MultinomialNB

import warnings
warnings.filterwarnings("ignore")                     #Ignoring unnecessory warnings

import numpy as np                                  #for large and multi-dimensional arrays
import pandas as pd                                 #for data manipulation and analysis
import nltk                                         #Natural language processing tool-kit

from nltk.corpus import stopwords                   #Stopwords corpus
from nltk.stem import PorterStemmer                 # Stemmer

from sklearn.feature_extraction.text import CountVectorizer          #For Bag of words
from sklearn.feature_extraction.text import TfidfVectorizer          #For TF-IDF
from sklearn.ensemble import RandomForestClassifier                  # for rf
from gensim.models import Word2Vec                                   #For Word2Vec

from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Dense
from keras.layers import SpatialDropout1D
import re
import pickle






## Creating model
embedding_vector_features=400
voc_size=5000
sent_length=400
model=Sequential()
model.add(Embedding(voc_size,embedding_vector_features,input_length=sent_length))
model.add(Dropout(0.3))
model.add(LSTM(100))
model.add(Dropout(0.3))
model.add(Dense(10,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
# print(model.summary())


model.load_weights("./models/final_lstm-0.56.h5")


def get_lstm(test):
    snow = nltk.stem.SnowballStemmer('english')

    corpus_test = []
    # for i in range(0, len(df)):
    review = re.sub('[^a-zA-Z]', ' ', test)
    review = review.lower()
    review = review.split()

    review = [snow.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus_test.append(review)

    voc_size=5000
    onehot_repr=[one_hot(words,voc_size)for words in corpus_test] 

    sent_length=400
    embedded_docs=pad_sequences(onehot_repr,padding='pre',maxlen=sent_length)

    y_pred_lstm = model.predict_classes(embedded_docs)
    return int(y_pred_lstm)
#     return int(y_pred_lstm)

if __name__ == "__main__":
    test = 'last updat st june debarghya das debarghyada com fb co dd deedi fb com dd cornel edu educ cornel univers meng comput scienc dec ithaca ny cornel univers bs comput scienc may ithaca ny colleg engin magna cum laud cum gpa major gpa la martinier boy grad may kolkata india link facebook dd github deedyda linkedin debarghyada youtub deedydash twitter debarghya das quora debarghya das coursework graduat advanc machin learn open sourc softwar engin advanc interact graphic compil practicum cloud comput evolutionari comput defend comput network machin learn undergradu inform retriev oper system artifici intellig practicum function program comput graphic practicum research asst teach asst x unix tool script skill program line java shell python javascript ocaml matlab rail latex line c c css php assembl familiar io android mysql experi facebook softwar engin jan present new york ny coursera kpcb fellow softwar engin intern june sep mountain view ca applic chosen kpcb fellow led ship yoda admin interfac new phoenix platform full stack develop wrote review code js use backbon jade stylus requir scala use play googl softwar engin intern may aug mountain view ca work youtub caption team javascript python plan design develop full stack add edit automat speech recognit caption product creat backbon js like framework caption editor phabric open sourc contributor team leader jan may palo alto ca ithaca ny phabric use daili facebook dropbox quora asana creat meme generat php shell led team mit cornel ic london uhelsinki project research cornel robot learn lab research jan jan ithaca ny work ashesh jain prof ashutosh saxena creat planit tool learn larg scale user prefer feedback plan robot trajectori human environ cornel phonet lab head undergradu research mar may ithaca ny led develop quicktongu first ever breakthrough tongu control game prof sam tilsen aid linguist research award top kpcb engin fellow st microsoft code competit cornel nation jump trade challeng finalist th cs cach race bot tournament nd cs biannual intra class bot tournament nation indian nation mathemat olympiad inmo finalist public jain das saxena planit crowdsourc approach learn plan path larg scale prefer feedback tech report icra press tilsen das b mckee real time articulatori biofeedback electromagnet articulographi linguist vanguard press'
    
    get_lstm(test)