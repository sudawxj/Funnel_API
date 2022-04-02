from flask import Flask, jsonify, request, render_template
import json
import numpy as np
import pickle
import re
import nltk
from nltk import pos_tag
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use', 'gov','com'])
from nltk.stem import WordNetLemmatizer

# a function for Filter for only nouns
def noun_only(x):
    pos_comment = nltk.pos_tag(x)
    filtered =[word[0] for word in pos_comment if word[1] in ['NN']]
    return filtered


def tokenizer(text):
    lemmatizer = WordNetLemmatizer()
    sentence = re.sub(r"[^A-Za-z]", " ", text)# remove everthing expect the words
    words = re.sub(r'(^| ).( |$)',' ',sentence) # remove single character word
    words = re.sub(r'(^| ).( |$)',' ',words).lower().split() # remove the remaining single charater
    words = [word for word in words if word not in stop_words] # remove stopwords
    words = [lemmatizer.lemmatize(word) for word in words] # lemmatize the words
    words = noun_only(words) # keep only the nouns
    return words

topics = {0: "TIME", 1: "COMPUTER", 2: "INFORMATION", 3: "SPORTS"}
with open("model_xgb.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    pred = ""
    if request.method == "POST":
        email = [request.form["email"]]
        y = model.predict(email)
        pred = topics[int(y[0])]
    return render_template("index.html", pred=pred)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
