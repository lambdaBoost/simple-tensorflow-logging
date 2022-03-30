# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 22:46:13 2022

"""
from keras.callbacks import Callback
import requests
import logging

class remoteLog(Callback):
    
    def __init__(self,
               root = 'http://192.168.1.217',
               path= '/publish/epoch/end/',
               field='data',
               headers=None,
               send_as_json=False,
               epochs=100):
        super(remoteLog, self).__init__()

        self.root = root
        self.path = path
        self.field = field
        self.headers = headers
        self.send_as_json = send_as_json
        self.epochs = epochs

    def on_epoch_end(self, epoch, logs=None):
        if requests is None:
            raise ImportError('RemoteMonitor requires the `requests` library.')
        logs = logs or {}
        send = {}
        send['data'] = logs
        send['epoch'] = epoch
        send['total_epochs'] = self.epochs
               
        try:
            requests.post(self.root + self.path, json=send, headers=self.headers)
        
            #TODO. ugh another blind exception but connectionerror doesnt seem to work
        except:
            logging.info("no connection to monitor API")
        