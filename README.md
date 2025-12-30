📥 Step 1: Download Dataset from Kaggle

Dataset link:
https://www.kaggle.com/datasets/pacific24k/insurance-dataset-v-indian

1️⃣ Install Kaggle API (if not installed)
pip install kaggle

2️⃣ Configure Kaggle API

Go to Kaggle → Account

Download kaggle.json

Place it in:

Windows

C:\Users\<your-username>\.kaggle\kaggle.json


Linux / Mac

~/.kaggle/kaggle.json

📁 Step 2: Create data Folder
mkdir data

⬇️ Step 3: Download Dataset into data/
kaggle datasets download -d pacific24k/insurance-dataset-v-indian -p data/


Unzip the file:

unzip data/insurance-dataset-v-indian.zip -d data/


Make sure the CSV file is inside the data/ folder.

📓 Step 4: Open Notebook
cd notebooks
jupyter notebook


Open:

train_mlflow.ipynb

▶️ Step 5: Run Training Notebook

Run all cells in train_mlflow.ipynb

The notebook:

Loads data from data/

Trains ML model

Logs metrics and model using MLflow

📊 MLflow UI (Optional)

To view experiments:

mlflow ui


Then open in browser:

http://localhost:5000

✅ Requirements
Python 3.8+
pandas
scikit-learn
mlflow
kaggle

jupyter

Install all:

pip install pandas scikit-learn mlflow kaggle jupyter

📌 Notes

Dataset must be inside the data/ folder

Do NOT upload kaggle.json to GitHub

Add .kaggle/ to .gitignore
