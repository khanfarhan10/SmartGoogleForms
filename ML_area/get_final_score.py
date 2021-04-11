
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
from similarity_score_estimation import get_similarity_score
from get_lstm_pred import get_lstm
from get_rf_pred import get_rf_result
from get_rf_rscv_pred import get_rf_rscv_result
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))




if __name__ == "__main__":


    ans1 = "AI is the understanding that machines can interpret, mine, and learn from external data in a way where said machines functionally imitate cognitive practices normally attributed to humans. Artificial intelligence is based on the notion that human thought processes have the ability to both be replicated and mechanized. The history of artificial intelligence dates back to antiquity with philosophers mulling over the idea that artificial beings, mechanical men, and other automatons had existed or could exist in some fashion. To know more about the history you can also visit Analytics Jobs as I got to know about the history of AI and the changes that are happening daily.Thanks to early thinkers, artificial intelligence became increasingly more tangible throughout the 1700s and beyond. Philosophers contemplated how human thinking could be artificially mechanized and manipulated by intelligent non-human machines. The thought processes that fuelled interest in AI originated when classical philosophers, mathematicians, and logicians considered the manipulation of symbols (mechanically), eventually leading to the invention of a programmable digital computer, the Atanasoff Berry Computer (ABC) in the 1940s. This specific invention inspired scientists to move forward with the idea of creating an “electronic brain,” or an artificially intelligent being.In 1955 a leading computer expert, John McCarthy, wrote a proposal to hold a two-month workshop with top computer scientists. The goal was to enable computers to simulate the basics of human intelligence. They sincerely thought that two months would be plenty of time to address all aspects of the problem and start a new era of human intelligence in a machine.Obviously they didn’t succeed, but the event launched the first period of intense AI research. It led to many highly useful developments, but putting the basics of human intelligence into a computer proved to be far more difficult than anyone imagined. After sixty-four years we’re barely able to reproduce the simplest biological intelligence, let alone anything approaching human level. The top researchers currently say that even a primitive artificial general intelligence is a long way off and it’s unknown how it would ever compare to human intelligence."


    ans2 = 'McCarthy invented Artificial Intelligence.The term artificial intelligence was first coined by John McCarthy in 1956 when he held the first academic conference on the subject. But the journey to understand if machines can truly think began much before that. Introduction of AI: Logic was introduced into AI research as early as 1958, by John McCarthy in his Advice Taker proposal. In 1963, J. Alan Robinson had discovered a simple method to implement deduction on computers, the resolution and unification algorithm.He created the term "artificial intelligence" and , was a towering figure in computer science at the Stanford University , most of his professional life. In his career, he developed the programming language LISP, played computer chess via telegraph with opponents in Russia and invented computer time-sharing.In proposing the first conference on Artificial Intelligence, McCarthy wrote, "The study is to proceed on the basis of the conjecture that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it." The subsequent conference is considered a watershed moment in computer science. In late 20th century, McCarthy invented the computer programming language LISP, the second oldest programming language after FORTRAN. LISP is still used today and is the programming language of choice for artificial intelligence.'


#     model_path1 = "./models/rf-0.607.pkl"
    model_path = "./models/rf-0.5215.pkl"

    # say ans2= answer provided by student ans1=answer provided by teacher
    sim= get_similarity_score(ans1,ans2)
#     rf_rscv = get_rf_rscv_result(ans2,model_path1)
    rf = get_rf_result(ans2,model_path)
    lstm = get_lstm(ans2)

    total_score = (sim+rf_rscv+rf+lstm)/4
    print(total_score)