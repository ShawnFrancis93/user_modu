from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.users import User

@app.route('/')
def index():
    return render_template("dashboard.html")

@app.route("/add_user")
def add_friend(): 
    
    return render_template("create.html")


@app.route("/create_user", methods =["POST"])
def add_user():
    User.save(request.form)
    return redirect("/show/{id}")

@app.route("/show/<id>")
def show(id): 
    data = {
        'id': (id)
    }
    return render_template("show.html", user = User.get_by_id(data))

@app.route("/edit/<id>")
def edit(id): 
    data = {
        "id" : int(id)
    }
    return render_template("edit.html", user = User.get_by_id(data))

@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    data = {
        "id" : id,
        "first_name" : request.form ['fname'],
        "last_name" : request.form ['lname'],
        "email" : request.form ['email'],
        
    }
    User.update(data)
    return redirect(f"/show/{id}")

@app.route("/delete/<int:id>")
def delete(id):
    data = {
        "id": id,
    }
    User.destroy(data)
    return redirect(f"/users")