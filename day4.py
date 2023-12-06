import re

with open("./input/day4.txt", "r") as file:
    total = 0
    data = file.read().splitlines()
    cards = [1] * len(data)
    for i in range(len(data)):
        line = data[i]
        line_info = line[line.find(":")+1:]
        points_tuple= line_info.split("|")
        
        card_points = re.split(r"\s+", points_tuple[0].strip())
        winner_points = set(re.split(r"\s+", points_tuple[1].strip()))
        
        n = 0
        for points in card_points:
            if points in winner_points:
                n+=1
        # solution 1
        # if n > 0:
        #     total += 2 ** (n-1)
        # solution 2
        curr = cards[i]
        for j in range(i+1, i+n+1):
            cards[j] += curr
        print(cards)
    # solution 2
    for totalCards in cards:
        total+=totalCards

    print(total)
