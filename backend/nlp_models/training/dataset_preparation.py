# backend/nlp_models/training/dataset_preparation.py

import json
import pandas as pd
from sklearn.model_selection import train_test_split

def prepare_dataset(json_path, output_dir):
    with open(json_path, 'r') as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    train, test = train_test_split(df, test_size=0.2, random_state=42)

    train.to_csv(f"{output_dir}/train.csv", index=False)
    test.to_csv(f"{output_dir}/test.csv", index=False)
    print("✅ Dataset prepared and saved.")

if __name__ == "__main__":
    prepare_dataset("scripts/qa_dataset.json", "nlp_models/training")

