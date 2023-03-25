import os
import sys
import warnings
from model_handlers import respiratory_model, heart_disease_model, parkinson_model
from flask import Flask, url_for, request, render_template
from werkzeug.utils import secure_filename

warnings.filterwarnings("ignore")

app = Flask(__name__)

classes = [
    "Bronchiectasis",
    "Bronchiolitis",
    "COPD",
    "Healthy",
    "Pneumonia",
    "URTI",
]

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('Home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('aboutus.html')

@app.route('/heart', methods=['GET', 'POST'])
def heart():
    if request.method == "GET":
        return render_template('HeartDisease.html', got_prediction=False)
    elif request.method == "POST":
        prediction = heart_disease_model(list(request.form.values()))
        result = "Heart Disease Not Found" if prediction == 0 else "Heart Disease Found"
        return render_template('HeartDisease.html', result=result, got_prediction=True)

@app.route('/parkinson', methods=['GET', 'POST'])
def parkinson():
    if request.method == "GET":
        return render_template('Parkinson.html', got_prediction=False)
    elif request.method == "POST":
        print(request.files)
        f = request.files['file']
        print(f)
        print(f.filename)
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploaded-data', secure_filename(f.filename))
        f.save(file_path)

        prediction = parkinson_model(file_path)

        result = "Parkinsons Not Found" if prediction == 0 else "Parkinsons Found"
        return render_template('Parkinson.html', result=result, got_prediction=True)


@app.route('/respiratory', methods=['GET', 'POST'])
def resp_detect():
    if request.method == "GET":
        return render_template('Respiratory.html', got_prediction=False)
    if request.method == "POST":
        f = request.files.get('uploaded-audio', None)

        if f is None:
            return render_template('Respiratory.html', got_prediction=False)

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploaded-data', secure_filename(f.filename))
        f.save(file_path)
        prediction = respiratory_model(file_path)

        if(type(prediction) == str):
            return render_template('Respiratory.html', got_prediction=False)
        print(prediction)
        return render_template('Respiratory.html', prediction=prediction, classes=classes, got_prediction=True)

if __name__ == "__main__":
    app.run(debug=True)
