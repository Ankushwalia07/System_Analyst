'''explore techniques to enhance the maintainability of our task
management web application. We'll focus on code organization,
 error handling, logging, and providing support to users.'''

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

# ... Existing code ...

@app.route("/add", methods=["POST"])
def add_task():
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
