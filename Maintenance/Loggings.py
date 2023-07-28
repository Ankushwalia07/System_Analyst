import logging

# ... Existing code ...

if __name__ == "__main__":
    app.logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler("task_manager.log")
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)
    app.run(debug=True)
