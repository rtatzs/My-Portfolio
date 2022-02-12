from myprofilelib.profile import getInitializeProfile
from pickle import NONE, TRUE
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "f5bb0c8de146c67b44babbf4e6584cc0"

@app.route("/MyProfile")
def myprofile():
	myprofile = getInitializeProfile()
	return render_template("myprofile.html", myprofile = myprofile)
