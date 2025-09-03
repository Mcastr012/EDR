import os

# Database Settings
DB_NAME = os.getenv('DB_NAME', 'edr')
DB_USER = os.getenv('DB_USER', '')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PASS = os.getenv('DB_PASS', '')

# App Settings
APP_DEBUG_MODE = os.getenv("APP_DEBUG_MODE", True)
APP_HOST = "0.0.0.0"

# ELK Settings
ES_HOST = os.getenv("ES_HOST", "elastic")
WINLOGBEAT_INDEX = os.getenv("WINLOGBEAT_INDEX", "winlogbeat-*")
ATTCK_YAML = "attck.yaml"
