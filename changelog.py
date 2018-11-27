import json

with open('cards.json') as f:
    cards = json.load(f)

with open('columns.json') as f:
    columns = json.load(f)

print(columns["name"] + " Changelog:")

index = 0
for column in cards:
    print(columns["columns"][index]["name"] + ":")

    cardindex = 0
    for card in column["cards"]:
        print(card["name"])

        cardindex += 1

    if (cardindex == 0):
        print("[None]")
    
    if (index != len(cards) - 1):
        print("\n---\n")
    else:
        print("\n")

    index += 1