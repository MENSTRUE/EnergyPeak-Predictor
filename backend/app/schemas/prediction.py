from pydantic import BaseModel, Field

class FeaturePredictionRequest(BaseModel):
    features: dict[str, float] = Field(min_length=1, max_length=300)
