#aoc-2024 day 1 part 2 challenge solution
import sys
import re

def computeCalibrationCode():
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', "\\d"]
    regex = re.compile('|'.join(numbers))
    calibrationCode = 0

    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r+') as f:
            lines = f.readlines()
            for i in range(0, len(lines)):
                line = re.findall(regex, lines[i])

                if len(line) > 1:
                    firstDigit = str(line[0])
                    secDigit = str(line[len(line) - 1])

                    if firstDigit.isdigit() is False:
                        firstDigit = getNum(firstDigit)
                    if secDigit.isdigit() is False:
                        secDigit = getNum(secDigit)

                    codeSegment = ''.join([firstDigit, secDigit])
                    calibrationCode += int(codeSegment)
                else:
                    firstDigit = str(line[0])

                    if firstDigit.isdigit is False:
                        firstDigit = getNum(firstDigit)

                    codeSegment = ''.join([line[0], line[0]])
                    calibrationCode += int(codeSegment)
        print(calibrationCode)
        f.close()
    else:
        return
    
def getNum(numStr):
    match numStr:
        case 'one':
            return str(1)
        case 'two':
            return str(2)
        case 'three':
            return str(3)
        case 'four':
            return str(4)
        case 'five':
            return str(5)
        case 'six':
            return str(6)
        case 'seven':
            return str(7)
        case 'eight':
            return str(8)
        case 'nine':
            return str(9)

def main():
    computeCalibrationCode()

main()
