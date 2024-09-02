from crypt import methods
from tabnanny import check
from time import sleep
from unittest import result
from flask import Flask, render_template, request, redirect,jsonify,session
from werkzeug.utils import secure_filename
import os
import random

app = Flask(__name__)
app.secret_key = 'lv_3000'

app.config["SESSION_TYPE"] = "filesystem"
app.config['SESSION_PARMANENT'] = False

url_file = "url.txt"

@app.after_request
def after_request(response):
  """Ensure responses aren't cached"""
  response.headers["Cache-Control"] = "no-cache,no-store,must-revalidate"
  response.headers["Expires"] = 0
  response.headers["Pragma"] = "no-cache"
  return response


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/url',methods=['POST', 'GET'])
def url():
  if request.method == 'POST':
    data = request.get_json()
    if 'url' in data:
      url = data['url']
      # Save the URL to the file
      with open(url_file, 'w') as file:
        file.write(url)
      return jsonify({"message": "URL saved successfully"}), 200
    else:
      return jsonify({"error": "No URL provided"}), 400
  
  elif request.method == 'GET':
    try:
    # Read the URL from the file
      with open(url_file, 'r') as file:
        url = file.read()
      return jsonify({"url": url}), 200
    except FileNotFoundError:
      return jsonify({"error": "File not found"}), 404
    except Exception as e:
      return jsonify({"error": str(e)}), 500

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/progress')
def progress():
    return render_template('progress.html')


if (__name__ == "__main__"):
    print("started")
    app.run(host="0.0.0.0", port = 9090, debug= True)
