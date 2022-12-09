from flask import Flask
from flask import render_template, redirect, request, send_from_directory

from werkzeug.utils import secure_filename
import os

from badwords import bad_words_highlight
from sentiment import sentimentfunc
from tweetsanalysis import tweetAnalysis

app = Flask(__name__,static_url_path = "/static")

@app.route("/")
def home_page():
    return render_template("index.html") 

@app.route("/home")
def home_re():
    return redirect("/")

@app.route("/tweet",methods=['GET'])
def tweet_page():
    return render_template("tweetanalysis.html")

@app.route("/tweet",methods=['POST'])
def tweet_hate():
    results = tweetAnalysis(request.form['word'],int(request.form['count']))
    return render_template("tweetanalysisResult.html",keyword = request.form['word'], emotion = request.form['emotion'],result=results)
    

if __name__ == "__main__":
        app.run(debug=True)


