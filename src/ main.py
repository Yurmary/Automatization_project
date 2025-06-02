import schedule
import time
from generate_data import generate_data
from load_data import load_data
from configs.config import CONFIG

def job():
# Генерируем данные
generate_data(CONFIG["data_path"])

# Загружаем данные в базу данных
load_data(
CONFIG["db_host"],
CONFIG["db_port"],
CONFIG["db_name"],
CONFIG["db_user"],
CONFIG["db_password"]
)

# Запланируем выполнение задачи каждый день, кроме воскресенья
def schedule_job():
schedule.every().day.at("09:00").do(job) # Пример времени — 09:00

while True:
schedule.run_pending()
time.sleep(60) # Проверяем расписание каждые 60 секунд

if __name__ == "__main__":
schedule_job()