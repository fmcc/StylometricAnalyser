import numpy
import math
from generate import generate_profile
from database import *
from database.models import *
from database.utilities import get_or_create, order_sections
from log import log
from settings import RESTRICT_VECTOR_SPACE

def cosine_distance(profile_one, profile_two):
    return numpy.dot(profile_one,profile_two) / (math.sqrt(numpy.dot(profile_one,profile_one)) * (math.sqrt(numpy.dot(profile_two,profile_two))))

def compare_texts(session, sec_one, sec_two):
    section_one, section_two = order_sections(sec_one.id, sec_two.id)
    comparison = get_or_create(session, Comparison, text_one=section_one,text_two=section_two)
    version = session.query(GlobalVersion).first()
    if comparison.version and  comparison.version == version.version:
        log('Retrieving stored comparison.')
        return comparison.cosine_similarity
    log('Generating comparison.')
    vector_space = session.query(VectorSpace).first()
    profile_one = get_current_profile(session, version.version, vector_space, section_one)
    profile_two = get_current_profile(session, version.version, vector_space, section_two)
    comparison.cosine_similarity = cosine_distance(profile_one, profile_two)
    comparison.version = version.version
    session.commit()
    return comparison.cosine_similarity

def get_current_profile(session, version, vector, sect):
    profile = get_or_create(session, SectionProfile, section=sect)

    def get_profile():
        ngrams = session.query(SectionNgrams).filter_by(section=sect).first()
        profile.profile = generate_profile(ngrams.ngrams, vector.space)
        profile.version = version
        session.commit()
        return profile.profile

    if profile.profile:
        if profile.version == version:
            log('Retrieving profile.')
            return profile.profile
        else:
            log('Updating profile.')
            return get_profile()
    else:
        log('Creating profile.')
        return get_profile()
