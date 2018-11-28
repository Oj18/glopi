import json
import sys

def make_plain(file):
    with open('/tmp/glopi/cards.json') as f:
        cards = json.load(f)

    with open('/tmp/glopi/columns.json') as f:
        columns = json.load(f)

    if file != "":
        f = open(file, 'w')
        sys.stdout = f

    print(columns["name"] + " Changelog:")

    allcards = []

    for column in cards:
        for card in column["cards"]:
            allcards.append(card)
    
    index = 0

    for column in columns["columns"]:
        print(column["name"] + ":")

        cardindex = 0

        for card in allcards:
            if card["column_id"] == column["id"]:
                print(card["name"])

                cardindex += 1

        if cardindex == 0:
            print("[None]")
    
        if index != len(cards) - 1:
            print("\n---\n")
        else:
            print("\n")

        index += 1
        
    print("Columns: " + str(len(columns)) + " Cards: " + str(len(cards)))

def make_fancy(file):
    with open('/tmp/glopi/cards.json') as f:
        cards = json.load(f)

    with open('/tmp/glopi/columns.json') as f:
        columns = json.load(f)

    if file != "":
        f = open(file, 'w')
        sys.stdout = f
    else:
        print("(You will probably want to save it as it uses markdown)")

    print("# " + columns["name"] + " Changelog:")

    allcards = []

    for column in cards:
        for card in column["cards"]:
            allcards.append(card)
    
    index = 0

    for column in columns["columns"]:
        print("## " + column["name"] + ":")

        cardindex = 0

        for card in allcards:
            if card["column_id"] == column["id"]:
                print("- " + card["name"])

                cardindex += 1

        if cardindex == 0:
            print("- [None]")
    
        print("\n") #just do a new line, as markdown does seperators and titles

        index += 1
    
    print("## Columns: " + str(len(columns)) + " Cards: " + str(len(cards)))