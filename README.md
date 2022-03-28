# simple-tensorflow-logging
Basic server to log tensorflow models using a modified version of the keras remoteMonitor callback. For basic training runs - better to use MLFlow in cases where practical.

Uses fast api to deploy remote logging API to monitor training progress. Created mainly because I can't find any other examples of anyone actually using this callback.
