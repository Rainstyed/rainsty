#!./python/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import logging
base_path = os.path.dirname(__file__)
print('{}/{}'.format(base_path, 'logs/rainLog.log'))
with open('{}/{}'.format(base_path, 'logs/rainLog.log'), 'a') as a:
    a.write('\n')
from flask import Flask, request
from controller.rainController import *
from middleWare import rainMiddleWare as Ware
from config import rainConfig


app = Flask(__name__, static_url_path='', static_folder='file', template_folder='html')
app.config['SECRET_KEY'] = os.urandom(24)
app.config['RAIN_USER'] = './db/rainUser.db'
app.config['RAINDB_CONF'] = {'path': './rainDB', 'database': 'rain'}
app.logger = logging
app.logger.basicConfig(level=logging.INFO, **rainConfig.logConf())


@app.route('/rainenrollment', methods=['POST'])
@Ware.rainEnrollmentMW(request)
def enrollment():
    return rainEnrollment(request.json)


@app.route('/rain', methods=['GET', 'POST'])
@Ware.rainEntranceMW(request)
def entrance():
    return rainEntrance(request.form.to_dict())


@app.route('/rainentergoin', methods=['GET', 'POST'])
@Ware.rainEntergoinMW(request, "input_entergoin")
def entergoin():
    return rainVerifyInfo(request.form.to_dict())


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error=error), 404


def main(args):
    app.run('0.0.0.0', int(args))


if __name__ == '__main__':
    main(sys.argv[1])

