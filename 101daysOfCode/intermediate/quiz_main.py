from quiz_data import question_data
from quiz_questionModel import Question
from quiz_engine import QuizEngine
import requests
from html import unescape


questions = []
source = input("Would you like to get questions from local file or online database? type 'online or 'local': ")
if source == 'local':
    # LOAD QUESTIONS FROM LOCAL FILE
    for qd in question_data:
        q = Question(qd["text"], qd["answer"])
        questions.append(q)
else:
    # LOAD QUESTIONS FROM ONLINE TRIVIA DATABASE
    url = 'https://opentdb.com/api.php?amount=5&difficulty=easy&type=boolean'

    # Fetching JSON data from the URL
    response = requests.get(url)

    # Checking if the request was successful (status code 200)
    if response.status_code == 200:
        # Parsing the JSON data
        json_data = response.json()
        for qd in json_data["results"]:
            q = Question(unescape(qd["question"]), unescape(qd["correct_answer"]))
            questions.append(q)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

quiz = QuizEngine(questions)

while quiz.hasQuestionsLeft():
    quiz.nextQuestion()

print(f"\nYour final score is {quiz.score}/{quiz.question_number}. You got "
      f"{(quiz.score/quiz.question_number*100):.2f}% of answers right.")
print("Bye bye")
