def main():
    variable = input("Variable: ")  # Prompt the user for input
    print(snake_convert(variable))  # Convert the input to snake_case and print it

def snake_convert(camel):
    snake = ""  # Initialize an empty string to build the snake_case result
    for letter in camel:
        if str(letter).isupper():  # Check if the letter is uppercase
            converted_letter = "_" + letter.lower()  # Convert to lowercase and add an underscore
            snake += converted_letter  # Append the converted letter to the result
        else:
            snake += letter  # Append the letter as is to the result
    return snake  # Return the final snake_case string

main()