numbers = {
    "one": 1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
    "zero":0
}

def is_int(c):
    try:
        return int(c)
    except:
        return -1

def is_letter_number(string):
    for k in numbers.keys():
        if string.startswith(k):
            return numbers[k]
    return -1

with open("./input/day1.txt", "r") as file:
    data = file.read().splitlines()
    total = 0
    for line in data:
        curr = 0
        forward = True
        backward = True
        for i in range(len(line)):
            if forward:
                char = line[i]
                number = is_int(char)
                if number == -1:
                    number = is_letter_number(line[i:])
                if number >= 0:
                    curr += number*10
                    forward = False
            if backward:
                char = line[len(line)-i-1]
                number = is_int(char)
                if number == -1:
                    number = is_letter_number(line[len(line)-i-1:])
                if number >= 0:
                    curr += number
                    backward = False
            if not forward and not backward:
                break
        total += curr
    print(total)