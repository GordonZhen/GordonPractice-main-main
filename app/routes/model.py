
from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Blog, Comment, Model
from app.classes.forms import BlogForm, CommentForm, ModelForm
from flask_login import login_required
import datetime as dt

@app.route('/model/list')
@app.route('/models')

@login_required
def modelList():
    models = Model.objects()
    
    return render_template('models.html',models= models)

@app.route('/model/<modelID>')
@login_required

def model(modelID):
    thisModel = Model.objects.get(id=modelID)
    return render_template('models.html',model=thisModel)

@app.route('/model/delete/<modelID>')
@login_required

def modelDelete(modelID):
    deleteModel = Model.objects.get(id=modelID)
    if current_user == deleteModel.author:
        deleteModel.delete()

        flash('The Model was deleted.')
    else: 
        flash("You can't delete a model you don't own.")
    models = Model.objects()  

    return render_template('models.html',models=models)

@app.route('/model/new', methods=['GET', 'POST'])
@login_required

def modelNew():
    form = ModelForm()

    if form.validate_on_submit():
        newModel = Model(
            title = form.title.data,
            file = form.file.data,
            fileSize = form.fileSize.data,
            # thumbnail = form.thumbnail.data,
            fileType = form.fileType.data,

        )
        if form.thumbnail.data:
            newModel.thumbnail.put(form.thumbnail.data, content_type = 'image/jpeg')
            newModel.save()
     
        newModel.save()
        

        return redirect(url_for('model',modelID=newModel.id))
    
    return render_template('modelform.html',form=form) 

@app.route('/model/edit/<modelID>', methods=['GET', 'POST'])
@login_required

def modelEdit(modelID):
    editModel = Model.objects.get(id=modelID)

    if current_user != editModel.author: 
        flash("You can't edit a model you don't own.")
        return redirect(url_for('model',modelID=modelID))

    form = ModelForm()
 
    if form.validate_on_submit():

        editModel.update(
            title = form.title.data,
            file = form.file.data,
            fileSize = form.fileSize.data,
            # thumbnail = form.thumbnail.data,
            fileType = form.fileType.data,

        )
        if editModel.thumbnail:
               editModel.thumbnail.delete()
               editModel.thumbnail.put(form.thumbnail.data, content_type = 'image/jpeg')
        editModel.save()

        return redirect(url_for('model',modelID=modelID))
    
    form.title.data = editModel.title
    form.file.data = editModel.file
    form.fileSize.data = editModel.fileSize
    form.thumbnail.data = editModel.thumbnail
    form.fileType.data = editModel.fileType

    return render_template('modelform.html',form=form)






