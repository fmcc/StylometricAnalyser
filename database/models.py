from sqlalchemy import *
from database import Base

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
