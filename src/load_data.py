import pandas as pd
import sqlalchemy as sa
import logging
import os # Импортируем модуль os
from configs.config import CONFIG

logging.basicConfig(level=logging.INFO)

def load_data(db_host, db_port, db_name, db_user, db_password):
data_path = CONFIG["data_path"]

files = os.listdir(data_path)

for file in files:
if file.endswith('.csv'):
try:
df = pd.read_csv(os.path.join(data_path, file))
engine = sa.create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
df.to_sql('sales', engine, if_exists='append', index=False, schema='sales_schema')
logging.info(f"Данные из {file} успешно загружены")
except Exception as e:
logging.error(f"Ошибка при обработке файла {file}: {str(e)}")

if __name__ == "__main__":
try:
load_data(CONFIG["db_host"], CONFIG["db_port"], CONFIG["db_name"], CONFIG["db_user"], CONFIG["db_password"])
except Exception as e:
logging.error(f"Ошибка подключения к БД: {str(e)}")