import schedule
import time
from generate_data import generate_data
from load_data import load_data


def job():
    # Генерируем данные
    generate_data()

    #