# -*- coding: windows-1251 -*-
from flask import Flask, jsonify
import random

app = Flask(__name__)

# ������ ��������
questions = [
    {"question": "����� ������� �������� � �����?", "answer": "Ailuropoda melanoleuca"},
    {"question": "��� ��� ������ ����������� ���?", "answer": "������ ���������"},
    {"question": "����� ��� ��� ������� Google?", "answer": "1998"},
    {"question": "��� ������� ����� \"����� � ���\"?", "answer": "��� �������"}
]

# ������� API, ������� ���������� ��������� ������ �� ������
@app.route('/api/question/random')
def random_question():
    return jsonify(random.choice(questions))

if __name__ == '__main__':
    app.run(debug=True)
