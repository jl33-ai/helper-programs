import random
import openai
from sudoku import Sudoku

# A valid solved Sudoku grid
EXAMPLE_SUDOKU = [[9, 5, 7, 6, 1, 3, 2, 8, 4], 
                  [4, 8, 3, 2, 5, 7, 1, 9, 6], 
                  [6, 1, 2, 8, 4, 9, 5, 3, 7], 
                  [1, 7, 8, 3, 6, 4, 9, 5, 2], 
                  [5, 2, 4, 9, 7, 1, 3, 6, 8], 
                  [3, 6, 9, 5, 2, 8, 7, 4, 1], 
                  [8, 4, 5, 7, 9, 2, 6, 1, 3], 
                  [2, 9, 1, 4, 3, 6, 8, 7, 5], 
                  [7, 3, 6, 1, 8, 5, 4, 2, 9]]

# OpenAI Key
openai.api_key = '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'

# Call ChatGPT API to interpret difficulty, returns float in interval (0, 1)
def get_difficulty(desired_difficulty):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content" : "You will receive a description of difficulty. You should interpret it this and return ONLY a float value representing the difficulty, with 0 being easiest and 1 being hardest. Your response should be nothing other than the value between 0 and 1. E.g: 'kind of hard' returns 0.7"},
            {"role": "user", "content": desired_difficulty}
        ]
    )
    answer = float(completion.choices[0].message.content)
    print("Interpreted difficulty =", answer)
    return answer

# Call ChatGPT API to Generate Message
def generate_worded_sudoku(puzzle):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content" : "You will receive an incomplete sudoku puzzle in the form of . Your task is to encode it into an english paragraph that could be communicated. Speak like you are a riddler"},     
            {"role": "user", "content": str(puzzle)}
        ]
    )
    return completion.choices[0].message.content

# Generate the legend 
def generate_legend(message, sudoku):
    # Mapping of 1-9 to A-I
    a_to_i = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

    # Secret message to be encoded
    letters = list(message)

    # Alphabet set to be used for random letter selection
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ_')

    # Index to keep track of the current letter in the message
    letter_idx = 0

    # Open the legend file for writing
    with open("sudoku_legend.txt", 'w') as file:
        file.write(f"🧩 SUDOKU LEGEND TO DECODE 💻\n\n+================================+\n\n")
        for row in range(9):
            for cell in range(9):
                # Copy the alphabet set
                current_alphabet = alphabet.copy()
                
                # Get the current letter if there are any left, otherwise use 'X'
                letter = letters[letter_idx] if letter_idx < len(letters) else 'X'
                
                # Remove the current letter from the alphabet set
                current_alphabet.discard(letter)

                # Update the index for the next letter in the message
                if letter_idx < len(letters):
                    letter_idx += 1

                num = sudoku[row][cell]
                file.write(f"⇲ {a_to_i[row]}{cell+1}: \n")

                # Write the legend for the current cell
                for i in range(1, 10):
                    random_letter = random.choice(list(current_alphabet))
                    current_alphabet.discard(random_letter)
                    if num == i:
                        file.write(f"{i}='{letter}'    ")
                    else:
                        file.write(f"{i}='{random_letter}'    ")
                file.write('\n\n')

def main():
    desired_difficulty = input("Describe how difficult you would like your Sudoku (key) to be: ")

    # Generate a Sudoku puzzle
    puzzle = Sudoku(3).difficulty(get_difficulty(desired_difficulty))

    while True:
        message = input("What message would you like to encrypt (MAX 81 CHARACTERS)")
        if len(message) <= 81:
            print("Valid message")
            break
        else:
            print("This message is too long, try again")

    generate_legend(message, puzzle.solve().board)
    
if __name__ == "__main__":
    main()