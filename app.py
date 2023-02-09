from flask import Flask, render_template, jsonify

app = Flask(__name__)


class Timer:
    def __init__(self, current_time):
        self.current_time = current_time

    def decrement(self):
        if self.current_time > 0:
            self.current_time = self.current_time - 1
        return self.current_time


t = Timer(current_time=60)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/_timer", methods=["GET", "POST"])
def timer():
    new_time = t.decrement()
    return jsonify({"result": new_time})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)