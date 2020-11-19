import random
import shelve

class Quiz:
    """Zarządzanie tworzeniem Quizów."""
    def __init__(self, quiz_topic):
        """Inicjalizacja quizu."""
        self.get_data_quiz(quiz_topic)

    def get_data_quiz(self, quiz_topic):
        """Pobranie pytań do quizu."""
        with shelve.open('quiz/mydata_quiz') as shelfFile:
            questions = shelfFile[quiz_topic]
        return questions, len(questions)

    def generate_quiz_files(self, num_of_quizes):
        """Utworzenie plików z quizami i odpowiedziami."""
        for quiz_num in range(num_of_quizes):
            create_answer_files()
            create_quiz_file()



generate_quiz_files(35)

for quiz_num in range(35):
    #Create the quiz and answer key files.
    quiz_answ_file_name = 'quiz/capquizansw' + str(quiz_num+1) + '.txt'
    answer_file = open(quiz_answ_file_name, 'w')

    quiz_file_name = 'quiz/capquiz' + str(quiz_num+1) + '.txt'
    #TOD: Write out the header for the quiz.
    quiz_file_header = 'State Capitals Quiz (Form nr ' + str(quiz_num+1) + ')' 
    with open(quiz_file_name, 'w') as quiz_file:
        quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quiz_file.write((' ' * 20) + quiz_file_header)
        quiz_file.write('\n\n')

        #TOD: Shuffle the order of the states.
        states = list(questions.keys())
        random.shuffle(states)

        #TOD: Loop through all 50 states, making a question for each.
        for question_num in range(num_of_questions):
            correct_answer = questions[states[question_num]]
            wrong_answers = list(questions.values())
            del wrong_answers[wrong_answers.index(correct_answer)]
            wrong_answers = random.sample(wrong_answers, 3)
            answers_options = wrong_answers + [correct_answer]
            random.shuffle(answers_options)

            # Write the question and the answer options to the quiz file.
            question_header = str(question_num+1) + '. What is the capital of ' + str(states[question_num]) + '?\n\n'
            quiz_file.write(question_header)
            for quest_option in range(4):
                quiz_file.write(f"  {'ABCD'[quest_option]}. {answers_options[quest_option]}\n")
                quiz_file.write('\n')

            #Write answer to another file
            answer_letter = 'ABCD'[answers_options.index(correct_answer)]
            answer_to_file = str(question_num + 1) + '. ' + answer_letter + '\n'
            answer_file.write(answer_to_file)

    answer_file.close()