import os
import logging
import imp

from jenkins_report.scripts.fetch_data import update_builds_db

logger = logging.getLogger(__name__)
logging.basicConfig()

env_cfg = os.environ.get('JENKINS_REPORT_SETTINGS')
if env_cfg:
    config = imp.load_source('config', env_cfg)
else:
    logger.error('No configuration')
    exit(1)


for name, entry in config.DB.items():
    filename = entry['filename']
    source = entry['source']
    if 'url' in source:
        params = {
            'dbname': filename,
            'source_url': source['url']
        }
    elif 'file' in source:
        params = {
            'dbname': filename,
            'source_file': source['file']
        }
    else:
        logging.warn('No source for {}'.format(name))
        continue
    try:
        update_builds_db(**params)
    except:
        logging.warn('Failed while importing from {}'.format(name))
