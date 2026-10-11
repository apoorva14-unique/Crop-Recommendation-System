from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model, scaler, and label encoder
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        ec = float(request.form['ec'])

    # Convert to numpy array
        features = np.array([[N, P, K, temperature, humidity, ph, rainfall, ec]])

    # Scale
        features_scaled = scaler.transform(features)

    # Predict
        prediction = model.predict(features_scaled)
        crop_name = label_encoder.inverse_transform(prediction)[0]

    # Pass both inputs and prediction to the same page
        input_data = {
            'N': N, 'P': P, 'K': K,
            'Temperature': temperature, 'Humidity': humidity,
            'pH': ph, 'Rainfall': rainfall, 'EC': ec
        }

        return render_template('index.html', prediction=crop_name, input_data=input_data)

    except Exception as e:
        return render_template('index.html', prediction=f"⚠️ Error: {e}", input_data=None)

if __name__ == '__main__':
  app.run(debug=True)