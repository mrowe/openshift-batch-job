#!/usr/bin/env python

import json, logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(message)s')

class LogMessage(object):
    def __init__(self, message, **kwargs):
        self.message = message
        self.kwargs = kwargs

    def __str__(self):
        self.kwargs['@timestamp'] = datetime.utcnow().isoformat()
        self.kwargs['message'] = self.message
        return json.dumps(self.kwargs)

if __name__ == '__main__':
    logging.info(LogMessage("Hello, world!", batch_ran = "yes"))
