from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os

from project import app, db

app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def test():
	"""Runs the unit tests with coverage."""
	os.system('python unit_tests.py -v')

@manager.command
def coverage():
    """Runs the unit tests with coverage."""
    os.system('coverage run --source=project unit_tests.py -v')
    os.system('coverage report -m')
    os.system('coverage html')
    os.system('coverage erase')

if __name__ == '__main__':
    manager.run()