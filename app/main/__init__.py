from flask import Blueprint


main = Blueprint('main', __name__)
# print(main.name, main.import_name, main.template_folder)
from . import view