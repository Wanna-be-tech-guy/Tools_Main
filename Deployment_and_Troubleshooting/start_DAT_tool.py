import subprocess
import time

subprocess.run(["git", "pull"])

time.sleep(10)

subprocess.run(["usr/bin/python3", "deployment_and_troubleshooting_tool.py"], cwd="/home/linux-user/gitmaster/Network_Troubleshooting_Tool/https---github.com-Wanna-be-tech-guy-Network_Troubleshooting_Tool/Deployment_and_Troubleshooting")
