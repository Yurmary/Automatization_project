import csv
from datetime import datetime
import random
import os
from configs.config import CONFIG
import logging


# Настройка логирования
logging.basicConfig(
    level=logging.INFO
)

# Список категорий и товаров
CATEGORIES = ["бытовая химия", "текстиль", "посуда"]
ITEMS = {
    "бытовая химия": ["гель для стирки", "порошок", "средство для мытья посуды"],
    "текстиль": ["полотенца", "наволочки", "простыни"],
    "посуда": ["кастрюля", "сковорода", "тарелки"]
}


def generate_filename(shop_id, cash_id):
    try:
        data_path = CONFIG["data_path"]
        logging.info(f"Используемый путь к данным: {data_path}")

        if not os.path.exists(data_path):
            logging.info(f"Папка {data_path} не существует, пытаемся создать...")
            os.makedirs(data_path)
            logging.info(f"Создана директория: {data_path}")

        return os.path.join(data_path, f"{shop_id}_{cash_id}.csv")
    except Exception as e:
        logging.error(f"Ошибка при создании имени файла: {e}")
        return None


def generate_data(shops=10, cash_per_shop=5):
    try:
        for shop_id in range(1, shops + 1):
            for cash_id in range(1, cash_per_shop + 1):
                filename = generate_filename(shop_id, cash_id)

                if not filename:
                    logging.error(f"Ошибка при создании файла для магазина {shop_id}, касса {cash_id}")
                    continue

                try:
                    with open(filename, 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        # Добавляем заголовки столбцов
                        writer.writerow(["doc_id", "item", "category", "amount", "price", "discount", "shop_num", "cash_num"])

                        for _ in range(random.randint(50, 150)):  # Генерируем от 50 до 150 чеков
                            doc_id = f"{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(1000, 9999)}"
                            category = random.choice(CATEGORIES)
                            item = random.choice(ITEMS[category])
                            amount = random.randint(1, 10)
                            price = round(random.uniform(10.0, 100.0), 2)
                            discount = round(random.uniform(0.0, price), 2)
                            writer.writerow([doc_id, item, category, amount, price, discount, shop_id, cash_id])
                except Exception as e:
                    logging.error(f"Ошибка при записи в файл {filename}: {e}")
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
