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

cmd = "killport 9000"
x = os.popen(cmd).read()

cmd = "killport 9001"
x = os.popen(cmd).read()

cmd = "killport 9002"
x = os.popen(cmd).read()

cmd = "killport 9003"
x = os.popen(cmd).read()

cmd = "killport 9004"
x = os.popen(cmd).read()

cmd = "killport 9005"
x = os.popen(cmd).read()

cmd = "killport 9006"
x = os.popen(cmd).read()

cmd = "killport 9007"
x = os.popen(cmd).read()

cmd = "killport 9008"
x = os.popen(cmd).read()

cmd = "killport 9009"
x = os.popen(cmd).read()

cmd = "killport 9010"
x = os.popen(cmd).read()

cmd = "killport 9011"
x = os.popen(cmd).read()

cmd = "killport 9012"
x = os.popen(cmd).read()

cmd = "killport 9013"
x = os.popen(cmd).read()