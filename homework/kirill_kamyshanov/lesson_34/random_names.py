from time import sleep

from faker import Faker
import requests

fake = Faker()

while True:
    requests.get("https://www.google.com")
    sleep(1)
    print("Случайное имя:", fake.name())
