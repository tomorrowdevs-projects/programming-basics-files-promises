'''The project allows users to analyze the frequency of letters in a given text or document.    
The program will read input from the user, analyze the frequency of each letter (both uppercase and lowercase), 
and present the results in a visually appealing format.'''

def analyze_frequency(text, array, letters, counter):
    uppertext = text.upper()
    for letter in uppertext:
        if letter in letters:
            if letter not in array:
                array.append(letter)
                counter += 1
    return counter

def main():
    array = []
    text = input("Please input a text: ")
    counter = 0
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(analyze_frequency(text, array, letters, counter))

if __name__ == '__main__':
    main()