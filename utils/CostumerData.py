from pydantic import BaseModel, Field
from typing import Literal

class CostumerData(BaseModel):
    income_annum: int = Field(description="Annual income of the applicant (range: 200,000 - 9,900,000)")
    loan_amount: int = Field(description="Total loan amount requested (range: 300,000 - 39,500,000)")
    loan_term: int = Field(ge=2, le=20, description="Loan term in years (range: 2 - 20)")
    cibil_score: int = Field(ge=300, le=900, description="CIBIL credit score of the applicant (range: 300 - 900)")
    bank_asset_value: int = Field(description="Assets declared to bank (range: 0 - 14,700,000)")
    total_assets: int = Field(description="Total assets owned by applicant (range: 400,000 - 9,070,000)")
    loan_to_income: float = Field(ge=1.5, le=4.0, description="Ratio of loan amount to annual income (range: 1.5 - 4.0)")
    loan_to_assets_ratio: float = Field(ge=1.17, le=2.33, description="Ratio of loan amount to total assets (range: 1.17 - 2.33)")
    education: Literal['Graduate', 'Not Graduate'] = Field(description="Educational qualification of the applicant")
    self_employed: Literal['Yes', 'No'] = Field(description="Whether the applicant is self-employed")
    commercial_assets_value: int = Field(description="Value of commercial assets owned by the customer")
    residential_assets_value: int = Field(description="Value of residential assets owned by the customer")
    luxury_assets_value: int = Field(description="Value of luxury assets owned by the customer")
    no_of_dependents: int = Field(ge=0, description="Number of dependents the customer has")