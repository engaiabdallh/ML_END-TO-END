from fastapi import FastAPI,HTTPException,Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils.inference import predict_new 
from utils.config import APP_NAME,VERSION,SECRET_KEY_TOKEN,preprocessor,logistic,forest,xgb
from utils.CostumerData import CostumerData

app = FastAPI(title=APP_NAME,version=VERSION)

# to deal block requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/',tags=['General'])
async def home():
    return{
        "message":f"Welcome to {APP_NAME} API v{VERSION}"
    }


security = HTTPBearer()

async def verify_api_key(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="You are not authorized to use this API")
    return credentials.credentials


@app.post('/predict/logistic',tags=['Models'])          
async def predict_logistic(data: CostumerData,credentials:str=Depends(verfiy_api_key)) -> dict:
    
    try:
        result = predict_new(data=data,preprocessor=preprocessor,model = logistic)      
        return result
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
@app.post('/predict/forest',tags=['Models'])
async def predict_forest(data: CostumerData,credentials:str=Depends(verfiy_api_key)) -> dict:
    try:
        result = predict_new(data=data,preprocessor=preprocessor,model=forest)
        return result 
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
@app.post('/predict/xgboost',tags=['Models'])
async def predict_xgboost(data: CostumerData,credentials:str=Depends(verfiy_api_key)) -> dict:
    try:
        result = predict_new(data=data,preprocessor=preprocessor,model=xgb)
        return result 
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
