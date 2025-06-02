import pandas as pd
import sqlalchemy as sa
import os
from sqlalchemy.exc import IntegrityError


def load_data(engine):
    data_path = 'data'
    files = os.listdir(data_path)

    for file in files:
        if file.endswith('.csv'):
            try:
                df = pd.read_csv(os.path.join(data_path, file))
                df.to_sql('sales', engine, if_exists='append', index=False)
                print(f"Данные из {file} успешно загружены")
            except IntegrityError:
                print(f"Ошибка загрузки данных из {file}: дублирующиеся чеки")
            except Exception as e:
                print(f"Ошибка при обработке файла {file}: {str(e)}")


if __name__ == "__main__":
    engine = sa.create_engine('postgresql://user:password@localhost/sales_db')
    load_data(engine)
