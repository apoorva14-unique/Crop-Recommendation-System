# 🌾 Crop Recommendation System Using Ensemble Techniques

## 📌 Project Overview

The **Crop Recommendation System Using Ensemble Techniques** is a machine learning-based agricultural decision support system designed to recommend suitable crops based on soil properties and climatic conditions. The system analyzes important agricultural parameters such as Nitrogen (N), Phosphorus (P), Potassium (K), soil pH, Electrical Conductivity (EC), temperature, humidity, and rainfall to predict an appropriate crop.

The project explores individual machine learning algorithms and ensemble learning techniques to analyze agricultural data and improve crop prediction. A Flask-based web application provides a simple interface where users can enter soil and environmental parameters and receive crop recommendations.

## 🎯 Objectives

- To develop a machine learning-based crop recommendation system using agricultural soil and climatic data.
- To implement and evaluate different machine learning and ensemble learning techniques for crop prediction.
- To provide a user-friendly web application that helps users identify suitable crops based on input agricultural conditions.

## ⚙️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Algorithms | Linear Regression, SVM, Random Forest |
| Ensemble Techniques | Bagging, Boosting, Stacking |
| Meta-Learner | XGBoost |
| Web Framework | Flask |
| Frontend | HTML, CSS |
| Model Serialization | Pickle |
| Development Environment | Visual Studio Code |

## 📊 Dataset Description

The project uses an agricultural soil and environmental dataset containing crop information and important soil and climatic parameters.

### Input Features

| Feature | Description |
|---|---|
| N | Nitrogen content in soil |
| P | Phosphorus content in soil |
| K | Potassium content in soil |
| Temperature | Environmental temperature |
| Humidity | Relative humidity |
| pH | Soil acidity or alkalinity |
| Rainfall | Rainfall measurement |
| EC | Electrical Conductivity of soil |

**Target Variable:** Crop – the crop category to be predicted.

**Dataset File:** `complete soil data.csv`

## 🧠 Methodology

The proposed system follows a multi-stage machine learning workflow:

1. **Data Collection:** Collect agricultural soil and climatic information.
2. **Data Preprocessing:** Clean the dataset, handle missing and inconsistent values, encode crop labels and scale numerical features.
3. **Training and Testing:** Divide the processed dataset into training and testing sets.
4. **Base Model Development:** Implement Linear Regression, Support Vector Machine (SVM) and Random Forest.
5. **Ensemble Learning:** Apply Bagging, Boosting and Stacking techniques.
6. **Meta-Learning:** Use XGBoost as the meta-learner in the stacking approach.
7. **Model Evaluation:** Evaluate model performance using suitable classification metrics, including accuracy, precision, recall and F1-score.
8. **Crop Prediction:** Integrate the trained model into a Flask web application to generate crop recommendations.

## 🏗️ System Architecture

```text
          Agricultural Dataset
                   |
                   v
            Data Preprocessing
                   |
                   v
             Training & Testing
                   |
                   v
           Base Machine Learning
                   |
          ---------------------
          |         |         |
          LR        SVM       RF
          |         |         |
          ---------------------
                   |
                   v
           Ensemble Learning
          ---------------------
          |         |         |
       Bagging   Boosting  Stacking
                             |
                             v
                       XGBoost
                      Meta-Learner
                             |
                             v
                      Model Evaluation
                             |
                             v
                      Crop Prediction
                             |
                             v
                     Flask Web Application
                             |
                             v
                     Recommended Crop
```

## 💻 Application Features

- Simple and user-friendly web interface.
- Accepts eight soil and climatic input parameters.
- Processes user-provided agricultural information.
- Generates crop recommendations using a trained machine learning model.
- Displays the predicted crop along with submitted input values.
- Integrates the machine learning model with Flask.

## 📂 Project Structure

```text
Crop-Recommendation-System/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── train_model.py
├── complete soil data.csv
│
├── model.pkl
├── scaler.pkl
├── label_encoder.pkl
│
├── style.css
├── README.md
└── .gitignore
```

## 🚀 Installation and Execution

### Step 1: Clone the Repository

```bash
git clone https://github.com/apoorva14-unique/Crop-Recommendation-System.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Crop-Recommendation-System
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### Step 5: Install Required Libraries

```bash
pip install flask numpy pandas scikit-learn
```

Install any additional dependencies required by your training script.

### Step 6: Run the Application

If the trained model files are already available:

```bash
python app.py
```

### Step 7: Open the Application

Open the following URL in your browser:

```text
http://127.0.0.1:5000
```

Enter the soil and climatic parameters and click **Predict Suitable Crop** to view the recommendation.

### Optional: Train the Model Again

If you want to regenerate the trained model files, execute:

```bash
python train_model.py
```

This generates the model artifacts required by the Flask application.

## 📈 Results

The project explores multiple machine learning and ensemble learning approaches for crop prediction.

The following results were reported in the research experiments:

| Algorithm | Reported Accuracy |
|---|---:|
| Linear Regression | 59.81% |
| Support Vector Machine | 89.90% |
| Random Forest | 93.01% |
| Bagging | 91.79% |
| Boosting | 92.58% |
| Stacking | 80.07% |

**Note:** These are the reported research experiment results, not the accuracy of every subsequently trained model. The current retrained model produced 53.39% test accuracy on the cleaned dataset.

## 🌱 Sample Prediction

The application accepts soil and climate information and generates a suitable crop recommendation.

**Example Input:**

| Parameter | Value |
|---|---:|
| Nitrogen | 150 |
| Phosphorus | 14 |
| Potassium | 270 |
| Temperature | 34.59°C |
| Humidity | 77.4% |
| Soil pH | 8.01 |
| Rainfall | 834.3 mm |
| EC | 0.12 |

**Example Output:** Cotton

## 🔮 Future Enhancements

- Integration of real-time weather information.
- IoT-based soil monitoring.
- Improved prediction performance through advanced ensemble techniques and hyperparameter tuning.
- Support for additional agricultural datasets and geographical regions.
- Multilingual support for farmers.
- Deployment on a cloud platform for wider accessibility.

---

⭐ If you find this project useful, consider giving the repository a star.

**Project Domain:** Machine Learning | Ensemble Learning | Precision Agriculture | Crop Recommendation