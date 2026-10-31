"""Metadata is read from Kaggle report snapshots, never fabricated."""
import csv
import json
import re
from pathlib import Path
from fastapi import HTTPException
from app.core.config import settings

_ID = re.compile(r'^(steel|appliances|electricity_MT_[0-9]+)$')

def valid_id(series_id: str) -> str:
    if not _ID.fullmatch(series_id):
        raise HTTPException(422, detail='Invalid series ID')
    return series_id

def files() -> tuple[Path, Path, Path]:
    root = settings.report_dir
    return root / 'evaluation', root / 'forecasts', root / 'audit'

def available_series() -> list[str]:
    eval_dir, forecasts, _ = files()
    if not eval_dir.is_dir():
        return []
    ids = []
    for file in eval_dir.glob('*_heldout_metrics.json'):
        identifier = file.name.removesuffix('_heldout_metrics.json')
        if _ID.fullmatch(identifier):
            ids.append(identifier)
    return sorted(ids, key=lambda x: (x != 'steel', x != 'appliances', x))

def load_json(path: Path):
    if not path.is_file():
        raise HTTPException(404, detail=f'Report not found: {path.name}')
    try:
        return json.loads(path.read_text(encoding='utf-8-sig'))
    except (ValueError, UnicodeError):
        raise HTTPException(500, detail=f'Malformed report: {path.name}')

def metric(series_id: str):
    valid_id(series_id)
    root, _, _ = files()
    obj = load_json(root / f'{series_id}_heldout_metrics.json')
    if not isinstance(obj, list) or len(obj) != 1 or not isinstance(obj[0], dict):
        raise HTTPException(500, detail='Metric report must have exactly one result object')
    return obj[0]

def recent_rows(path: Path, limit: int, offset: int):
    if not path.is_file():
        raise HTTPException(404, detail=f'Report not found: {path.name}')
    from itertools import islice
    try:
        with path.open(encoding='utf-8-sig', newline='') as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames:
                raise HTTPException(500, detail='Empty CSV header')
            rows = list(islice(reader, offset, offset + limit))
            return {'columns': reader.fieldnames, 'rows': rows, 'limit': limit, 'offset': offset, 'source': 'saved_kaggle_report'}
    except UnicodeError:
        raise HTTPException(500, detail='Invalid CSV encoding')

def forecast(series_id: str, limit: int, offset: int):
    valid_id(series_id)
    _, folder, _ = files()
    return recent_rows(folder / f'{series_id}_heldout_predictions.csv', limit, offset)

def report_names():
    eval_dir, _, audit = files()
    paths = {
        'research_gate': eval_dir / 'research_gate.json',
        'run_config': eval_dir / 'run_config.json',
        'claim_boundaries': eval_dir / 'claim_boundaries.json',
        'electricity_results': eval_dir / 'electricity_results.json',
    }
    return paths

def manifest(limit: int, offset: int):
    _, _, audit = files()
    return recent_rows(audit / 'model_manifest.csv', limit, offset)
