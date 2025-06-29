from .CostumerData import CostumerData 
import pandas as pd


def predict_new(data:CostumerData,preprocessor,model):
   
    df = pd.DataFrame([data.model_dump()])
    x_processed = preprocessor.transform(df)
    
    y_pred = model.predict(x_processed)
    y_prob = model.predict_proba(x_processed)
    return {
        "loan_prediction":bool(y_pred[0]),
        "loan_probabilty":float(y_prob[0][1])
    }