# Create a ready-to-upload GitHub starter template as a zip file
import os, json, textwrap, zipfile, datetime, pathlib

here = pathlib.Path(__file__).parent.resolve()
root = "/wrr-project-starter"
pp = pathlib.Path(here + root)
pp.mkdir(parents=True, exist_ok=True)

# Helper to write files
def w(path, content, binary=False):
    p = pp / path
    p.parent.mkdir(parents=True, exist_ok=True)
    mode = "wb" if binary else "w"
    with open(p, mode) as f:
        if binary:
            f.write(content)
        else:
            f.write(content.strip() + "\n")
    return p

year = datetime.date.today().year

README = f"""
# Open Python for WRR Data Project - Starter Template

This repository is a starter for the student project. It gives you a clean, reproducible Python setup for WRR analyses with geodata and GDAL.

## Quick start
1. Install [mamba](https://mamba.readthedocs.io) or conda.
2. Create the environment:
   ```bash
   mamba env create -f environment.yml
   mamba activate hydraulics-proj

