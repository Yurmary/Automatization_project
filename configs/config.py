import os

CONFIG = {
    "data_path": "/Users/mary/Pycharm/Projects/Automatization_project/data",
    "cron_schedule": "0 9 * * 1-6",
    "db_host": os.environ.get("DB_HOST", "localhost"),
    "db_port": os.environ.get("DB_PORT", "5432"),
    "db_name": os.environ.get("DB_NAME", "your_database"),
    "db_user": os.environ.get("DB_USER", "your_username"),
    "db_password": os.environ.get("DB_PASSWORD", "your_password")
}
