# stores all url endpoints (front end)
# from crypt import methods
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json 


views = Blueprint('views', __name__)


@views.route('/', methods=['GET','POST'])

@login_required

def home():

    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash(' Your text is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note) 
            db.session.commit() 
            flash('Added note successfully!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])  

def delete_note():

    note = json.loads(request.data) # takes in data from a post request 
    noteId = note['noteId'] # now gets loaded into aa python object / now lets access the note id arg from the js file within the jsonify method 
    note = Note.query.get(noteId) # now lets look foe the note that has that id 
    
    if note: # if note exists...
        if note.user_id == current_user.id: # security check : if the exact user owns this note...
           db.session.delete(note) # then we'll delete the note 
           db.session.commit() # now save 

    return jsonify({}) # then we return an empty response 