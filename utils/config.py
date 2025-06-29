from dotenv import load_dotenv 
import os
import joblib
load_dotenv(override=True)

# .env variables
APP_NAME = os.getenv('APP_NAME')
VERSION = os.getenv('VERSION')
SECRET_KEY_TOKEN = os.getenv('SECRET_KEY_TOKEN')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_FOLDER_PATH = os.path.join(BASE_DIR,"models")

#models

preprocessor = joblib.load(os.path.join(MODEL_FOLDER_PATH,'preprocessor.pkl'))
logistic = joblib.load(os.path.join(MODEL_FOLDER_PATH,'logistic.pkl'))
forest = joblib.load(os.path.join(MODEL_FOLDER_PATH,'randomforest.pkl'))
xgb = joblib.load(os.path.join(MODEL_FOLDER_PATH,'xgb.pkl'))



