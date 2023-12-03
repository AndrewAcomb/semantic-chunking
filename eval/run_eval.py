"""
    Uses AutoEvals to run evals
    https://github.com/braintrustdata/autoevals
"""
# from autoevals.llm import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Create a new LLM-based evaluator
# evaluator = Factuality()


class Eval:
    def __init__(self) -> None:
        pass

    # def run_eval(self, input, output, expected):
    #     result = evaluator(output, expected, input)
    #     return result
    
    def cosine_simililarity_between_two_texts(self, text1, text2):
        # Init tfidf vectorizer
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([text1, text2])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        return similarity[0][0]
        

