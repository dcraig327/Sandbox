from question_model import Question


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.questions_list = question_list
        self.score = 0

    def next_question(self):
        if self.question_number > len(self.questions_list):
            print("At end of quiz")
            return
        answer = self.questions_list[self.question_number].answer
        question = self.questions_list[self.question_number].text
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {question}. ("
                            f"True/False): ")
        self.check_answer(user_answer, answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            print('Correct!')
            self.score += 1
        else:
            print(f'Incorrect. The correct answer was: {answer}.')
        print(f"Your score: {self.score}/{self.question_number}\n")
