from flask import Flask, render_template

app = Flask(__name__)


@app.route('/about/')
def page_about():
    return render_template('about.html')


@app.route('/contacts/')
def page_contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run()
