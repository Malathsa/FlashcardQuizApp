from os import name
import random

def display_flashcards(flashcards):
    print("\nFlashcards:")
    for i, (question, answer) in enumerate(flashcards.items(), start=1):
        print(f"{i}. {question}")

def quiz_user(flashcards):
    questions = list(flashcards.keys())
    random.shuffle(questions)
    score = 0

    for question in questions:
        answer = input(f"\nWhat is the answer to: '{question}'? ")
        if answer.strip().lower() == flashcards[question].strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: '{flashcards[question]}'")

    print(f"\nYour final score: {score}/{len(flashcards)}")

def main():
    flashcards = {}
    print("Welcome to the Flashcard Quiz App!")
    
    while True:
        action = input("\nWould you like to (1) Add a flashcard or (2) Quiz yourself? (q to quit): ")
        if action == '1':
            question = input("Enter the question: ")
            answer = input("Enter the answer: ")
            flashcards[question] = answer
            print("Flashcard added!")
        elif action == '2':
            if not flashcards:
                print("No flashcards available. Please add some first.")
            else:
                quiz_user(flashcards)
        elif action.lower() == 'q':
            print("Exiting the Flashcard Quiz App. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()