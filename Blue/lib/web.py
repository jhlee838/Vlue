from http import server
import os

def start(port=8000):
    os.system("cd {}".format(os.path.join(os.path.dirname(os.path.abspath(__file__)), "server")))
    result = os.popen("dir").read()
    print(result)