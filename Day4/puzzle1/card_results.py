# Initialize empty arrays for the two sets of numbers
set1_numbers = []
set2_numbers = []

# Read input data from the file "sample.txt"
with open("input.txt", "r") as file:
    lines = file.readlines()

# Process each line
for line in lines:
    # Split the line by ":"
    parts = line.split(':')
    
    # Extract the card name (part 0) and the two sets of numbers (part 1)
    card_name = parts[0].strip()
    numbers = parts[1].strip().split('|')
    
    # Split and append numbers from set 1 to the set1_numbers array
    set1_numbers.append([int(x) for x in numbers[0].strip().split()])
    
    # Split and append numbers from set 2 to the set2_numbers array
    set2_numbers.append([int(x) for x in numbers[1].strip().split()])

# Initialize an array to store the count of matches per card
matches_per_card = []

# Compare set1 and set2 for each card and count the matches
for set1, set2 in zip(set1_numbers, set2_numbers):
    # Use set intersection to find the common elements between set1 and set2
    common_elements = set(set1) & set(set2)
    
    # Append the count of common elements to the matches_per_card array
    matches_per_card.append(len(common_elements))

# Print the results
total_points = 0;
for i, (set1, set2, matches) in enumerate(zip(set1_numbers, set2_numbers, matches_per_card), start=1):
    print(f"Card {i} - Set 1: {set1}")
    print(f"Card {i} - Set 2: {set2}")
    print(f"Card {i} - Matches: {matches} common element(s)")
    if matches > 0:
        total_points += 2**(matches -1)
print(f"Total Points: {total_points}")