from fastapi import APIRouter, Query, HTTPException
from app.core.config import settings
from app.services import catalog

router = APIRouter(tags=['research reports'])

@router.get('/series')
def series():
    ids = catalog.available_series()
    return {'source':'saved_kaggle_report', 'count':len(ids), 'series':ids}

@router.get('/series/{series_id}/metrics')
def metrics(series_id: str):
    return {'series_id':series_id, 'source':'saved_kaggle_report', 'metrics':catalog.metric(series_id)}

@router.get('/series/{series_id}/forecast')
def forecasts(series_id: str, limit: int=Query(100,ge=1,le=5000), offset: int=Query(0,ge=0)):
    return {'series_id':series_id, **catalog.forecast(series_id, min(limit,settings.energypeak_max_report_rows), offset)}

@router.get('/reports/model-manifest')
def manifest(limit: int=Query(100,ge=1,le=5000),offset: int=Query(0,ge=0)):
    return catalog.manifest(min(limit,settings.energypeak_max_report_rows),offset)

@router.get('/reports/{report_name}')
def report(report_name: str):
    allowed=catalog.report_names()
    if report_name not in allowed:
        raise HTTPException(404, detail='Unknown report')
    return {'name':report_name,'source':'saved_kaggle_report','data':catalog.load_json(allowed[report_name])}
