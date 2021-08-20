import unittest
from flask_login.mixins import UserMixin
from app.models import Comment,User,Pitch
from . import db

class TestClass(unittest.TestCase):
    
    def setUp(self):
        self.user=User(username='morara',email='isaiahmorara9@gmail.com',bio='Biography',img='path',password='isaiahmorara')
        self.pitch=Pitch(content='contente',likes=1,dislikes='dislikes',owner=UserMixin.username,category='Sales')
        self.comment=Comment(content='Content',parentid=Pitch.id,owner=UserMixin.username)
        
    def tearDown(self):
        User.session.delete()
        Pitch.session.delete()
        Comment.session.delete()
        
        
        
if __name__=='__main__':
    unittest.main()