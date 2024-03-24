from random import shuffle


class QuizEngine:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        shuffle(self.question_list)
        self.score = 0

    def nextQuestion(self):
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} Is it "
                            f"true or false? ")
        self.checkAnswer(user_answer)
        self.question_number += 1

    def hasQuestionsLeft(self):
        return self.question_number < len(self.question_list)

    def checkAnswer(self, user_answer):
        if user_answer.lower() == self.question_list[self.question_number].answer.lower():
            self.score += 1
            print("You've got it right!")
        else:
            print("You've got it wrong!")
        print(f"Correct answer: {self.question_list[self.question_number].answer}")
        print(f"Your current score is {self.score}/{self.question_number + 1}")
