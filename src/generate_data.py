import csv
from datetime import datetime
import random
import os
import shutil
from pathlib import Path
import configparser
import logging

logging.basicConfig(level=logging.INFO)

# Загрузка конфига
CONFIG_PATH = Path(__file__).parent.parent / "configs" / "config.ini"
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

CATEGORIES = ["бытовая химия", "текстиль", "посуда"]
ITEMS = {
    "бытовая химия": ["гель для стирки", "порошок", "средство для мытья посуды"],
    "текстиль": ["полотенца", "наволочки", "простыни"],
    "посуда": ["кастрюля", "сковорода", "тарелки"]
}


def clear_data_dir(data_path: str) -> bool:
    """Очищает папку с данными перед генерацией"""
    try:
        if os.path.exists(data_path):
            shutil.rmtree(data_path)
        os.makedirs(data_path, exist_ok=True)
        logging.info(f"Папка {data_path} очищена")
        return True
    except Exception as e:
        logging.error(f"Ошибка очистки папки: {e}")
        return False


def generate_data():
    """Генерирует новые данные"""
    data_path = config["paths"]["data_path"]

    if config.getboolean("paths", "clean_before_generate"):
        if not clear_data_dir(data_path):
            return

    for shop_id in range(1, 11):  # 10 магазинов
        for cash_id in range(1, 6):  # 5 касс в каждом
            filename = Path(data_path) / f"{shop_id}_{cash_id}.csv"
            try:
                with open(filename, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(
                        ["doc_id", "item", "category", "amount", "price", "discount", "shop_num", "cash_num"])

                    for _ in range(random.randint(50, 150)):
                        doc_id = f"{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(1000, 9999)}"
                        category = random.choice(CATEGORIES)
                        item = random.choice(ITEMS[category])
                        amount = random.randint(1, 10)
                        price = round(random.uniform(10.0, 100.0), 2)
                        discount = round(random.uniform(0.0, 5.0), 2)
                        writer.writerow([doc_id, item, category, amount, price, discount, shop_id, cash_id])

                logging.info(f"Сгенерирован файл {filename.name}")
            except Exception as e:
                logging.error(f"Ошибка генерации файла {filename}: {e}")


if __name__ == "__main__":
    generate_data()