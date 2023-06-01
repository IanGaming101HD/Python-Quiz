import json
import random

points = 0
question_num = 1

data = open('questions.json')
questions = json.load(data)

def main():
    global points, question_num, questions

    while True:
        dictionary = random.choice(questions)
        question = dictionary['question']
        correct_answer = dictionary['choices']['correct']
        choices = dictionary['choices']['incorrect'] + [dictionary['choices']['correct']]
        random.shuffle(choices)
        a = choices[0]
        b = choices[1]
        c = choices[2]
        d = choices[3]

        while True:
            userInput = input(f'Question {question_num}\n{question}\nPlease pick one of the choices below!\n\nA) {a}\n\nB) {b}\n\nC) {c}\n\nD) {d}\n\n> ').lower()

            if userInput in choices or userInput in ['a', 'b', 'c', 'd']:
                correct_choice = None

                if a == correct_answer:
                    correct_choice = 'a'
                elif b == correct_answer:
                    correct_choice = 'b'
                elif c == correct_answer:
                    correct_choice = 'c'
                elif d == correct_answer:
                    correct_choice = 'd'

                if userInput == correct_choice or userInput == correct_answer.lower():
                    print('Correct!')
                    points += 1
                else:
                    print('Incorrect!')
                question_num += 1
                try:
                    questions.remove(dictionary)
                except:
                    print('Not enough questions!')
                break
            else:
                print('Please enter a valid option!')
        if question_num == 11:
            print(f'You got {points} out of 10 correct!')
            break
main()