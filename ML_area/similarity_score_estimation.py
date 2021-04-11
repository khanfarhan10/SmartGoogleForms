# imports
import gensim
import nltk
import numpy as np
from nltk.tokenize import word_tokenize, sent_tokenize

"""
provide only the answer of the teacher and the answer of the student, and it 
will give you the similarity score from 1 to 10

"""
def get_similarity_score(ans1,ans2):
    file_docs = []
    file2_docs = []
    avg_sims = []
    # ans1 processing and conversion in a tfidf vector
    tokens = sent_tokenize(ans1)
    for line in tokens:
        file_docs.append(line)

    length_doc1 = len(file_docs)

    gen_docs = [[w.lower() for w in word_tokenize(text)] 
                for text in file_docs]

    dictionary = gensim.corpora.Dictionary(gen_docs)
    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
    tf_idf = gensim.models.TfidfModel(corpus)
    #provide the path of this script by changing './corpus'
    sims = gensim.similarities.Similarity('./corpus',tf_idf[corpus],
                                        num_features=len(dictionary))

    # tokenizing students's ans
    tokens = sent_tokenize(ans2)
    for line in tokens:
        file2_docs.append(line)
    # estimating Similarity value 
    for line in file2_docs:
        query_doc = [w.lower() for w in word_tokenize(line)]
        query_doc_bow = dictionary.doc2bow(query_doc)
        query_doc_tf_idf = tf_idf[query_doc_bow] 
        sum_of_sims =(np.sum(sims[query_doc_tf_idf], dtype=np.float32))
        avg = sum_of_sims / len(file_docs)
        avg_sims.append(avg)  
    # rounding up the similarity value
    total_avg = np.sum(avg_sims, dtype=np.float)
    percentage_of_similarity = round(float(total_avg) * 100)
    if percentage_of_similarity >= 100:
        percentage_of_similarity = 100

    #provides 6 if the similarity score lies in 60s
    return round(percentage_of_similarity/10)


if __name__ == "__main__":
    ans1 = "AI is the understanding that machines can interpret, mine, and learn from external data in a way where said machines functionally imitate cognitive practices normally attributed to humans. Artificial intelligence is based on the notion that human thought processes have the ability to both be replicated and mechanized. The history of artificial intelligence dates back to antiquity with philosophers mulling over the idea that artificial beings, mechanical men, and other automatons had existed or could exist in some fashion. To know more about the history you can also visit Analytics Jobs as I got to know about the history of AI and the changes that are happening daily.Thanks to early thinkers, artificial intelligence became increasingly more tangible throughout the 1700s and beyond. Philosophers contemplated how human thinking could be artificially mechanized and manipulated by intelligent non-human machines. The thought processes that fuelled interest in AI originated when classical philosophers, mathematicians, and logicians considered the manipulation of symbols (mechanically), eventually leading to the invention of a programmable digital computer, the Atanasoff Berry Computer (ABC) in the 1940s. This specific invention inspired scientists to move forward with the idea of creating an “electronic brain,” or an artificially intelligent being.In 1955 a leading computer expert, John McCarthy, wrote a proposal to hold a two-month workshop with top computer scientists. The goal was to enable computers to simulate the basics of human intelligence. They sincerely thought that two months would be plenty of time to address all aspects of the problem and start a new era of human intelligence in a machine.Obviously they didn’t succeed, but the event launched the first period of intense AI research. It led to many highly useful developments, but putting the basics of human intelligence into a computer proved to be far more difficult than anyone imagined. After sixty-four years we’re barely able to reproduce the simplest biological intelligence, let alone anything approaching human level. The top researchers currently say that even a primitive artificial general intelligence is a long way off and it’s unknown how it would ever compare to human intelligence."
    ans2 = 'McCarthy invented Artificial Intelligence.The term artificial intelligence was first coined by John McCarthy in 1956 when he held the first academic conference on the subject. But the journey to understand if machines can truly think began much before that. Introduction of AI: Logic was introduced into AI research as early as 1958, by John McCarthy in his Advice Taker proposal. In 1963, J. Alan Robinson had discovered a simple method to implement deduction on computers, the resolution and unification algorithm.He created the term "artificial intelligence" and , was a towering figure in computer science at the Stanford University , most of his professional life. In his career, he developed the programming language LISP, played computer chess via telegraph with opponents in Russia and invented computer time-sharing.In proposing the first conference on Artificial Intelligence, McCarthy wrote, "The study is to proceed on the basis of the conjecture that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it." The subsequent conference is considered a watershed moment in computer science. In late 20th century, McCarthy invented the computer programming language LISP, the second oldest programming language after FORTRAN. LISP is still used today and is the programming language of choice for artificial intelligence.'
    
    sim_score = get_similarity_score(ans1,ans2)