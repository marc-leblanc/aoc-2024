use std::fs::File;
use std::io::{self, BufRead};
use regex::Regex;

fn main() -> std::io::Result<()> {
    // Create a regex pattern to match numbers
    let re = Regex::new(r"\d+").unwrap();

    // Open the file for reading (you can change "your_file.txt" to your file's path)
    let file = File::open("./input.txt")?;

    // Create a buffer to store the contents
    let reader = io::BufReader::new(file);


    let mut total_sum = 0;  // Initialize a total sum variable

    for line in reader.lines() {
        let line = line?;
        let mut combined_number = String::new();  // Initialize a string to store combined numbers

        for mat in re.find_iter(&line) {
            combined_number.push_str(mat.as_str());  // Concatenate each number as a string
        }

        // If there are at least two digits, combine the first and last digits
        if combined_number.len() >= 2 {
            let first_digit = combined_number.chars().next().unwrap();
            let last_digit = combined_number.chars().last().unwrap();
            let two_digit_number = format!("{}{}", first_digit, last_digit);

            // Parse the two-digit number as an integer
            if let Ok(number) = two_digit_number.parse::<i32>() {
                // Print the combined two-digit number for the current line
                println!("Combined Two-Digit Number for line: {}", number);

                // Add the combined two-digit number to the total sum
                total_sum += number;
            }
        } else if let Ok(number) = combined_number.parse::<i32>() {
            // If there is only one digit, treat it as the same number twice
            // and add it to the total sum
            println!("Combined Two-Digit Number for line: {}", number);
            total_sum += number * 11;
        }
    }

    // Print the total combined sum of all the two-digit numbers in the file
    println!("Total Combined Sum: {}", total_sum);


    Ok(())
}