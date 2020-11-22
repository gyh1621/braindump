#! /usr/bin/env nix-shell
#! nix-shell -i python3 -p python3 ninja

import glob
from pathlib import Path
import os
import re


ignore_file_patterns = [
    '^\d{4}-\d{2}-\d{2}\.org$',
    '^inbox\.org$',
    '^daily_.*?\.org$',
    '^mit_3\.org$'
]
allow_file_pattern = '^.*\.org$'

files = []
for root, dirnames, filenames in os.walk('org'):
    for filename in filenames:
        if any(re.match(pattern, filename) for pattern in ignore_file_patterns):
            print('Ignore', filename)
            continue
        if re.match(allow_file_pattern, filename):
            filepath = os.path.join(root, filename)
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
