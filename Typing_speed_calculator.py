from time import time
import random as r
from rich.console import Console

console = Console()

def mistake(par, userinput):
    error = 0
    for i in range(len(par)):
        try:
            if par[i] != userinput[i]:
                error += 1
        except:
            error += 1
    return error

def speed(start, end, userinput):
    delay = end - start
    roundoff = round(delay, 2)
    speed = len(userinput) / roundoff
    return round(speed * 60)

while True:
    choice = 0
    choice = int(input("ENTER 0 TO START !"))
    if choice != 0: break
    test = [
    "apple", "banana", "orange", "grape", "pineapple", "kiwi", "strawberry", "blueberry", "watermelon", "mango",
    "carrot", "potato", "tomato", "cucumber", "broccoli", "lettuce", "spinach", "onion", "garlic", "pepper",
    "soccer", "basketball", "tennis", "volleyball", "football", "baseball", "golf", "swimming", "cycling", "boxing",
    "knowledge", "information", "education", "learning", "wisdom", "intelligence", "curiosity", "insight", "awareness", "understanding",
    "biology", "chemistry", "physics", "astronomy", "geology", "meteorology", "ecology", "genetics", "botany", "zoology",
    "noun", "verb", "adjective", "adverb", "preposition", "conjunction", "pronoun", "article", "subject", "predicate",
    "city", "town", "village", "country", "continent", "ocean", "mountain", "river", "lake", "island",
    "USA", "Canada", "Australia", "UK", "France", "Germany", "China", "Japan", "Brazil", "India",
    "computer", "internet", "technology", "space", "universe", "history", "culture", "language", "art", "music"
    ]

    test1 = ' '.join(r.choices(test, k=15))
    console.print("*****TYPING SPEED*****", style="bold magenta")
    console.print("TYPE THE TEXT BELOW :\n", test1, style="bold cyan")
    print("\n")
    time1 = time()
    testInput = input("START! \n")
    time2 = time()
    console.print("SPEED : ", speed(time1, time2, testInput), "WPM", style="bold green")
    console.print("ERROR : ", mistake(test1, testInput))