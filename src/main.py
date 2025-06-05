#!/usr/bin/env python3
from generate_data import generate_data
from load_data import load_data
import logging

import os

log_dir = '/Users/mary/Pycharm/Projects/Automatization_project/logs'
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, 'load_data.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info('Скрипт запущен')

def job():
    logging.info("Начало выполнения задачи")
    try:
        generate_data()
        load_data()
        logging.info("Задача выполнена успешно")
    except Exception as e:
        logging.error(f"Ошибка выполнения задачи: {e}")

if __name__ == "__main__":
    job()