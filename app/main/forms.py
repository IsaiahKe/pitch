from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,TextField
from wtforms.validators import Required
class ProfileUpdate(FlaskForm):
    bio =TextAreaField(label="Bio Data",validators=[Required()])
    
    save=SubmitField('Save')
    
class PitchForm(FlaskForm):
    category=TextField(label="Category",validators=[Required()])
    content=TextAreaField(label='Pitch',validators=[Required()])
    submit=SubmitField('Post')
    
    
class CommentForm(FlaskForm):
    comment=TextAreaField("Comment",validators=[Required()])
    submit=SubmitField('Send')