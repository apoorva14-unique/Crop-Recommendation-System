
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Load your dataset
df = pd.read_csv("complete soil data.csv")
df.columns = df.columns.str.strip()

# 2. Select the required columns
features = [
    "N", "P2O5", "K20", "Temparature",
    "Humidity", "PH", "Rainfall", "EC"
]
target = "CROP"

# 3. Convert input columns to numeric values.
# Malformed values such as '0..07' become missing values.
for col in features:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove rows with missing inputs or crop names
before = len(df)
df = df.dropna(subset=features + [target])
df = df[df[target].astype(str).str.strip() != ""]

print("Rows removed during cleaning:", before - len(df))
print("Rows available for training:", len(df))
print("Number of crop classes:", df[target].nunique())

# 4. Prepare features and crop labels
X = df[features]
encoder = LabelEncoder()
y = encoder.fit_transform(df[target].astype(str))

# 5. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# 6. Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 7. Train the model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)

# 8. Evaluate the model
predictions = model.predict(X_test)
print("Test accuracy:", round(
    accuracy_score(y_test, predictions) * 100, 2
), "%")

# 9. Save the model files
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

with open("label_encoder.pkl", "wb") as f:
    pickle.dump(encoder, f)

print("SUCCESS: All three model files were created!")