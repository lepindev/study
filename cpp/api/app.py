# -*- coding: windows-1251 -*-
from flask import Flask, jsonify
import random

app = Flask(__name__)

# Список вопросов
questions = [
    {"question": "Какое научное название у панды?", "answer": "Ailuropoda melanoleuca"},
    {"question": "Кто был первым президентом США?", "answer": "Джордж Вашингтон"},
    {"question": "Какой год был основан Google?", "answer": "1998"},
    {"question": "Кто написал роман \"Война и мир\"?", "answer": "Лев Толстой"}
]

# Маршрут API, который возвращает случайный вопрос из списка
@app.route('/api/question/random')
def random_question():
    return jsonify(random.choice(questions))

if __name__ == '__main__':
    app.run(debug=True)
