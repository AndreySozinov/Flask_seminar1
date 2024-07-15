from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def shop_page():
    return render_template('shop.html')


@app.route('/clothes/')
def page_clothes():
    return render_template('clothes.html')


@app.route('/shoes/')
def page_shoes():
    return render_template('shoes.html')


@app.route('/jacket/')
def page_jacket():
    return render_template('jacket.html')


if __name__ == '__main__':
    app.run()
