import shelve

class Quiz:
    """Zarządzanie tworzeniem Quizów."""
    def __init__(self, quiz_topic, num_of_quizes):
        """Inicjalizacja quizu."""
        self.quiz_topic = quiz_topic
        self.num_of_quizes = num_of_quizes
        self.get_data_quiz()
        for quiz_num in range(num_of_quizes):
            self.create_quiz_files(quiz_num)

    def get_data_quiz(self):
        """Pobranie pytań do quizu."""
        with shelve.open('quiz/mydata_quiz') as shelfFile:
            self.questions = shelfFile[self.quiz_topic]
        self.num_of_questions = len(self.questions)
    
    def create_quiz_files(self, quiz_num):
        """Utworzenie plików dla określonego quizu."""
        quiz_file_name = 'quiz/quiz' + str(quiz_num+1) + '.txt'
