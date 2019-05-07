from flask_script import Manager

from apps import app

manager = Manager(app)

@manager.command
def wow():
    print("wow")


if __name__ == '__main__':
    manager.run()

