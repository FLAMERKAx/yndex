from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/<title>")
@app.route("/index/<title>")
def index(title):
    return render_template('index.html', title=title, prof="None")


@app.route("/training/<prof>")
def training(prof):
    if prof == "Инженер" or prof == "Строитель":
        return render_template('index.html', title=prof, prof="Инженер",
                               img=f"{url_for('static', filename='img/scientist.png')}")
    else:
        return render_template('index.html', title=prof, prof="Ученый",
                               img=f"{url_for('static', filename='img/engineer.png')}")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
