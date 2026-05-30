"""Application configuration."""

import os
from dotenv import load_dotenv

# Load từ project .env
load_dotenv()

# Nếu key < 20 ký tự → đọc đúng dòng từ hermes .env
current_key = os.getenv("XIAOMI_API_KEY", "")
if len(current_key) < 20:
    hermes_env = os.path.expanduser("~/.hermes/.env")
    if os.path.exists(hermes_env):
        with open(hermes_env, "r") as f:
            lines = f.readlines()
            # Dòng 474 chứa key đúng
            for line in lines:
                stripped = line.strip()
                if stripped.startswith("XIAOMI_API_KEY=tp-sad"):
                    key = stripped.split("=", 1)[1]
                    os.environ["XIAOMI_API_KEY"] = key
                    print(f"[CONFIG] Loaded API key from hermes .env (length: {len(key)})")
                    break


class Settings:
    APP_ENV: str = os.getenv("APP_ENV", "development")
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT: int = int(os.getenv("APP_PORT", "8000"))
    
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///data/roadmaps.db")
    
    # Xiaomi MiMo API
    XIAOMI_API_KEY: str = os.getenv("XIAOMI_API_KEY", "")
    XIAOMI_BASE_URL: str = os.getenv("XIAOMI_BASE_URL", "https://token-plan-sgp.xiaomimimo.com/v1")
    XIAOMI_MODEL: str = os.getenv("XIAOMI_MODEL", "mimo-v2.5")
    
    @property
    def db_path(self) -> str:
        """Get SQLite database path."""
        if self.DATABASE_URL.startswith("sqlite:///"):
            return self.DATABASE_URL.replace("sqlite:///", "")
        return "data/roadmaps.db"


settings = Settings()
