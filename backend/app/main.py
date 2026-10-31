from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import health, reports, inference

app=FastAPI(title='EnergyPeak Predictor API', version='0.1.0',
 description='Research-only one-step-ahead forecasting, saved held-out evaluation, and read-only Kaggle reports. Not live grid control.')
app.add_middleware(CORSMiddleware,allow_origins=settings.origins,allow_credentials=False,
                   allow_methods=['GET','POST'],allow_headers=['Content-Type'])
app.include_router(health.router,prefix='/api/v1')
app.include_router(reports.router,prefix='/api/v1')
app.include_router(inference.router,prefix='/api/v1')

@app.get('/')
def root():
    return {'service':'EnergyPeak Predictor API','swagger':'/docs','health':'/api/v1/health'}
