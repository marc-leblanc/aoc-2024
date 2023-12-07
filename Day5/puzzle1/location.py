# Initialize variables
seed_numbers = []
maps = {}
current_map = None

# Read the file and process lines
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            if current_map is None and line.startswith("seeds:"):
                # Extract seed numbers from the first line
                seed_numbers = list(map(int, line.split()[1:]))
            elif line.endswith(":"):
                current_map = line[:-1]
                maps[current_map] = []
            elif current_map is not None:
                dest_start, src_start, length = map(int, line.split())
                maps[current_map].append((dest_start, src_start, length))

# Initialize the lowest location number to a large value
lowest_location = float('inf')

# Iterate through each seed number
for seed in seed_numbers:
    # Start with the seed number
    current_number = seed
    
    # Iterate through each map category
    for category, mapping in maps.items():
        for dest_start, src_start, length in mapping:
            # Check if the current_number falls within this mapping
            if src_start <= current_number < src_start + length:
                # Calculate the corresponding destination number
                destination_number = dest_start + (current_number - src_start)
                # Update current_number for the next category
                current_number = destination_number
                break  # Exit the inner loop
        
    # Check if the current location is lower than the lowest_location found so far
    if current_number < lowest_location:
        lowest_location = current_number

# Print the lowest location number
print("Lowest Location:", lowest_location)
