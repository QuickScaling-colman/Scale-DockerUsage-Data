from Docker import *
from MongoDBReporter import *
import yaml

# Open the config to figure out the connection details
f = open('config.yaml')
config = yaml.safe_load(f)
f.close()

# Connect to Docker Remote API to query the containers
docker = Docker( config["docker"]["api"])
containers = docker.getContainers()

# Create MongoDBReporter
mongo = InfluxDBReporter(config["mongodb"]["connectionstring"], config["mongodb"]["database"])

for container in containers:	
	id = container["Id"];
	name = container["Names"][0]
	print id, name

	# Get stats from Cgroups files in /sys/fs/cgroup/.. 
	# Paths are different in CoreOS and Ubuntu, do not know really why
	cpu = docker.cpuStats(id);
	memory = docker.memoryStats(id);

	# Report the metrics to database
	mongo.reportMemory(id, memory)
	mongo.reportCpu(id, cpu)