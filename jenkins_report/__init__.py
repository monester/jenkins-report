import flask
import logging

app = flask.Flask(__name__)
logging.basicConfig()

try:
    app.config.from_object('config')
except ImportError:
    env_config_silent = False
else:
    env_config_silent = True
app.config.from_envvar('JENKINS_REPORT_SETTINGS', silent=env_config_silent)

import jenkins_report.views
import jenkins_report.filters
