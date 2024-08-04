import os
from flask import Flask, render_template

app = Flask(__name__)

def make_tree(path):
    tree = {"name": os.path.basename(path), "children": []}
    try:
        lst = os.listdir(path)
    except OSError:
        pass  # Ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree["children"].append(make_tree(fn))
            else:
                tree["children"].append({"name": name})
    return tree

@app.route("/")
def dirtree():
    # Specify the path to the folder you want to list
    path = os.path.expanduser("~/path/to/your/folder")
    return render_template("dirtree.html", tree=make_tree(path))

if __name__ == "__main__":
    app.run(host="localhost", port=8888, debug=True)