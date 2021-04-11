"""
python RAKEEngine.py

Rake - Keyword Extraction
Word2Vec

getRAKEScore Implementation
"""

from rake_nltk import Rake

def get_keywords(text):
    r = Rake() 
    keywords = r.extract_keywords_from_text(text)
    phrases = r.get_ranked_phrases() # To get keyword phrases ranked highest to lowest.
    return keywords,phrases

def getRAKEScore(orig_text,each_ans,each_scores):
    """
    Use params to return a score
    Answer1 : orig_text - Student
    Answer2 : each_ans - Teacher
    Score :   each_ans : Score
    """
    
    
    
    return 0

if __name__ == "__main__":
    """# Uses stopwords for english from NLTK, and all puntuation characters."""

    text ="""
    Two roads diverged in a yellow wood,
    And sorry I could not travel both
    And be one traveler, long I stood
    And looked down one as far as I could
    To where it bent in the undergrowth;"""

    keywords,phrases = get_keywords(text)
    print(keywords,phrases)