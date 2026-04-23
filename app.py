from flask import Flask, render_template, request

from m import check_password

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    result = None

    if request.method == "POST":
        password = request.form.get("password", "")
        result = check_password(password)

    return render_template("index.html", password=password, result=result)


if __name__ == "__main__":
    app.run(debug=True)
