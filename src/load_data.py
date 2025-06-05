import pandas as pd
import sqlalchemy as sa
from sqlalchemy import text
from pathlib import Path
import configparser
import logging

logging.basicConfig(level=logging.INFO)

# Загрузка конфига
CONFIG_PATH = Path(__file__).parent.parent / "configs" / "config.ini"
config = configparser.ConfigParser()
config.read(CONFIG_PATH)


def load_data():
    """Загружает данные в БД с очисткой таблицы"""
    data_path = config["paths"]["data_path"]
    db_config = config["database"]
    schema_config = config["schema"]

    engine = sa.create_engine(
        f"postgresql://{db_config['db_user']}:{db_config['db_password']}@"
        f"{db_config['db_host']}:{db_config['db_port']}/{db_config['db_name']}"
    )

    try:
        # Очистка таблицы
        with engine.connect() as conn:
            conn.execute(text(f"TRUNCATE TABLE {schema_config['db_schema']}.{schema_config['db_table']}"))
            conn.commit()
        logging.info("Таблица очищена")

        # Загрузка данных
        for file in Path(data_path).glob("*.csv"):
            try:
                df = pd.read_csv(file)
                df.to_sql(
                    name=schema_config["db_table"],
                    con=engine,
                    schema=schema_config["db_schema"],
                    if_exists="append",
                    index=False
                )
                logging.info(f"Файл {file.name} загружен")
            except Exception as e:
                logging.error(f"Ошибка загрузки {file.name}: {e}")

    except Exception as e:
        logging.error(f"Ошибка подключения к БД: {e}")


if __name__ == "__main__":
    load_data()