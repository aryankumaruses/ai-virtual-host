import json
import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# Load dataset
with open("scripts/qa_dataset.json", "r", encoding="utf-8") as f:
    qa_data = json.load(f)

texts = []
intents = []

for intent, response in qa_data.items():
    texts.append(intent)        # or a list of example utterances if available
    intents.append(intent)      # Label is the same as the intent name

# Vectorize and train
model = make_pipeline(
    TfidfVectorizer(),
    LogisticRegression(max_iter=1000)
)

model.fit(texts, intents)

# Save model
os.makedirs("models/intent_model", exist_ok=True)
joblib.dump(model, "models/intent_model/intent_model.pkl")

print("✅ Intent classifier trained and saved.")








