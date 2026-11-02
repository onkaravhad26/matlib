import random 

subjects = ["shahkrukh khan", 
            "virat kohli",
            "sachin tendulkar",
            "A auto-rikshaw from delhi ",
            "a man in palace",
            "A beautifull women"]

Actions = ["dances with a man",
           "rides on horse",
           "walks on ground",
           "drinks coffee with",
           "plays cricket ",
           "sangs a song"]

things = ["on a fort",
          "on a building",
          "inside a home",
          "a plate of samosa",
          "at ganga ghatt",
          "a handsome man "]

while True :
    subject = random.choice(subjects)
    actions = random.choice(Actions)
    Things = random.choice(things)

    headline = f" Breakiing News: {subject} {actions} {Things}"

    print("\n" + headline)

    user = input("do you want another headline (Yes/No)").strip().lower()

    if user == "no":
        break

print("thanks for using")