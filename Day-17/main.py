from question_model import Question
from data import question_bank
from quiz_brain import QuizBrain

new_QB_DB = question_bank
question_bank = []
for question in new_QB_DB:
    new_q = Question(question['question'],question['correct_answer'])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.check_answer()
    quiz.result()

