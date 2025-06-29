from fastapi import FastAPI,HTTPException,Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
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


api_key_header = APIKeyHeader(name="X-API-Key")

async def verfiy_api_key(api_key:str=Depends(api_key_header)):
    if api_key!= SECRET_KEY_TOKEN:
        raise HTTPException(status_code=403,detail="you are not authorized to use API")
    return api_key
    


@app.post('/predict/logistic',tags=['Models'])          
async def predict_logistic(data: CostumerData,api_key:str=Depends(verfiy_api_key)) -> dict:
    
    try:
        result = predict_new(data=data,preprocessor=preprocessor,model = logistic)      
        return result
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
@app.post('/predict/forest',tags=['Models'])
async def predict_forest(data: CostumerData,api_key:str=Depends(verfiy_api_key)) -> dict:
    try:
        result = predict_new(data=data,preprocessor=preprocessor,model=forest)
        return result 
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
@app.post('/predict/xgboost',tags=['Models'])
async def predict_xgboost(data: CostumerData,api_key:str=Depends(verfiy_api_key)) -> dict:
    try:
        result = predict_new(data=data,preprocessor=preprocessor,model=xgb)
        return result 
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))