from flask import Flask, Response, render_template
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

app = Flask(__name__)

model_file_path = model_pickle

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/training', methods=['POST','GET'])
def training_route_client():
    try:
        return Response('Training is succesfull')
    except Exception as e:
        print(str(e))
        return Response("Error", status=500)
if __name__ == '__main__':
    app.run()

