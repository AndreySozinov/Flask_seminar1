import datetime

from flask import Flask
from flask import render_template

app = Flask(__name__)
index = 'my_html_page.html'
students = 'students.html'


@app.route('/')
def hello_world():
    return 'Hello fake World!'


@app.route('/about')
def about():
    return 'about'


@app.route('/contact')
def contact():
    return 'contact'


@app.route('/<int:num1>/<int:num2>')
def my_sum(num1: int, num2: int):
    return f'{num1} + {num2} = {num1 + num2}'


@app.route('/<string>')
def str_length(string):
    return f'Длина строки: {len(string)} символов.'


@app.route('/index')
def html_page():
    return render_template(index)


@app.route('/students')
def students_info():
    context = [{
        "Имя": "Андрей",
        "Фамилия": "Петров",
        "Возраст": 28,
        "Балл": 4.71},
        {
            "Имя": "Сергей",
            "Фамилия": "Васильев",
            "Возраст": 25,
            "Балл": 4.24},
        {
            "Имя": "Игорь",
            "Фамилия": "Ветров",
            "Возраст": 26,
            "Балл": 3.28},
        {
            "Имя": "Степан",
            "Фамилия": "Смирнов",
            "Возраст": 21,
            "Балл": 5.00}]
    return render_template(students, context=context)


@app.route('/news/')
def show_news():
    news = [{
        'heading': 'Event1',
        'text': 'Lorem ipsum',
        'date': f'{datetime.date.today()}'},
        {'heading': 'Event2',
         'text': 'Quod licet Iovi, non licet bovi.',
         'date': f'{datetime.date.today()}'},
        {'heading': 'Event3',
         'text': 'Per aspera ad astra.',
         'date': f'{datetime.date.today()}'},
        {'heading': 'Event4',
         'text': 'Veni, vidi, vici!',
         'date': f'{datetime.date.today()}'}]
    return render_template('news.html', context=news)


if __name__ == '__main__':
    app.run()
