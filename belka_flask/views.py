from flask import render_template

from belka_flask import app


@app.route('/')
def index():
    app.logger.warning('sample message')
    return render_template('index.html')


@app.route("/forward/", methods=['POST'])
def move_forward():
    forward_message = "Moving Forward..."
    return render_template('index.html', message=forward_message)


@app.route("/backward/", methods=['POST'])
def move_backward():
    forward_message = "Moving Backward..."
    return render_template('index.html', message=forward_message)


@app.route("/turnleft/", methods=['POST'])
def turn_left():
    forward_message = "Turning Left..."
    return render_template('index.html', message=forward_message)


@app.route("/turnright/", methods=['POST'])
def turn_right():
    forward_message = "Turning Right..."
    return render_template('index.html', message=forward_message)


@app.route("/stop/", methods=['POST'])
def stop():
    forward_message = "Stop..."
    return render_template('index.html', message=forward_message)
