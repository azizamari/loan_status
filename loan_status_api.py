from fastapi import FastAPI
from pydantic import BaseModel

class Loan(BaseModel):
    Gender:int
    Married:int
    Education:int
    Self_Employed:int
    ApplicantIncome:float
    CoapplicantIncome:float
    LoanAmount:float
    Loan_Amount_Term:float
    Credit_History:int
    Property_Area:str
    Loan_Status:int

app=FastAPI()

@app.post("/")
def result(instance:Loan):
    return instance