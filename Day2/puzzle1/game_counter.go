package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	// Replace "sample.txt" with the path to the file you want to open.
	filePath := "input.txt"

	// Open the file for reading.
	file, err := os.Open(filePath)
	if err != nil {
		fmt.Printf("Error opening file: %v\n", err)
		return
	}
	defer file.Close()

	// Create a map to store color mappings with lowercase keys.
	colorMap := map[string]int{
		"red":   12,
		"green": 13,
		"blue":  14,
	}

	// Create a bufio.Scanner to read lines from the file.
	scanner := bufio.NewScanner(file)

	// Initialize a variable to store the sum of game numbers.
	totalGameNumber := 0

	// Iterate over each line and process the index and sets.
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Split(line, ":")
		if len(parts) != 2 {
			fmt.Printf("Invalid line format: %s\n", line)
			continue
		}

		index := parts[0]
		sets := strings.Split(parts[1], ";")

		fmt.Printf("Index: %s\n", index)
		isGamePossible := true

		// Extract the game number from the index.
		gameNumberStr := strings.TrimPrefix(index, "Game ")
		gameNumber, err := strconv.Atoi(gameNumberStr)
		if err != nil {
			fmt.Printf("Invalid game number format: %s\n", gameNumberStr)
			continue
		}

		// Add the game number to the total if the game is possible.
		for i, set := range sets {
			set = strings.TrimSpace(set)
			if set != "" {
				items := strings.Split(set, ",")
				colorCounts := make(map[string]int)

				for _, item := range items {
					item = strings.TrimSpace(item)
					parts := strings.Split(item, " ")
					if len(parts) != 2 {
						fmt.Printf("Invalid item format: %s\n", item)
						continue
					}
					color := strings.ToLower(parts[1])   // Convert color to lowercase
					count, err := strconv.Atoi(parts[0]) // Convert count to integer
					if err != nil {
						fmt.Printf("Invalid count format: %s\n", parts[0])
						continue
					}
					colorCounts[color] += count
				}

				fmt.Printf("Set %d:\n", i+1)
				for color, setCount := range colorCounts {
					mapCount, exists := colorMap[color]
					fmt.Printf("  %s - %d - Map Count: %d\n", color, setCount, mapCount)
					if exists && setCount > mapCount {
						isGamePossible = false
					}
				}
			}
		}

		if isGamePossible {
			fmt.Printf("Game %s: Possible\n", index)
			totalGameNumber += gameNumber // Add the game number to the total
		} else {
			fmt.Printf("Game %s: Not Possible\n", index)
		}
	}

	// Print the total game number for all possible games.
	fmt.Printf("Total Game Number for Possible Games: %d\n", totalGameNumber)

	// Check for scanner errors (e.g., bad file format).
	if err := scanner.Err(); err != nil {
		fmt.Printf("Error reading file: %v\n", err)
	}
}
