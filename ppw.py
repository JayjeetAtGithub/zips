import os

DIRNAME="nyc/"

for root, dir, files in os.walk(DIRNAME, topdown=True):
	if len(files) > 0:
		id = root + "/" + files[0]
		print(f"putting {id}")
		os.system(f"rados -p test-pool put {id} {id}")

