#length of string using js

from flask import Flask
app = Flask(__name__)


def call():
	val = input("Enter value: ")
	val = int(val) + 10;
	return val


@app.route('/')
def hello_world():
	return """
	<html>
	<head>
	<style>
		p{
		padding:0px;
		margin:0px;
		}
	</style>
	</head>
	<body>
	<form name="form1" >
		<input type="text" name="name">
		<input type="button" value="length" onclick="fun()">
	</form>
	<p id="demo"></p>
	</body>
	<script>
	function fun()
	{
		 var x = document.forms["form1"]["name"].value;
    	document.getElementById("demo").innerHTML = "length of your string: " + x.length;
    }
	</script>
	</html>"""
	
