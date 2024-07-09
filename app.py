from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the model
model = load_model('base_model.h5')
name_list = {0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer', 5: 'dog', 6: 'frog', 7: 'horse', 8: 'ship', 9: 'truck'}

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file:
        image = Image.open(io.BytesIO(file.read()))
        image = image.resize((32, 32))  # Adjust this to your model's expected input dimensions
        image = np.expand_dims(image, axis=0)
        image = np.array(image) / 255.0  # Normalize if required by your model

        predictions = model.predict(image)
        predicted_class = np.argmax(predictions, axis=1)
        print(predicted_class)
        class_name = name_list[int(predicted_class[0])]  # Convert class ID to class name
        print(class_name)

        return jsonify({'class_name': class_name, 'confidence': float(predictions[0][predicted_class[0]])})

if __name__ == '__main__':
    app.run(debug=True, port=5320)
