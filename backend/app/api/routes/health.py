from fastapi import APIRouter
from app.core.config import settings
from app.services.catalog import available_series
from app.inference.predictor import model_available

router = APIRouter(tags=['health'])

@router.get('/health')
def health():
    ids = available_series()
    return {'status':'ok','service':'EnergyPeak Predictor API','version':'0.1.0',
            'production_validated':False,'live_grid_connected':False,
            'reports_available':len(ids)>0,'series_count':len(ids),
            'model_files_available':{i:model_available(i) for i in ids},
            'report_dir':str(settings.report_dir)}
