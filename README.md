<center>

# Diagnose Me

</center>

A web application powered by deep learning to predict respiratory disorders, heart diseases, and parkinson's disease with just an image, audio, or text input from users.
![Bot Description](https://github.com/DhritiGabani/Diagnose-me/blob/master/UI%20Design/homepage.png?raw=true)
## Technologies used

- Node.js
- Python
- TensorFlow
- Sci-kit Learn

## Metrics of the models trained

- Respiratory Disease Detection Model (CNN) :: 90.8% accuracy
- Heart Disease Detection Model (RandomForestCLassifier) :: 84.8% accuracy
- Parkinson's Disease Model (CNN) :: 76.6% accuracy

<br />

## Multi-Respiratory Disease Diagnosis

![Bot Description](https://github.com/DhritiGabani/Diagnose-me/blob/master/UI%20Design/respiratory.png?raw=true)

The sound emitted when a person breathes directly changes within lung tissue and the position of secretions within the lung. This, if captured, opens up the possibility of dianosing disorders like asthma, pneumonia, and bronchiolitis, to name a few. In this project, that information is captured in audio using digital stethoscopes.

The audio are converted into mel-spectrograms and then these mel spectrograms are fed as an input to convolutional neural networks that outputs a vector representing the probability of occurence of that disease.
The disease classified from the model are

- Bronchiolitis
- Pneuomonia
- Asthma
- Bronchitis


## Heart Disease Diagnosis
![Bot Description](https://github.com/DhritiGabani/Diagnose-me/blob/master/UI%20Design/respiratory.png?raw=true)

Heart Disease describes a range of conditions that affect your heart. This can be cause by many factors. But using some information from day to day life, it can be effective to know to get an appointment with this project. Here, we take previous medical records of patients like Maximum Heart Rate Achieved, Blood Pressure, Cholestrol Levels, Exercise-induced Agina, Age etc. A Random Forest Classifier is trained to take these as an input and make a binary decision to predict whether the fed inputs imply chances of getting a heart disease.

## Parkinson's Disease Diagnosis
![Bot Description](https://github.com/DhritiGabani/Diagnose-me/blob/master/UI%20Design/parkinson.png?raw=true)

Parkinson's Disease is a brain disorder that leads to shaking, stifness, and face difficulty in tasks with balance and coordination. Drawing requires the stability of hand movement. We can get an intuition that it could help us diagnose the disease at some level. Here in this project, we use the dataset that contains drawings of waves and spirals drawn by both healthy patients and diagnosed patients. These drawings are given as an input to a convolutional neural network to make a binary decision of whether the drawing is done by the patient with parkinson's disease or a one.

<br />

## Setting up the local environment

1. Clone the repository

```shell
git clone https://github.com/DhritiGabani/Diagnoseme
```

2. Navigate to the directory

```shell
cd Diagnoseme
```

3. Install the required dependencies

```shell
npm install
pip install -r requirements.txt
```

4. Visit the web application at `localhost:8000/`
