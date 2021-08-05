# IndianCurrencyDetection
Detection of currency notes using deep learning


Foreign and visually disable people in India often find difficulties in recognizing different currency notes. Even if some time it is also difficult for Indian healthy people to identify same amount of currency notes with different-new designs. Human eye has also some limitation so some time fake currency not identifiable by them. In this paper deep learning model is trained with dataset and is being tested with different Indian currency with good accuracy.

Training the machine to learn to detect and recognize object from given input, so the machine learning is based on what it sees and learns from their image dataset. Therefore, with a good amount of quality images we can improve machine’s learning ability.

## Technologies used :
- Python, Tensorflow, Streamlit

- Dataset is taken from Kaggle

## Files :
- currencydetectionmodel.ipynb :
  - Here we load the data and preprocess the same
  - build the ML deep learning model
  - train the model with the dataset
  - plot graphs for clear understanding
- app.py : 
  - Contains python code for streamlit library
  - Initial display, Uploading image, Displaying result
- img_classification.py :
  - Contains python code to predict the result
  - Takes uploaded image, loads the ML model, Computes

## How to run the file from cmd :
- Go to the file location
- use the command : Streamlit run app.py

## Future scope :

We used Convolution and Dense layers to create our model which helps in detecting Indian Currency accurately to a good extent.
Futher we can add audio files which will tell us the identified currency and can be used to help the visually disabled, foreign and aged people.
