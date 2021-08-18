from flask.globals import session
from sqlalchemy.orm import backref
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__="users"
    
    id= db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255),index=True)
    email= db.Column(db.String(50),unique=True,index=True)
    bio=db.Column(db.String(255))
    img=db.Column(db.String(255))
    securepassword= db.Column(db.String(200),index=True)
    @property
    def password(self):
        raise AttributeError ("password encrypted!")
    
    @password.setter
    def password(self,password):
        self.securepassword= generate_password_hash(password)
        
    def passwordVerification(self,password):
        return check_password_hash(self.securepassword,password)
    @login_manager.user_loader
    def loader_user(user_id):
        return User.query.get(int(user_id))
    def __repr__(self):
        return f'User{self.username}'
    
class Pitch(db.Model):
    __tablename__="pitches"
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(255))
    likes=db.Column(db.Integer)
    posted=db.Column(db.DateTime,default=datetime.now)
    dislikes=db.Column(db.Integer)
    owner=db.Column(db.String(50))
    category=db.Column(db.String(50))
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self):
        return f'Pitch{self.content}'
class Comment(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(255), index=True)
    parentid=db.Column(db.Integer,db.ForeignKey('pitches.id'))
    owner=db.Column(db.String(50))
    def save(self):
        db.session.add(self)
        db.session.commit()
    def __repr__(self):
        return f'Comment{self.content}'
    