def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if plate has between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False
    
    # Check if first two characters are letters
    if not s[0:2].isalpha():
        return False
    
    # Check for presence of numbers in the middle
    found_number = False
    for i, char in enumerate(s):
        if char.isdigit():
            found_number = True
            # First number cannot be '0'
            if char == '0' and not any(s[j].isdigit() for j in range(i)):
                return False
        # After finding a number, all subsequent characters must be numbers
        elif found_number:
            return False
    
    # Check for periods, spaces, or punctuation marks
    if not s.isalnum():
        return False
    
    return True


main()