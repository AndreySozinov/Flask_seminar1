
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def shop_page():
    return render_template('shop.html')


@app.route('/clothes/')
def page_clothes():
    _clothes = [{'size': ['small clothes', 'medium clothes', 'large clothes']}]
    context = {'title': 'Одежда',
               'clothes': _clothes}
    return render_template('clothes.html', **context)


@app.route('/shoes/')
def page_shoes():
    _shoes = [{'type': ['slippers', 'boots', 'monks']}]
    context = {'title': 'Обувь',
               'shoes': _shoes}
    return render_template('shoes.html', **context)


@app.route('/jacket/')
def page_jacket():
    _jacket = [{'color': ['red color', 'white color', 'black color']}]
    context = {'title': 'Куртки',
               'jacket': _jacket}
    return render_template('jacket.html', **context)


if __name__ == '__main__':
    app.run()
