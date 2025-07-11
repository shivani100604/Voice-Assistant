import random

def get_random_fact():
    facts = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
        "Octopuses have three hearts and blue blood.",
        "Bananas are berries, but strawberries are not.",
        "India is the world's largest democracy by population.",
        "Sharks are older than trees.",
        "The Taj Mahal appears pink in the morning, white in the afternoon, and golden at night."
    ]
    return "📘 Fact: " + random.choice(facts)
