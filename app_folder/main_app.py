from flask import Flask, jsonify, render_template, request
import base64
from PIL import Image
from scipy import spatial
import numpy as np
import filetype
import sys
import threading
import os
import requests
import subprocess

cmd = "nohup flask -A app.py run --host=0.0.0.0 --port=9000 &"
subprocess.Popen(cmd, shell = True)

cmd = "nohup flask -A app1.py run --host=0.0.0.0 --port=9001 &"
subprocess.Popen(cmd, shell = True)

cmd = "nohup flask -A app2.py run --host=0.0.0.0 --port=9002 &"
subprocess.Popen(cmd, shell = True)

cmd = "nohup flask -A app3.py run --host=0.0.0.0 --port=9003 &"
subprocess.Popen(cmd, shell = True)

cmd = "nohup flask -A app4.py run --host=0.0.0.0 --port=9004 &"
subprocess.Popen(cmd, shell = True)

cmd = "nohup flask -A app5.py run --host=0.0.0.0 --port=9005 &"
subprocess.Popen(cmd, shell = True)

cmd = "nohup flask -A app6.py run --host=0.0.0.0 --port=9006 &"
subprocess.Popen(cmd, shell = True)

cmd = "nohup flask -A app7.py run --host=0.0.0.0 --port=9007 &"
subprocess.Popen(cmd, shell = True)

cmd = "nohup flask -A app8.py run --host=0.0.0.0 --port=9008 &"
subprocess.Popen(cmd, shell = True)

cmd = "nohup flask -A app9.py run --host=0.0.0.0 --port=9009 &"
subprocess.Popen(cmd, shell = True)

cmd = "nohup flask -A app10.py run --host=0.0.0.0 --port=9010 &"
subprocess.Popen(cmd, shell = True)

cmd = "nohup flask -A app11.py run --host=0.0.0.0 --port=9011 &"
subprocess.Popen(cmd, shell = True)

cmd = "nohup flask -A app12.py run --host=0.0.0.0 --port=9012 &"
subprocess.Popen(cmd, shell = True)

cmd = "nohup flask -A app_reduce.py run --host=0.0.0.0 --port=9013 &"
subprocess.Popen(cmd, shell = True)