from flask import Flask, render_template
from static.python import newSongOperations
from jinja2 import Environment, PackageLoader, select_autoescape
import os
import sys

# ensure project root is on sys.path so imports like `import src.whatever` work
_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _project_root not in sys.path:
  sys.path.insert(0, _project_root)

env = Environment(
  loader=PackageLoader("src", "templates"),
  autoescape=select_autoescape()
)

app = Flask(__name__)



@app.route("/")
def home():
  songObjs = newSongOperations.createAllSongs()
  
  return render_template("index.html",songs=songObjs)

@app.route("/search/<inputText>")
def search(inputText):
  return None # TODO

@app.route("/returnjson")
def returnjson():
  return app.send_static_file("data/library.json")

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
