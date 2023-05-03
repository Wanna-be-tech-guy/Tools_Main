import subprocess
import time

subprocess.run(["git", "pull"])

time.sleep(10)

subprocess.run(["usr/lib/python3", "deployment_and_troubleshooting_tool.py"])
