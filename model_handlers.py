import librosa
from tensorflow.keras.models import load_model
import joblib
import numpy as np
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier
import cv2


def respiratory_model(audio_path):
    if audio_path.split(".")[-1] not in ["wav", "mp3", "m4a"]:
        return "Wrong File Uploaded"

    clip, sr = librosa.load(audio_path)
    mfccs = librosa.feature.mfcc(y=clip, sr=sr, n_mfcc=40)
    if mfccs.shape[1] == 862:
        model = load_model(
            "static/models/respiratory-Model/respiratory-model.h5")
        mfccs = mfccs.reshape(1, 40, 862, 1)
        predictions = model.predict(mfccs)
        predictions = [("{:.2f}".format(pred * 100))
                       for pred in predictions[0]]
        return predictions
    else:
        return "Cannot process audio file"


def heart_disease_model(data):
    model = joblib.load(
        "./static/models/heart-disease-detection-model/model.joblib")
    X_test = np.array(data)

    df = pd.DataFrame(data=X_test).T
    if '' not in X_test:
        prediction = model.predict(df)
        print(prediction[0])

    return prediction[0]


def parkinson_model(image_path):
    model = load_model(
        "static/models/parkinsons-detection-model/parkinson-model.h5")
    img = cv2.imread(image_path)
    img = cv2.resize(img, (200, 200))  # Resizing the images
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converting the image into RBG
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)
    return np.argmax(prediction)
