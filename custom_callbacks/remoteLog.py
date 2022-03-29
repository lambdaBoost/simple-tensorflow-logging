# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 22:46:13 2022

"""
from keras.callbacks import Callback
import requests

class remoteLog(Callback, api_root, api_path):
    
    def __init__(self,
               root=api_root,
               path=api_path,
               field='data',
               headers=None,
               send_as_json=False):
        super(remoteLog, self).__init__()

        self.root = root
        self.path = path
        self.field = field
        self.headers = headers
        self.send_as_json = send_as_json

    def on_epoch_end(self, epoch, logs=None):
        if requests is None:
            raise ImportError('remoteLog requires the `requests` library.')
        logs = logs or {}
        send = {}
        send['data'] = logs
        send['epoch'] = epoch
        #send['loss'] = logs['loss']
        
        
        requests.post(self.root + self.path, json=send, headers=self.headers)
        