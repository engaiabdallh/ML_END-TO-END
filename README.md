# Loan Approval Prediction API

A FastAPI app that predicts loan approval status using trained ML models.

## Features

- FastAPI REST endpoints for predictions
- Supports Logistic Regression, Random Forest, XGBoost
- Modular preprocessing and inference pipeline
- Dockerized setup
- Configurable using `.env`
- Notebook included for training and EDA

## Directory Overview

```
.
├── main.py                 # FastAPI app entry point
├── UI.py                   # Optional frontend interface (if used)
├── t.ipynb                 # Temporary or test notebook
├── .env                    # Environment config
├── .env.example            # Template for .env
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker setup
│
├── dataset/
│   └── loan_approval_dataset.csv
│
├── models/
│   ├── logistic.pkl
│   ├── randomforest.pkl
│   ├── xgb.pkl
│   └── preprocessor.pkl
│
├── notebooks/
│   └── noebook.ipynb       # Training + analysis
│
└── utils/
    ├── config.py
    ├── CostumerData.py     # Data input schema
    ├── inference.py        # Model loading and predictions
    └── __init__.py
```

## Setup Instructions

### 1. Clone the repo

```bash
git clone <repo-url>
cd <repo-folder>
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup environment variables

```bash
cp .env.example .env
```

Edit `.env` and set the values (e.g. model paths if needed)

## Run Locally

```bash
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for Swagger UI.

## Example API Request

**Endpoint:** `POST /predict`

**Sample JSON:**

```json
{
  "Gender": "Male",
  "Married": "Yes",
  "Dependents": "1",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5000,
  "CoapplicantIncome": 2000,
  "LoanAmount": 100,
  "Loan_Amount_Term": 360.0,
  "Credit_History": 1.0,
  "Property_Area": "Urban"
}
```

**Response:**

```json
{
  "prediction": "Approved"
}
```

## Run with Docker

```bash
docker build -t loan-approval-app .
docker run -p 8000:8000 loan-approval-app
```

## Model Info

Trained and saved models are located in `/models`:

- `logistic.pkl`
- `randomforest.pkl`
- `xgb.pkl`
- `preprocessor.pkl`

Used by `utils/inference.py`.

## Dataset

- File: `dataset/loan_approval_dataset.csv`
- Used for training and evaluation

## Re-train or Experiment

Use `notebooks/noebook.ipynb` to:

- Load and preprocess data
- Train or tune models
- Export new `.pkl` model files

## Tech Stack

- Python
- FastAPI
- scikit-learn
- XGBoost
- Pandas, NumPy
- Docker

## Todo

- Add user auth (JWT)
- Connect to a database
- Add logging and monitoring
- Improve error handling

## License

MIT