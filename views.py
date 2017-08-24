""" This module contains all the view functions for the itemsListlist app"""
import re
from functools import wraps
from . import app
from flask import render_template, session, flash, redirect, url_for, request
from .models.user import User

USERS = {}

def register(name, username, password, rpt_password):
    """ This function handles user registration"""
    if name and username and password and rpt_password:
        if name.strip() and username.strip() and password.strip() and rpt_password.strip():
            if len(username) > 3 and len(username) < 11:
                if re.match("^[a-zA-Z0-9_.-]+$", username):
                    if len(password) > 5 and len(password) < 11:
                        if password == rpt_password:
                            USERS[username] = User(name, username, password)
                            return "Registration successful"
                        return "Passwords don't match"
                    return "Password should be 6 to 10 characters"
                return "Illegal characters in username"
            return "Username should be 4 to 10 characters"
        return "Blank input"
    return "None input"

def login(username, password):
    """ Handles user login """
    if username and password:
        if username.strip() and password.strip():
            if USERS.get(username):
                if USERS[username].password == password:
                    return "Login successful"
                return "Wrong password"
            return "User not found"
        return "Blank input"
    return "None input"


@app.route('/')
def index():
    """ Handles the index route """
    if session.get('username'):
        return redirect(url_for('read_itemsList'))
    else:
        return redirect(url_for('sign_in'))

@app.route('/sign_in', methods=['GET','POST'])
def sign_in():
    """ Handles the sign_in route """
    if request.method == 'POST':
        result = login(request.form['username'], request.form['password'])
        if result == "Login successful":
            session['username'] = request.form['username']
            return redirect(url_for('read_itemsList'))
        flash(result, 'warning')
    return render_template('login.html')

@app.route('/sign_up', methods=['GET','POST'])
def sign_up():
    """ Handles the sign_up route """
    if request.method == 'POST':
        result = register(request.form['name'], request.form['username'], request.form['password']
                          , request.form['rpt_password'])
        if result == "Registration successful":
            flash(result, 'info')
            return redirect(url_for('sign_in'))
        flash(result, 'warning')
    return render_template('register.html')

def login_required(func):
    """ Decorator function to ensure some routes are only accessed by logged in users """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        """ Modified descriprition of the decorated function """
        if not session.get('username'):
            flash('Login to continue', 'warning')
            return redirect(url_for('sign_in', next=request.url))
        return func(*args, **kwargs)
    return decorated_function

@app.route('/read_itemsList', methods=['GET', 'POST'])
@login_required
def read_itemsList():
    """ Handles displaying itemsList """
    return render_template('itemsList/read.html', itemsLists=USERS[session['username']].itemsList)

@app.route('/create_itemsList', methods=['GET', 'POST'])
@login_required
def create_itemsList():
    """ Handles new itemsList creation requests """
    if request.method == 'POST':
        result = USERS[session['username']].add_ItemsList(request.form['title'])
        if result == 'ItemsList added':
            flash(result, 'info')
        else:
            flash(result, 'warning')
        return redirect(url_for('read_itemsList'))
    return render_template('itemsList/create.html')

@app.route('/update_itemsList/<title>', methods=['GET', 'POST'])
@login_required
def update_itemsList(title):
    """ Handles request to update a itemsList """
    session['itemsList_title'] = title
    if request.method == 'POST':
        result = USERS[session['username']].update_itemsList(session['itemsList_title'],
                                                          request.form['title'])
        if result == 'ItemsList updated':
            flash(result, 'info')
        else:
            flash(result, 'warning')
        return redirect(url_for('read_itemsList'))
    return render_template('itemsList/update.html')

@app.route('/delete_itemsList/<title>',methods=['GET', 'POST'])
@login_required
def delete_itemsList(title):
    """ Handles request to delete a itemsList """
    result = USERS[session['username']].delete_itemsList(title)
    if result == 'ItemsList deleted':
        flash(result, 'info')
    else:
        flash(result, 'warning')
    return redirect(url_for('read_itemsList'))

@app.route('/read_items/<itemsList_title>', methods=['GET', 'POST'])
@login_required
def read_items(itemsList_title):
    """ Handles displaying items """
    session['current_itemsList_title'] = itemsList_title
    return render_template('items/read.html', items=USERS[session['username']]
                           .itemsList[itemsList_title].items)

@app.route('/create_item',methods=['GET', 'POST'])
@login_required
def create_item():
    """ Handles new item creation requests """
    if request.method == 'POST':
        result = USERS[session['username']].itemsList[session['current_itemsList_title']].add_item(
            request.form['description'])
        if result == 'Item added':
            flash(result, 'info')
        else:
            flash(result, 'warning')
        return redirect(url_for('read_items', itemsList_title=session['current_itemsList_title']))
    return render_template('items/create.html', items=USERS[session['username']]
                           .itemsList[session['current_itemsList_title']].items)

@app.route('/update_item/<description>',methods=['GET', 'POST'])
@login_required
def update_item(description):
    """ Handles request to update an item """
    session['description'] = description
    if request.method == 'POST':
        des_result = (USERS[session['username']].itemsList[session['current_itemsList_title']].
                      update_description(session['description'], request.form['description']))
        status_result = (USERS[session['username']].itemsList[session['current_itemsList_title']].
                         update_status(session['description'], request.form['status']))
        if des_result == 'Item updated' or status_result == 'Item updated':
            flash('Item updated', 'info')
        else:
            flash(des_result, 'warning')
        return redirect(url_for('read_items', itemsList_title=session['current_itemsList_title']))
    return render_template('items/update.html', item=USERS[session['username']]
                           .itemsList[session['current_itemsList_title']].items[description],
                           items=USERS[session['username']].
                           itemsList[session['current_itemsList_title']].items)

@app.route('/delete_item/<description>',methods=['GET', 'POST'])
@login_required
def delete_item(description):
    """ Handles request to delete an item """
    result = USERS[session['username']].itemsList[session['current_itemsList_title']].delete_item(
        description)
    if result == 'Item deleted':
        flash(result, 'info')
    else:
        flash(result, 'warning')
    return redirect(url_for('read_items', itemsList_title=session['current_itemsList_title']))

@app.route('/logout')
@login_required
def logout():
    """ logs out users """
    session.pop('username')
    flash('You have logged out', 'warning')
    return redirect(url_for('index'))
