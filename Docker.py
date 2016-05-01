import urllib2
import json

def getLines(filename):
	f = open(filename)
	lines = [line.rstrip('\n') for line in open(filename)]
	f.close()
	return lines

class Docker:
	def __init__(self, api):
		self.api = api;

	def cpuStats(self, id):
		values = [int(value) for value in getLines("/sys/fs/cgroup/cpuacct/docker/" + id + "/cpuacct.usage_percpu")[0].split()]
		total = 0
		for value in values:
			total = total + value
		resp = {'total': total, 'cpus': values} 
		return resp

	def memoryStats(self, id):
		lines = getLines("/sys/fs/cgroup/memory/docker/" + id + "/memory.stat")
		resp = {}
		for line in lines:
			line = line.split()
			resp[line[0]] = int(line[1])

		return resp

	def getContainers(self):
		response = urllib2.urlopen(self.api + "/containers/json");
		data = json.load(response) 
		return data
