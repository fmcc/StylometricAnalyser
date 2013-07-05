import numpy
import math

"""
This function will create the profile of a text from the ngram object of the text and the vector space. 
"""
def profile_text(text_ngram, vector_space):
    text_counts = text_ngram.ngram_counts()
    profile = [text_counts.get(ngram,0) for ngram in sorted(vector_space)]
    return profile 


def cosine_distance(profile_one, profile_two):
    return numpy.dot(profile_one,profile_two) / (math.sqrt(numpy.dot(profile_one,profile_one)) * (math.sqrt(numpy.dot(profile_two,profile_two))))

