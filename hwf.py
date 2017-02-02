#to install flask module
#pip install flask

#first flask prog

#@app.route(/../)in which function we use this
#it must be return something
#because it directly send to the web browser
#to display something 


#to run the flask project
#set FLASK_APP=hwf.py
#python -m flask run


#flask module Flask class
#do not change beginner---
from flask import Flask
app = Flask(__name__)
#-- end 

#python function
def call():
	val = input("Enter value: ")
	val = int(val) + 10;
	return val

#default (index) webpage
@app.route('/')
def hello_world():
	return "print value: "
	
#home webpage
@app.route('/home')
def home():
	y = call()
	#we also use html code here
	return ("hello welcome to home"+"<h1>"+str(y)+"</h1>")
	
