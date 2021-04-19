import sys

from os import rename

import requests


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    test = "Testing"
    return greeting


print(sys.version)
print(sys.executable)

r = requests.get("http://wwww.intelsat.com")
print(r.status_code)

print(greet("Orlando"))
