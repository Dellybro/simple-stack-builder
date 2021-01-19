import os
import sys
import yaml
import click
from cfn_tools import load_yaml, dump_yaml

sys.stdout = open("template.yaml", "w+")

@click.command()
def build():
    reader = load_yaml(open("header.yaml", 'r'))
    reader["Resources"] = {}

    for path, dirs, files in os.walk("./"):
        for filename in files:
            if "resource.yaml" in filename:
                fullpath = os.path.join(path, filename)
                reader["Resources"].update(load_yaml(open(fullpath)))

    print dump_yaml(reader)