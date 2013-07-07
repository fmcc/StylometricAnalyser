import numpy
import math

def cosine_distance(profile_one, profile_two):
    return numpy.dot(profile_one,profile_two) / (math.sqrt(numpy.dot(profile_one,profile_one)) * (math.sqrt(numpy.dot(profile_two,profile_two))))

