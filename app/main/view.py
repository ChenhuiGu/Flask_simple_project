import traceback
from flask import request, abort
from app.main import main
from utils.srf_log import logger


@main.route('/index', methods=['GET','POST'])
def credit_answer():
    try:
        method = request.method
        content_type = request.content_type
        if method == 'GET':
            data = 'get request'
        else:
            data = 'post request'
        return data
    except Exception as e:
        logger.error('url: %s, exception: %s', request.url, traceback.format_exc())
        abort(500)



























