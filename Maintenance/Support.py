from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with your own secret key

app.config["MAIL_SERVER"] = "smtp.example.com"  # Replace with your SMTP server
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "your_username"
app.config["MAIL_PASSWORD"] = "your_password"
app.config["MAIL_DEFAULT_SENDER"] = "support@example.com"  # Replace with your support email address

mail = Mail(app)

# ... Existing code ...

@app.route("/contact_support", methods=["GET", "POST"])
def contact_support():
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

# ... Existing code ...
