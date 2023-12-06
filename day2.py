import re

LIMIT_RED = 12
LIMIT_GREEN = 13
LIMIT_BLUE = 14

with open("./input/day2.txt", "r") as file:
    total = 0

    data = file.read().splitlines()
    for i in range(len(data)):
        line = data[i]
        line = line[line.find(":")+1:]
        games = line.split(";")
        # === Part 1
        # valid = True
        # === Part 2
        r = 0
        g = 0
        b = 0
        for game in games:
            colors = re.findall(r"\d+ [(green)|(red)|(blue)]", game)
            for color_count in colors:
                [number, color] = color_count.split(" ")
                number = int(number)
                # === Part 1
                # if ((color == "r" and number > LIMIT_RED) or 
                #     (color == "g" and number > LIMIT_GREEN) or 
                #     (color == "b" and number > LIMIT_BLUE)):
                #     valid = False
                #     break
                # === Part 2
                if color == "r" and number > r:
                    r = number
                if color == "g" and number > g:
                    g = number
                if color == "b" and number > b:
                    b = number
        # === Part 1
        # if valid:
        #     total += (i+1)
        # === Part 2
        total += (r*g*b)
        
        
    print(total)