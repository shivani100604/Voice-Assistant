import random

FACTS = [
    "Honey never spoils, archaeologists found 3000-year-old honey still edible.",
    "Bananas are berries, but strawberries are not.",
    "Sharks existed before trees.",
    "Octopuses have three hearts."
]

def get_random_fact():
    return f" {random.choice(FACTS)}"
