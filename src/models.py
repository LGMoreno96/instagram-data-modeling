import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    username = Column(String(16), nullable = False)
    email = Column(String(64), nullable = False)
    biography = Column (String(128), nullable = True)
    location = Column (String(256), nullable = True)
    post = relationship('Post', backref='user')
    reel = relationship('Reel', backref='user')
    igtv = relationship('Igtv', backref='user')
    story = relationship('Story', backref='user')
    post_like = relationship('PostLike', backref='user')
    reel_like = relationship('ReelLike', backref='user')
    igtv_like = relationship('IgtvLike', backref='user')
    post_comment = relationship('PostComment', backref='user')
    reel_comment = relationship('ReelComment', backref='user')
    igtv_comment = relationship('IgtvComment', backref='user')
    story_comment = relationship('StoryComment', backref='user')
    story_reaction = relationship('StoryReaction', backref='user')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    photo = Column(String(128), nullable = True)
    video = Column(String(128), nullable = True)
    location = Column(String(128), nullable = True)
    caption = Column(String(256), nullable = True)

class PostLike(Base):
    __tablename__ = 'post_like'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("Post")

class Reel(Base):
    __tablename__ = 'reel'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    video = Column(String(128), nullable = False)
    effect = Column(String(16), nullable = True)
    song = Column(String(64), nullable = True)

class ReelLike(Base):
    __tablename__ = 'reel_like'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    reel_id = Column(Integer, ForeignKey('reel.id'))
    reel = relationship("Reel")

class ReelComment(Base):
    __tablename__ = 'reel_comment'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    reel_id = Column(Integer, ForeignKey('reel.id'))
    reel = relationship("Reel")

class Story(Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    photo = Column(String(128), nullable = True)
    video = Column(String(128), nullable = True)
    effect = Column(String(128), nullable = True)
    text = Column(String(128), nullable = True)
    song = Column(String(64), nullable = True)


class StoryComment(Base):
    __tablename__ = 'story_comment'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    story_id = Column(Integer, ForeignKey('story.id'))
    story = relationship("Story")

class StoryReaction(Base):
    __tablename__ = 'story_reaction'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    story_id = Column(Integer, ForeignKey('story.id'))
    story = relationship("Story")

class Igtv(Base):
    __tablename__ = 'igtv'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    video = Column(String(128), nullable = False)
    location = Column(String(128), nullable = True)
    caption = Column(String(256), nullable = True)

class IgtvLike(Base):
    __tablename__ = 'igtv_like'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    igtv_id = Column(Integer, ForeignKey('igtv.id'))
    igtv = relationship("Igtv")

class PostComment(Base):
    __tablename__ = 'post_comment'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("Post")    

class IgtvComment(Base):
    __tablename__ = 'igtv_comment'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    igtv_id = Column(Integer, ForeignKey('igtv.id'))
    igtv = relationship("Igtv")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e