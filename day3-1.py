def validate_engine(char):
    return char != '.' and not char.isdigit()

def number_next_to_engine(data, x, y, height, width):
    engine = False
    start = y
    end = start
    curr = data[x][end]
    while curr.isdigit() and (end+1) < width:
        if not engine and ((x-1 >= 0 and end-1 >= 0 and validate_engine(data[x-1][end-1])) or 
            (x-1 >= 0 and validate_engine(data[x-1][end])) or 
            (x-1 >= 0 and end+1 < width and validate_engine(data[x-1][end+1])) or 
            (end-1 >= 0 and validate_engine(data[x][end-1])) or 
            (end+1 < width and validate_engine(data[x][end+1])) or 
            (x+1 < height and end-1 >= 0 and validate_engine(data[x+1][end-1])) or
            (x+1 < height and validate_engine(data[x+1][end])) or 
            (x+1 < height and end+1 < width and validate_engine(data[x+1][end+1]))):
            engine = True
        end += 1
        curr = data[x][end]
    if curr.isdigit() and (end + 1) == width:
        end += 1

    return [engine, start, end]
    

with open("./input/day3.txt", "r") as file:
    total = 0

    data = file.read().splitlines()
    height = len(data)
    width = len(data[0])
    for i in range(height):
        j = 0
        while j < width:
            if data[i][j].isdigit():
                should_add, j_start, j_end = number_next_to_engine(data, i, j, height, width)
                if should_add:
                    print(int(data[i][j_start:j_end]))
                    total += int(data[i][j_start:j_end])
                    j = j_end
                else:
                    j += 1
            else: 
                j += 1
                
    print(total)
    
