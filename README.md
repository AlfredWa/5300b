This project is an image classification application using a Flask backend and an HTML/JavaScript frontend. It allows users to upload images and get predictions from a trained model.

The model training was implemented in the Google Colab using T4 GPU. 
All the required Python libraries are available on Google Colab, no installation needed. The ipynb will save the trained model into a h5 file which the python app could load.

The application is split into two main components:
1. **Backend**: A Flask application that serves the trained image classification model.
2. **Frontend**: An HTML page with JavaScript that allows users to upload images to be classified by the backend.

Before you can run this application, you'll need the following installed:
- Python 3.x
- Flask
- TensorFlow (or TensorFlow GPU)
- PIL (Pillow)

Run the Flask application with command: python app.py
This will start the server on http://localhost:5320
The one Demo in class will be available on public IP by ngrok instead of this local server.

Open the index.html file in a web browser to access the frontend.

Github link: https://github.com/AlfredWa/5300b