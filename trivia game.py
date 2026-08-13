import random

question_1 = {
    'Question':'Which of the following is not a primary color ?',
    'Options': {'A': 'Green', 'B': 'Blue', 'C': 'Red', 'D': 'Purple'},
    'Correct Answer': 'D'
}

question_2 = {
    'Question':'What is the capital of Nigeria ?',
    'Options': {'A': 'Lagos', 'B': 'Abuja', 'C': 'Calabar', 'D': 'Kano'},
    'Correct Answer': 'B'
}

question_3 = {
    'Question':'What is the color of the ocean ?',
    'Options': {'A': 'Blue', 'B': 'Green', 'C': 'Red', 'D': 'Purple'},
    'Correct Answer': 'A'
}

question_4 = {
    'Question':'Which of the following is a farming tool',
    'Options': {'A': 'Scissors', 'B': 'Tape rule', 'C': 'Hoe', 'D': 'Hammer'},
    'Correct Answer': 'C'
}

question_bank = [question_1, question_2, question_3, question_4]
selected_questions = random.sample(question_bank, 4)
score = 0

for question in selected_questions:
    print(question ['Question'])
    print(f"A: {question['Options']['A']}")
    print(f"B: {question['Options']['B']}")
    print(f"C: {question['Options']['C']}")
    print(f"D: {question['Options']['D']}")

    while True:
        player_choice = input('Pick an option:') .strip().upper()
        if player_choice in question['Options']:
            break
        else:
            print ('Invalid choice. Try again') 

    if player_choice == question ['Correct Answer']:
        print ('Correct Answer') 
        score += 1
    else:
        print (f'Wrong ! The correct answer was {question["Correct Answer"]}') 

print (f' You scored {score} out of {len(selected_questions)}')
        