'''Convert py script to ipynb notebook

This script finds all .py in the lesson subdirectories and converts
them to Jupyter notebooks. It excludes the answers dir and itself.

Tested on Linux; no cross-OS guarantees.

Source modified from https://stackoverflow.com/questions/23292242/converting-to-not-from-ipython-notebook-format/35720002#35720002
'''

from nbformat import v3, v4
from pathlib import Path
import re

p = Path('./')
pysrc = list(p.glob('[0-9]*L*/**/*.py'))

print(pysrc)

for src in pysrc:
	if 'answers' in str(src.parent):
		print('Skipping: {}'.format(src))
		pass
	else:
		# print('Writing file: {} to dir {}'.format(src.name, src.parent))
		with open(str(src)) as infile:
			text = infile.read()

			# Add matplotlib import
			if 'matplotlib' not in text:
				text = '%matplotlib inline\nimport matplotlib.pyplot as plt\n' + text
			else:
				text = '%matplotlib inline\n' + text

			# Convert and write the notebooks
			notebook = v3.read_py(text)
			notebook = v4.upgrade(notebook)
			jsonform = v4.writes(notebook) + "\n"
			outfile = re.sub('\.py', '.ipynb', str(src))
			with open(outfile, 'w') as fpout:
				fpout.write(jsonform)
			print('Converted {} to {}'.format(str(src), outfile))
