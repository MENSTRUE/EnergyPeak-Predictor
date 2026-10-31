from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND = Path(__file__).resolve().parents[2]
REPO = BACKEND.parent

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=str(BACKEND / '.env'), extra='ignore')
    energypeak_model_dir: Path = REPO / 'models' / 'champion'
    energypeak_report_dir: Path = REPO / 'reports'
    energypeak_cors_origins: str = 'http://localhost:5173,http://127.0.0.1:5173'
    energypeak_max_report_rows: int = Field(default=500, ge=1, le=5000)

    def resolve(self, path: Path) -> Path:
        return (BACKEND / path).resolve() if not path.is_absolute() else path.resolve()

    @property
    def model_dir(self) -> Path:
        return self.resolve(self.energypeak_model_dir)

    @property
    def report_dir(self) -> Path:
        return self.resolve(self.energypeak_report_dir)

    @property
    def origins(self) -> list[str]:
        return [x.strip() for x in self.energypeak_cors_origins.split(',') if x.strip()]

settings = Settings()
