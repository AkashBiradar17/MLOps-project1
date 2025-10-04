# Student Exam Performance Prediction – MLOps Project

## 📌 Overview

This project predicts a student’s **math score** based on demographics and prior test scores.  
It is built with an **end-to-end ML pipeline**: data ingestion, transformation, model training, and deployment via a Flask web app.

---

## 🏗 Project Structure

MLOps project1/
│
├── notebook/data/stud.csv # Raw dataset
├── artifacts/ # Generated artifacts (train/test data, model, preprocessor)
│ ├── train.csv
│ ├── test.csv
│ ├── model.pkl
│ ├── preprocessor.pkl
│
├── src/
│ ├── components/
│ │ ├── data_ingestion.py
│ │ ├── data_transformation.py
│ │ ├── model_trainer.py
│ │
│ ├── pipeline/
│ │ ├── train_pipeline.py
│ │ ├── predict_pipeline.py
│ │
│ ├── utils.py
│ ├── logger.py
│ ├── exception.py
│
├── templates/
│ └── index.html # Flask UI template
│
├── app.py # Flask app entry point
├── requirements.txt # Python dependencies
└── README.md

---

## 🔄 Workflow

1. **Data Ingestion**  
   Reads dataset → splits into train/test → saves in `artifacts/`.

2. **Data Transformation**

   - Numeric features: Median imputation + StandardScaler
   - Categorical features: Mode imputation + OneHotEncoder + StandardScaler
   - Saves fitted preprocessor (`preprocessor.pkl`).

3. **Model Training**  
   Trains multiple models (Linear, RandomForest, XGBoost, CatBoost) with GridSearchCV → best model saved (`model.pkl`).

4. **Prediction Pipeline**

   - `predict_pipeline.py` loads `preprocessor.pkl` and `model.pkl`.
   - Transforms new input data and returns predicted math score.

5. **Flask Deployment**
   - `app.py` serves UI at `http://127.0.0.1:5000/`.
   - User inputs student details → system predicts math score.

---

## ⚙️ Tech Stack

- **Python** (3.8+)
- **Libraries**: pandas, numpy, scikit-learn, xgboost, catboost, dill, flask
- **Tools**: Git, virtualenv, logging, pickle/dill
- **MLOps Extensions (optional)**: Docker, MLflow, DVC, GitHub Actions CI/CD

---

## ▶️ Running the Project

```bash
# 1. Clone repo and install dependencies
git clone <your-repo-url>
cd MLOps project1
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# 2. Generate artifacts (train/test, preprocessor, model)
python -m src.pipeline.train_pipeline

# 3. Run Flask app
python app.py


Visit: http://127.0.0.1:5000/

📊 Example Input (via UI)

Gender: male

Race/Ethnicity: group B

Parental Education: bachelor’s degree

Lunch: standard

Test Preparation: completed

Reading Score: 62

Writing Score: 79

✅ Example Output

Predicted Math Score: 68.5


```
