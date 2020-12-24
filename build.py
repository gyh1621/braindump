# coding: utf-8

import glob
from pathlib import Path
import os
import re

EXCLUDELIST = "excludelist"
INCLUDELIST = "includelist"

ORGDIRPATH = "/Users/gyh/org"

# Load exclude / include lists
exclude_patterns = []
include_patterns = ["^.*\.org$"]
if os.path.exists(EXCLUDELIST):
    with open(EXCLUDELIST, "r") as f:
        exclude_patterns += f.read().split()
if os.path.exists(INCLUDELIST):
    with open(INCLUDELIST, "r") as f:
        include_patterns += f.read().split()

files = []
print(ORGDIRPATH)
for root, dirnames, filenames in os.walk(ORGDIRPATH):
    for filename in filenames:
        filepath = os.path.join(root, filename)
        if not any(re.search(pattern, filepath) for pattern in include_patterns):
            continue
        if any(re.search(pattern, filepath) for pattern in exclude_patterns):
            print("Ignore", filename)
            continue
        files.append(filepath)
#print("\n".join(files))
#print(len(files))

with open("build.ninja", "w") as ninja_file:
    ninja_file.write(
        """
rule org2md
  command = emacs --batch -l ~/.emacs.d/init.el -l publish.el --eval \"(jethro/publish \\"$in\\")"
  description = org2md $in
"""
    )

    for f in files:
        path = Path(f)
        output_file = f"content/posts/{path.with_suffix('.md').name}"
        ninja_file.write(
            f"""
build {output_file}: org2md {path}
"""
        )

import subprocess

subprocess.call(["ninja"])
