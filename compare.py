import numpy
import math
from generate import generate_profile, generate_limited_profile
from database import *
from database.models import *
from database.utilities import get_or_create
from settings import RESTRICT_VECTOR_SPACE

def cosine_distance(profile_one, profile_two):
    return numpy.dot(profile_one,profile_two) / (math.sqrt(numpy.dot(profile_one,profile_one)) * (math.sqrt(numpy.dot(profile_two,profile_two))))

def compare_texts(session, sec_one, sec_two):
    section_one, section_two = order_sections(sec_one.id, sec_two.id)
    comparison = get_or_create(session, Comparison, text_one=section_one,text_two=section_two)
    if comparison.cosine_similarity:
        print('Retrieving similarity')
        return comparison.cosine_similarity
    #vector = session.query(VectorSpace).first()
    #if comparison.profile_length and comparison.profile_length == len(vector.space):
    #    print('Using stored comparison')
    #    return comparison.cosine_similarity
    #profile_one = get_current_profile(session, vector, sec_one)
    #profile_two = get_current_profile(session, vector, sec_two)
    global_ngrams = session.query(GlobalNgrams).first()
    top_ngrams = global_ngrams.top_ngram_counts
    profile_one = get_current_limited_profile(session, top_ngrams, sec_one)
    profile_two = get_current_limited_profile(session, top_ngrams, sec_two)
    comparison.cosine_similarity = cosine_distance(profile_one, profile_two)
    comparison.profile_length = len(profile_one)
    session.commit()
    return comparison.cosine_similarity

def get_current_profile(session, vector, section):
    if section.profile: 
        if(len(vector.space) != len(section.profile)):
            print('Updating profile of ' + str(section.number))
            section.profile = generate_profile(section.ngrams, vector.space)
            session.commit()
            return section.profile
        else:
            return section.profile
    else:
        print('Creating profile of ' + str(section.number))
        section.profile = generate_profile(section.ngrams, vector.space)
        session.commit()
        return section.profile

def get_current_limited_profile(session, top_ngrams, section):
    if section.profile and len(section.profile) == RESTRICT_VECTOR_SPACE:
        print('Retrieving profile of ' + str(section.number))
        return section.profile
    else:
        print('Creating profile of ' + str(section.number))
        section.profile = generate_limited_profile(section.ngrams, top_ngrams)
        session.commit()
        return section.profile
