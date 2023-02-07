from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def start():
    return "Миссия Колонизация Марса"

@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"

@app.route("/promotion")
def promotion():
    return "Человечество вырастает из детства.</br>" \
           "Человечеству мала одна планета.</br>" \
           "Мы сделаем обитаемыми безжизненные пока планеты.</br>" \
           "И начнем с Марса!</br>" \
           "Присоединяйся!</br>"


@app.route("/image_mars")
def image_mars():
    return f"""
            <!doctype html>
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                </head>
                <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for("static", filename="img/mars.jpg")}">
                </body>
            </html>
            """


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')