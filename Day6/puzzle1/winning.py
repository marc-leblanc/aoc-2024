def calculate1(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    times = [int(val) for val in lines[0].strip().split()[1:]]
    distances = [int(val) for val in lines[1].strip().split()[1:]]

    winways = 1
    pos = 0

    for timeval in times:
        tot_wins = 0
        pos += 1
        ms = timeval
        dist = distances[pos - 1]

        for i in range(ms + 1):
            win = i * (ms - i)

            if win > dist:
                tot_wins += 1

        winways *= tot_wins

    return winways

# Specify the path to your data file
file_path = "input.txt"

# Call the calculate1() function with the file path
result = calculate1(file_path)
print(result)
