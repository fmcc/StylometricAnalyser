from sqlalchemy import *
from database import Base
from database.utilities import order_sections

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, Sequence('author_id_seq'), primary_key=True)
    name = Column(Unicode)
    def __init__(self, name):
        self.name = name

class Text(Base):
    __tablename__ = 'text'
    id = Column(Integer, Sequence('text_id_seq'), primary_key=True)
    author = Column(Integer, ForeignKey('author.id'))
    name = Column(Unicode)
    def __init__(self, name, author):
        self.name = name
        self.author = author

class Section(Base):
    __tablename__ = 'section'
    id = Column(Integer, Sequence('section_id_seq'), primary_key=True)
    number = Column(Integer)
    source_text = Column(Integer, ForeignKey('text.id'))
    content = Column(UnicodeText)
    ngrams = Column(PickleType, nullable=True)
    profile = Column(PickleType, nullable=True)
    def __init__(self, source_text, number, content):
        self.number = number
        self.content = content
        self.source_text = source_text

class Comparison(Base):
    __tablename__ = 'comparison'
    id = Column(Integer, Sequence('comparison_id_seq'), primary_key=True)
    text_one = Column(Integer, ForeignKey('section.id'))
    text_two = Column(Integer, ForeignKey('section.id'))
    cosine_similarity = Column(Float, nullable=True)
    profile_length = Column(Integer, nullable=True)
    def __init__(self, text_one, text_two):
        self.text_one, self.text_two = order_sections(text_one, text_two)

class VectorSpace(Base):
    __tablename__ = 'vector_space'
    id = Column(Integer, Sequence('vector_space_id_seq'), primary_key=True)
    space = Column(PickleType, nullable=True)
    def __init__(self, space):
        self.space = space

class GlobalNgrams(Base):
    __tablename__ = 'global_ngrams'
    id = Column(Integer, Sequence('global_ngrams_id_seq'), primary_key=True)
    global_ngram_counts = Column(PickleType, nullable=True)
    top_ngram_counts = Column(PickleType, nullable=True)
    def __init(self, global_ngram_counts, top_ngram_counts):
        self.global_ngram_counts = global_ngram_counts
        self.top_ngram_counts = top_ngram_counts
