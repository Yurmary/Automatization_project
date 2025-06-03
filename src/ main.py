import schedule
from generate_data import generate_data
from load_data import load_data
from configs.config import CONFIG
import logging
import time

# Настройка логирования
logging.basicConfig(
    level=logging.INFO
)

def job():
    logging.info("Начинаем выполнение задачи")
    try:
        # Генерируем данные
        generate_data(CONFIG["data_path"])
        logging.info("Данные сгенерированы")

        # Загружаем данные в базу данных
        load_data(
            CONFIG["db_host"],
            CONFIG["db_port"],
            CONFIG["db_name"],
            CONFIG["db_user"],
            CONFIG["db_password"]
        )
        logging.info("Данные загружены в базу данных")
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")

# Запланируем выполнение задачи каждый день, кроме воскресенья
def schedule_job():
    schedule.every().day.at("09:00").do(job)  # Пример времени — 09:00

    while True:
        schedule.run_pending()
        time.sleep(60)  # Проверяем расписание каждые 60 секунд

if __name__ == "__main__":
    logging.info("Скрипт запущен")
    schedule_job()
