from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form.get('email')

        if email:
            file_path = os.path.join(os.getcwd(), "emails.txt")
            with open(file_path, "a") as f:
                f.write(email + "\n")

    return render_template("coming_soon.html")


@app.route('/<path:anything>')
def block_all(anything):
    return render_template("coming_soon.html")


if __name__ == "__main__":
    app.run()