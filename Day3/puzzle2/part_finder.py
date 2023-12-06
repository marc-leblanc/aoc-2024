def process_data(file_path):
    my_dict = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Initialize the grid to match the original file contents
        grid = [list(line.strip()) for line in lines]
        print(f"Lines {len(lines)}") 
        # Function to mark special characters touching numbers
        def mark_special_characters(row_num, start, end):
            #print(f"{row_num}-{start}-{end}")
            hit=0
            #print(f"row: {row_num}, lines: {len(lines)}")
            for r in range(max(0, row_num - 1), min(len(lines), row_num+2), 1):
                print(f"row#: {r}")

                for c in range(max(0, start - 1), min(len(grid[r]),end +2 ), 1):
                    #print(f"Character: {grid[r][c]} Row: {r + 1} Position: {c}")
                    if grid[r][c] == '*':
                        print(f"Special Character: {grid[r][c]}, Row: {r + 1}, Position: {c}")
                        hit =f"{r},{c}"
            return hit

        # Iterate over each line in the file
        totsum=0
        for line_number, line in enumerate(lines, start=1):
            row = list(line.strip())
            original_line = "".join(row)
            #print(f"Row {line_number}: {original_line}")
            idx = 0
            while idx < len(row):
                char = row[idx]

                # Check for numbers
                if char.isdigit():
                    start_pos = idx
                    end_pos = idx
                    while end_pos + 1 < len(row) and row[end_pos + 1].isdigit():
                        end_pos += 1
                    number = "".join(row[start_pos:end_pos + 1])
                    #print(f"Number: {number}, Row: {line_number}, Start Position: {start_pos}, End Position: {end_pos}")

                    # Mark special characters touching the number
                    addnum=0
                    print(f"Looking for characters around {number} at [{line_number}][{start_pos}]-[{end_pos}]")
                    if mark_special_characters(line_number-1, start_pos, end_pos):
                        print("searching: found")
                        asterisk = mark_special_characters(line_number-1, start_pos, end_pos)

                        # Check if the element exists
                        if asterisk not in my_dict:
                            # Element does not exist, so add it with val1
                            my_dict[asterisk] = {
                            "val1": number
                            }
                        else:
                            # Element already exists, so update val2
                            my_dict[asterisk]["val2"] = number
                            totsum+= int(my_dict[asterisk]["val1"]) * int(my_dict[asterisk]["val2"])
                    else:
                        print("searching: none found")

                    
                    idx = end_pos + 1

                idx += 1
        print(totsum)

if __name__ == "__main__":
    try:
        file_name = "input.txt"  # Replace with your file name
        process_data(file_name)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
