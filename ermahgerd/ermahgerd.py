#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import warnings
from pathlib import Path

import pygraphviz as pgv
import yaml
from jinja2 import Environment

YAMLEXAMPLE = f"{str(Path(__file__).parent.parent.resolve())}/example.erd.yml"
warnings.filterwarnings("ignore", category=RuntimeWarning)


def parse_model_yaml(path_):
    with open(path_) as yamlfile:
        model = yaml.safe_load(yamlfile)
    return model


def map_cardinality(card):
    map = {
        "0..1": "noneteeodot",
        "1": "nonetee",
        "0..N": "crowodot",
        "1..N": "crowtee",
        "N": "crow",
    }
    arrowname = map[str(card)]
    return arrowname


def parse_relations(rel={}):
    parent_tuple = rel["parent"].split(".")
    rel["parent"] = dict(table=parent_tuple[0], keycol=parent_tuple[1])
    child_tuple = rel["child"].split(".")
    rel["child"] = dict(table=child_tuple[0], keycol=child_tuple[1])

    rel["parent"]["ie_symbol"] = map_cardinality(str(rel["parent_cardinality"]).upper())
    rel["child"]["ie_symbol"] = map_cardinality(str(rel["child_cardinality"]).upper())
    return rel


def draw_diagram(dot=""):
    G = pgv.AGraph(dot)
    cwd_ = str(Path.cwd())
    G.draw(f"{cwd_}/ermahgerd_output.svg", prog="dot")


def render_template(yaml_file=YAMLEXAMPLE):
    with open(
        f"{str(Path(__file__).parent.resolve())}/template.dot.j2"
    ) as templatefile:
        tmpl_string = templatefile.read()
    env = Environment(keep_trailing_newline=True)

    template = env.from_string(tmpl_string)
    model = parse_model_yaml(yaml_file)
    for rel in model["relations"]:
        rel = parse_relations(rel)
    rendered = template.render(**model)
    return rendered


def handle_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?")
    args = parser.parse_args()
    return args


def main():
    args = handle_args()
    dot = render_template(yaml_file=(args.filename or YAMLEXAMPLE))
    draw_diagram(dot)


if __name__ == "__main__":
    main()
