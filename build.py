# coding: utf-8

import glob
from pathlib import Path
import os
import re

EXCLUDELIST = 'excludelist'
INCLUDELIST = 'includelist'

# Load exclude / include lists
exclude_patterns = []
include_patterns = ['^.*\.org$']
if os.path.exists(EXCLUDELIST):
    with open(EXCLUDELIST, 'r') as f:
        exclude_patterns += f.read().split()
if os.path.exists(INCLUDELIST):
    with open(INCLUDELIST, 'r') as f:
        include_patterns += f.read().split()

files = []
for root, dirnames, filenames in os.walk('org'):
    for filename in filenames:
        filepath = os.path.join(root, filename)
        if not any(re.search(pattern, filepath) for pattern in include_patterns):
            continue
        if any(re.search(pattern, filepath) for pattern in exclude_patterns):
            print('Ignore', filename)
            continue
        # replace time stamp
        stinfo = os.stat(filepath)
        with open(filepath, 'r') as f:
            content = f.read()
        with open(filepath, 'w') as f:
            content = re.sub(
                'Time-stamp:\s<([-\d: ]*) .*>',
                r'- last modified :: \1',
                content
            )
            f.write(content)
        os.utime(filepath, (stinfo.st_atime, stinfo.st_mtime))
        files.append(filepath)
#print('\n'.join(files))
#print(len(files))

with open('build.ninja', 'w') as ninja_file:
    ninja_file.write("""
rule org2md
  command = emacs --batch -l ~/.emacs.d/init.el -l publish.el --eval \"(jethro/publish \\"$in\\")"
  description = org2md $in
""")
    
    for f in files:
        path = Path(f)
        output_file = f"content/posts/{path.with_suffix('.md').name}"
        ninja_file.write(f"""
build {output_file}: org2md {path}
""")

import subprocess
subprocess.call(["ninja"])
