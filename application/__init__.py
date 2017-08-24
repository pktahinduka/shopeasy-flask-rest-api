from flask import Flask
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

from .import views

### @petertahinduka ######

### This file fires up the ShopEasy Application ###

#from flask_login import LoginManager
#from user import User
from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('shopeasy_index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signin.html')


@app.route('/showHome')
def showHome():
    return render_template('home.html')


        
if __name__ == "__main__":
    app.run()
