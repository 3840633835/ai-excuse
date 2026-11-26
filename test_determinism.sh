#!/bin/sh
# Check that two runs of main.py write byte-identical output, that the
# output matches entry.txt in this repo, and that it passes the gate
# (UTF-8 text, 1 to 200 characters, not only white space).
set -e
cd "$(dirname "$0")"
rm -rf /tmp/aex_a /tmp/aex_b
mkdir -p /tmp/aex_a /tmp/aex_b
MAKEFUN_OUTPUT_DIR=/tmp/aex_a python3 main.py > /tmp/aex_a.stdout
MAKEFUN_OUTPUT_DIR=/tmp/aex_b python3 main.py > /tmp/aex_b.stdout
cmp /tmp/aex_a/entry.txt /tmp/aex_b/entry.txt && echo "deterministic: identical bytes"
cmp /tmp/aex_a/entry.txt entry.txt && echo "matches entry.txt in repo"
cmp /tmp/aex_a.stdout /tmp/aex_b.stdout && echo "stdout deterministic"
python3 -c "
import os
p = '/tmp/aex_a/entry.txt'
d = open(p, 'rb').read()
t = d.decode('utf-8')
assert 1 <= len(t) <= 200, len(t)
assert t.strip(), 'only white space'
assert (os.stat(p).st_mode & 0o777) == 0o644, oct(os.stat(p).st_mode)
print('gate ok: %d chars, %d bytes, mode 0644' % (len(t), len(d)))
print('entry:', t)
"
