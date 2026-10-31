from fastapi.testclient import TestClient
from app.main import app

client=TestClient(app)

def test_health():
    r=client.get('/api/v1/health')
    assert r.status_code==200
    assert r.json()['production_validated'] is False

def test_invalid_id():
    assert client.get('/api/v1/series/../../metrics').status_code in (404,422)
    assert client.get('/api/v1/series/evil/metrics').status_code==422

def test_missing_reports():
    response=client.get('/api/v1/reports/not-a-report')
    assert response.status_code==404

def test_no_fake_model_prediction():
    response=client.post('/api/v1/predict/steel',json={'features':{'lag_1':1.0}})
    assert response.status_code in (422,503)

def test_list_series():
    response=client.get('/api/v1/series')
    assert response.status_code==200
    assert isinstance(response.json()['series'], list)
