from flask import (Flask,
                   url_for,
                   request,
                   render_template,
                   redirect)

from models import Human

app = Flask(__name__)
USERS = [Human("Ana", 18, "w"),
         Human("Yra", 15, "m"),
         Human("Vasa", 28, "m"),
         Human("Olya", 58, "w"),
         Human("Ira", 12, "w"),
         Human("Anry", 48, "m"), ]


@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    return render_template("home.html", data=name)


@app.route("/users")
def get_user_list():
    return render_template("users.html", users=USERS)


@app.route("/user", methods=['GET', 'POST'])
def create_user():
    if request.method == "GET":
        return render_template("create_user.html")

    name = request.form['username']
    age = request.form['age']
    sex = request.form['sex']
    user = Human(name, age, sex)
    USERS.append(user)
    return redirect( url_for("get_user_list"))


@app.route("/api/user", methods=['POST'])
@app.route("/api/user/<int:user_id>", methods=['GET', 'PUT'])
def get_user_api(user_id=None):
    if request.method == "POST":
        user = Human("test", 10, "w")
        USERS.append(user)
        return user.to_dict()

    user = [user.to_dict() for user in USERS if user.id == int(user_id)]
    if not user:
        return "id error"

    if request.method == "GET":
        return user[0]
    elif request.method == "PUT":
        for user in USERS:
            if user.id == user_id:
                user.id *= 10
                return user.to_dict()


@app.route("/api/users")
def get_user_list_api():
    return [user.to_dict() for user in USERS]


if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=80)

    app.run(host="0.0.0.0")
