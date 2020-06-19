

from flask import Flask
#as if importing df class from pandas
app = Flask(__name__)

# route: a URL path to visit
# route function names should be unique hello_world() vs about()

@app.route("/")
#@ = decorator, supercharges functionality of certain functions
#in flask defines a new route in our application, what should happen when we view a certain URL path
def hello_world():
    print("VISITED THE HELLO PAGE")
    return "Hello, World!"

@app.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    return "About me!"