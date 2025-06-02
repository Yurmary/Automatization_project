import csv
from datetime import datetime
import random
import os

# Список категорий и товаров
CATEGORIES = ['бытовая химия', 'текстиль', 'посуда']
ITEMS = {
    'бытовая химия': ['гель для стирки', 'порошок', 'средство для мытья посуды'],
    'текстиль': ['полотенца', 'наволочки', 'простыни'],
    'посуда': ['кастрюля', 'сковорода', 'тарелки']
}


def generate_filename(shop_id, cash_id):
    return f"data/{shop_id}_{cash_id}.csv"


def generate_data(shops=10, cash_per_shop=5):
    for shop_id in range(1, shops + 1):
        for cash_id in range(1, cash_per_shop + 1):
            filename = generate_filename(shop_id, cash_id)

            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['doc_id', 'item', 'category', 'amount', 'price', 'discount'])

                for _ in range(random.randint(50, 150)):  # Генерируем от 50 до 150 чеков
                    doc_id = f"{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(1000, 9999)}"
                    category = random.choice(CATEGORIES)
                    item = random.choice(ITEMS[category])
                    amount = random.randint(1, 5)
                    price = round(random.uniform(100, 1000), 2)
                    discount = round(random.uniform(0, price * 0.3), 2)

                    writer.writerow([doc_id, item, category, amount, price, discount])


if __name__ == "__main__":
    generate_data()
