def main():
    text = input("Enter a text: ")
    result = remove_vowels(text)
    print(result)

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

if __name__ == "__main__":
    main()