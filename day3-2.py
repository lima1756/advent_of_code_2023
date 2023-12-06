def validate_number(line, position, width):
    start = position
    end = position
    curr = line[start]
    while curr.isdigit() and (start-1) >= 0:
        start -= 1
        curr = line[start]
    if curr.isdigit() and start == 0:
        start -= 1
    curr = line[end]
    while curr.isdigit() and (end+1) < width:
        end += 1
        curr = line[end]

    if curr.isdigit() and end+1 == width:
        end += 1
    
    return int(line[start+1:end])
    
with open("./input/day3.txt", "r") as file:
    total = 0
    data = file.read().splitlines()
    height = len(data)
    width = len(data[0])
    for i in range(height):
        for j in range(width):
            if data[i][j] == "*":
                numbers = []
                if i-1 >= 0 and j-1 >= 0 and data[i-1][j-1].isdigit():
                    numbers.append(validate_number(data[i-1], j-1, width))
                if i-1 >= 0 and data[i-1][j].isdigit() and (j-1 < 0 or (j-1 >= 0 and not data[i-1][j-1].isdigit())):
                    numbers.append(validate_number(data[i-1], j, width))
                if i-1 >= 0 and j+1 < width and data[i-1][j+1].isdigit() and not data[i-1][j].isdigit():
                    numbers.append(validate_number(data[i-1], j+1, width))
                if j-1 >= 0 and data[i][j-1].isdigit():
                    numbers.append(validate_number(data[i], j-1, width))
                if j+1 < width and data[i][j+1].isdigit():
                    numbers.append(validate_number(data[i], j+1, width))
                if i+1 < width and j-1 >= 0 and data[i+1][j-1].isdigit():
                    numbers.append(validate_number(data[i+1], j-1, width))
                if i+1 < width and data[i+1][j].isdigit() and (j-1 < 0 or (j-1 >= 0 and not data[i+1][j-1].isdigit())):
                    numbers.append(validate_number(data[i+1], j, width))
                if i+1 < width and j+1 < width and data[i+1][j+1].isdigit() and not data[i+1][j].isdigit():
                    numbers.append(validate_number(data[i+1], j+1, width))
                if len(numbers) == 2:
                    total += (numbers[0] * numbers[1])
    print(total)
    