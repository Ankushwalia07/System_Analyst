from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mail import Mail, Message
import logging
import uuid

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with your own secret key

# Configuration for sending support emails
app.config["MAIL_SERVER"] = "smtp.example.com"  # Replace with your SMTP server
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "your_username"
app.config["MAIL_PASSWORD"] = "your_password"
app.config["MAIL_DEFAULT_SENDER"] = "support@example.com"  # Replace with your support email address

# Initialize Flask-Mail
mail = Mail(app)

tasks = []

class Task:
    """
    Represents a task in the task management system.
    """
    def __init__(self, title, description, status):
        """
        Initialize a new Task object.

        :param title: The title of the task.
        :param description: The description of the task.
        :param status: The status of the task (e.g., "Todo", "Completed").
        """
        self.title = title
        self.description = description
        self.status = status
        self.task_id = str(uuid.uuid4())

@app.route("/")
def index():
    """
    Render the index page that displays all tasks.
    """
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    """
    Add a new task to the task list.

    This function is triggered when the user submits the add task form.

    :return: Redirect to the index page with a flash message.
    """
    try:
        title = request.form["title"]
        description = request.form["description"]
        new_task = Task(title, description, "Todo")
        tasks.append(new_task)
        flash("Task added successfully!", "success")
    except Exception as e:
        app.logger.error(f"Error adding task: {str(e)}")
        flash("An error occurred while adding the task. Please try again.", "error")
    return redirect(url_for("index"))

@app.route("/update/<string:task_id>", methods=["POST"])
def update_task(task_id):
    """
    Update the details of an existing task.

    This function is triggered when the user submits the update task form.

    :param task_id: The ID of the task to update.
    :return: Redirect to the index page with a flash message.
    """
    try:
        title = request.form["title"]
        description = request.form["description"]
        for task in tasks:
            if task.task_id == task_id:
                task.title = title
                task.description = description
                flash("Task updated successfully!", "success")
                return redirect(url_for("index"))
        flash("Task not found!", "error")
    except Exception as e:
        app.logger.error(f"Error updating task: {str(e)}")
        flash("An error occurred while updating the task. Please try again.", "error")
    return redirect(url_for("index"))

@app.route("/complete/<string:task_id>")
def complete_task(task_id):
    """
    Mark a task as completed.

    This function is triggered when the user clicks the "Mark as Completed" link.

    :param task_id: The ID of the task to mark as completed.
    :return: Redirect to the index page with a flash message.
    """
    try:
        for task in tasks:
            if task.task_id == task_id:
                task.status = "Completed"
                flash("Task marked as completed!", "success")
                return redirect(url_for("index"))
        flash("Task not found!", "error")
    except Exception as e:
        app.logger.error(f"Error completing task: {str(e)}")
        flash("An error occurred while completing the task. Please try again.", "error")
    return redirect(url_for("index"))

@app.route("/contact_support", methods=["GET", "POST"])
def contact_support():
    """
    Render the contact support page and handle support requests.

    This function is triggered when the user submits the contact support form.

    :return: Redirect to the index page with a flash message.
    """
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        msg = Message("Support Request", recipients=["support@example.com"])  # Replace with your support email address
        msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        mail.send(msg)

        flash("Your message has been sent to support. We will get back to you soon.", "success")
        return redirect(url_for("index"))

    return render_template("contact_support.html")

if __name__ == "__main__":
    # Configure logging to write logs to a file
    app.logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler("task_manager.log")
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)

    app.run(debug=True)
