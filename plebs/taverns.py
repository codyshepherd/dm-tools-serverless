import numpy
import os
import random

from functools import partial
from name_gen import name_gen

import plebs as plebs_module
from util import http_response


OUT_DIR = os.path.dirname(__file__)
CONTENT_DIR = os.path.join(OUT_DIR, "content/")


NAME_GEN_FUNCTIONS = {
    "adj_noun": name_gen.name_gen_adj_noun,
    "petname": name_gen.name_gen_petname,
}


def tavern_name(**kwargs):
    gen_arg = kwargs.get("name_gen", "adj_noun")
    gen_func = NAME_GEN_FUNCTIONS.get(gen_arg, name_gen.name_gen_adj_noun)

    name = gen_func(**kwargs)
    capitalized_name = " ".join([s.capitalize() for s in name.split()])
    return capitalized_name


def tavern_quest(**kwargs):
    quests_file = kwargs.get("quests", "quests.txt")
    path = os.path.join(CONTENT_DIR, quests_file)

    with open(path, "r") as fh:
        quests = fh.read()
    quests = quests.split("\n")

    return numpy.random.choice(quests)


def tavern(**kwargs):
    t = {}

    for f in FUNCTIONS.keys():
        func = FUNCTIONS[f]
        val = func(**kwargs)
        kwargs[f] = val
        t[f] = val
    return t


FUNCTIONS = {
    "name": tavern_name,
    "npcs": partial(plebs_module._plebs, number=random.randint(0, 5)),
    "proprietor": partial(plebs_module._plebs, number=1),
    "quest": tavern_quest,
}


def _taverns(number: int = 1, **kwargs):

    ts = []
    for _ in range(number):
        ts.append(tavern(**kwargs))

    return ts


def taverns_handler(event, context):
    params = event["queryStringParameters"]
    if params is None:
        params = {}
    return http_response(_taverns(int(params.get("number", "1"))))
