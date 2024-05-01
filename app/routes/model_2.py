# from app import app
# import mongoengine.errors
# from flask import render_template, flash, redirect, url_for
# from flask_login import current_user
# from app.classes.data import Blog, Comment, Model
# from app.classes.forms import BlogForm, CommentForm, ModelForm
# from flask_login import login_required
# import datetime as dt

# @app.route('/model/list')
# @app.route('/models')

# @login_required
# def modelList():
#     models = Model.objects()
    
#     return render_template('models.html',models= models)

# @app.route('/model/<modelID>')
# @login_required

# def model(modelID):
#     thisModel = Model.objects.get(id=modelID)
#     return render_template('models.html',model=thisModel)

# @app.route('/model/delete/<modelID>')
# @login_required

# def modelDelete(modelID):
#     deleteModel = Model.objects.get(id=modelID)
#     if current_user == deleteModel.author:
#         deleteModel.delete()

#         flash('The Model was deleted.')
#     else: 
#         flash("You can't delete a model you don't own.")
#     models = Model.objects()  

#     return render_template('models.html',models=models)

# @app.route('/model/new', methods=['GET', 'POST'])
# @login_required

# def modelNew():
#     form = ModelForm()

#     if form.validate_on_submit():
#         newModel = Model(
#             title = form.title.data,
#             file = form.file.data,
#             fileSize = form.fileSize.data,
#             fileType = form.fileType.data,

#         )
#         newModel.save()
        

#         return redirect(url_for('model',modelID=newModel.id))
    
#     return render_template('modelform.html',form=form) 

# @app.route('/model/edit/<modelID>', methods=['GET', 'POST'])
# @login_required

# def modelEdit(modelID):
#     editModel = Model.objects.get(id=modelID)

#     if current_user != editModel.author: 
#         flash("You can't edit a model you don't own.")
#         return redirect(url_for('model',modelID=modelID))

#     form = ModelForm()
 
#     if form.validate_on_submit():

#         editModel.update(
#             title = form.title.data,
#             fileSize = form.fileSize.data,
#             fileType = form.fileType.data,

#         )

#         return redirect(url_for('model',modelID=modelID))
    
#     form.title.data = editModel.title
#     form.fileSize.data = editModel.fileSize
#     form.fileType.data = editModel.fileType

#     return render_template('modelform.html',form=form)






