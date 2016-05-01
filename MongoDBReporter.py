from pymongo import MongoClient
from datetime import datetime
import socket

class MongoDBReporter:

	def __init__(self, connectionstring, dbname):
		# Construct a MongoDB client and our localhost name to report to the server
		self.client = MongoClient(connectionstring)
        self.db = self.client[dbname]
		self.hostname = socket.gethostname()

	def reportCpu(self, id, metrics):
		points = [metrics["total"]]
		columns = ["Total"]
        usages = self.db.usages

    # There might be many cpus, store values as CPU0-value, CPU1-value..
		for idx, cpu in enumerate(metrics["cpus"]):
			points.append(cpu)
			columns.append("CPU" + str(idx))

        data = {}
        data['created_at'] = tweet.created_at
        data['points'] = [points]
        data['name'] = self.hostname + "."  + id + ".cpu"
        data['colums'] = colums
        usages.insert(data)

	def reportMemory(self, id, metrics):
		points = []
		columns = []
        usages = self.db.usages

		# Iterates over all memory metrics, can be altered to report only specific fields such as rss
		for key, value in metrics.iteritems():
			points.append(value)
			columns.append(key)

        data = {}
        data['created_at'] = tweet.created_at
        data['points'] = [points]
        data['name'] = self.hostname + "." + id + ".memory"
        data['colums'] = colums
        usages.insert(data)
