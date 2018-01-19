import sys
from flask import render_template

from belka_flask import app, ThunderBorg

TB = ThunderBorg.ThunderBorg()
TB.Init()
if not TB.foundChip:
    boards = ThunderBorg.ScanForThunderBorg()
    if len(boards) == 0:
        print('No ThunderBorg found, check you are attached :)')
    else:
        print('No ThunderBorg at address %02X, but we did find boards:' % (TB.i2cAddress))
        for board in boards:
            print('    %02X (%d)' % (board, board))
        print('If you need to change the I�C address change the setup line so it is correct, e.g.')
        print('TB.i2cAddress = 0x%02X' % (boards[0]))
    sys.exit()

@app.route('/')
def index():
    app.logger.warning('sample message')
    return render_template('index.html')


@app.route("/forward/", methods=['POST'])
def move_forward():
    forward_message = "Moving Forward..."
    TB.SetMotors(50)
    return render_template('index.html', message=forward_message)


@app.route("/backward/", methods=['POST'])
def move_backward():
    forward_message = "Moving Backward..."
    TB.SetMotors(-50)
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
    TB.SetMotors(0)
    return render_template('index.html', message=forward_message)
