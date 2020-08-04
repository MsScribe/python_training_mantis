import random
import string
import os.path
import jsonpickle
import getopt
import sys
from model.mantis import MantisProject

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of mantis project", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# Дефолтные значения
n = 5
f = "data/mantis.json"

# o - Название опции
for o, a in opts:
    if o == "-f":
        f = a
    elif o == "-n":
        n = int(a)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    MantisProject(projectname=random_string("name_", 10), description=random_string("description_", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
print("Path: " + f + " , " + file)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))