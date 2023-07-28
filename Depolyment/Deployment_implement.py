from flask import Flask, render_template, request, redirect, url_for, flash
import uuid

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with your own secret key

tasks = []

class Task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status
        self.task_id = str(uuid.uuid4())

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form["title"]
    description = request.form["description"]
    new_task = Task(title, description, "Todo")
    tasks.append(new_task)
    flash("Task added successfully!", "success")
    return redirect(url_for("index"))

@app.route("/update/<string:task_id>", methods=["POST"])
def update_task(task_id):
    title = request.form["title"]
    description = request.form["description"]
    for task in tasks:
        if task.task_id == task_id:
            task.title = title
            task.description = description
            flash("Task updated successfully!", "success")
            return redirect(url_for("index"))
    flash("Task not found!", "error")
    return redirect(url_for("index"))

@app.route("/complete/<string:task_id>")
def complete_task(task_id):
    for task in tasks:
        if task.task_id == task_id:
            task.status = "Completed"
            flash("Task marked as completed!", "success")
            return redirect(url_for("index"))
    flash("Task not found!", "error")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
