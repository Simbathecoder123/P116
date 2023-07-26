# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "My name is Bhargava" # write your name
    age = "I am 14 years old" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():

    name= "Veera"
    age = 53
# define the route to mother webpage
@app.route("/mother")
def father():

    name= "Kavitha"
    age = 43

# define the route to friends webpage
@app.route("/friends")
def father():

    name= "A lot"
    age = 14

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
