class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """Returns True if list have questions otherwise Returns False"""
        return True if self.question_number<len(self.question_list) else False
    def next_question(self):
        "Increments questions and takes answer for the user"
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        return input(f"Q.{self.question_number}: {current_question.text}. (True/False)?: ").lower()

    def check_answer(self):
        "Checks answer and increment total score"
        if self.question_list[self.question_number].answer.lower() ==  self.next_question().lower():
            self.score += 1

    def result(self):
        """Prints Result"""
        print(f"The correct answer is : {self.question_list[self.question_number-1].answer}")
        print(f"Total Score: {self.score}/{self.question_number}")
        print('\n')
        if self.question_number == len(self.question_list):
            print(f"\nYou've Completed the quiz\nYour Final Score: {self.score}/{self.question_number}")




