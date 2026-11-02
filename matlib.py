import random 

subjects = [
    "Shah Rukh Khan",
    "Virat Kohli",
    "Sachin Tendulkar",
    "A Bollywood actor",
    "A famous businessman",
    "A beautiful woman",
    "A police officer",
    "A school teacher",
    "A street food seller",
    "A Delhi auto-rickshaw driver",
    "A cricket player",
    "A rich businessman",
    "A mysterious stranger",
    "A village farmer",
    "A famous YouTuber"
]   

actions = [
    "dances with",
    "rides a horse with",
    "plays cricket with",
    "drinks coffee with",
    "sings a song for",
    "fights with",
    "cooks food for",
    "takes selfies with",
    "runs away from",
    "celebrates a party with",
    "challenges",
    "surprises",
    "teaches dance to",
    "plays football with",
    "buys a gift for"
]

things = [
    "a handsome stranger",
    "a plate of samosas",
    "a group of monkeys",
    "a giant elephant",
    "a mysterious man",
    "at India Gate",
    "inside a shopping mall",
    "on top of a mountain",
    "at Mumbai railway station",
    "inside a five-star hotel",
    "on a cricket ground",
    "at the Taj Mahal",
    "in the middle of a busy road",
    "inside a village house",
    "at Marine Drive"
]

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