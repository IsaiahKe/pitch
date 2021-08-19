from flask import render_template,redirect,url_for,abort
from flask_login import login_required
from . import main
from .forms import CommentForm, PitchForm
from ..models import Pitch, User,Comment
from .. import db
from flask_login import current_user

@main.route('/')
def index():
    
    title="Home"
    items=Pitch.query.order_by(Pitch.posted).all()

    return render_template('index.html',title=title,items=items)

@main.route('/profile/<accountname>')
@login_required
def profile(accountname):
    user=User.query.filter_by(username=accountname).first()
    
    if user is None:
        abort(404)


    return render_template('auth/profile.html', user=user)
@main.route('/newpitch',methods=['POST','GET'])
@login_required
def newpitch():
    form= PitchForm()
    current_user
    if form.validate_on_submit():
        category=form.category.data
        content= form.content.data
        owner=current_user.username
        newpitch= Pitch(category=category,content=content,likes=0,dislikes=0,owner=owner)
        newpitch.save()
        db.session.add(newpitch)
        db.session.commit() 
        redirect(url_for('main.index'))
    
    return render_template('newpitch.html',form=form)

@main.route('/<pitchid>/comment',methods=['POST','GET'])
@login_required
def comment(pitchid):
    item=Comment.query.filter_by(parentid=pitchid).all()
    form=CommentForm()
    if form.validate_on_submit():
        pitch=Pitch.query.filter_by(id=pitchid)
        if pitch:
            usercomment=form.comment.data
            user=current_user.username
            parentid=pitchid
            feedback= Comment(content=usercomment,owner=user,parentid=parentid)
            feedback.save()
            
    return render_template('comment.html',form=form,item=item)
@main.route('/<pid>/upvote')
@login_required
def uvote(pid):
    pitch=Pitch.query.filter_by(id=pid).first()
    title="Home"
    items=Pitch.query.order_by(Pitch.posted).all()

    
    pitch.likes=pitch.likes+1
    print(pitch.likes)
    db.session.commit()
    redirect(url_for('main.index'))
    return render_template('index.html',title=title,items=items)
        
@main.route('/<pid>/downvote')
@login_required
def dvote(pid):
    pitch=Pitch.query.filter_by(id=pid).first()
    title="Home"
    items=Pitch.query.order_by(Pitch.posted).all()

    
    pitch.dislikes=pitch.dislikes+1
    
    db.session.commit()
    redirect(url_for('main.index'))
    return render_template('index.html',title=title,items=items)  
    