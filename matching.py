from csv_processing import load_csv, get_name_list, get_name_role_mapping
import os
import json
import random
from functools import partial
from typing import Callable

CSV_FILE_PATH = "people.csv"


def satisfy_constraint(constraints: dict[str, list[str]], role_map: dict[str, str], pair: tuple[str, str]):
    '''
    Check if a potential pairing satisfy some arbitrary constraint(s).

    :param pair: Tuple of two names representing a potential pair.
    :return: True/False. True if the pair satisfy the constraint(s), False otherwise.
    '''
    role_constraint = role_map[pair[0]] != role_map[pair[1]]
    have_met_constraint = pair[0] not in constraints[pair[1]] and pair[1] not in constraints[pair[0]]
    return role_constraint and have_met_constraint


def find_pair(name_list: list[str], constraint_func: Callable):
    '''
    Recursively backtracks until a list of pairs that satisfy some constraints is found.

    :param name_list: List of names to be paired.
    :param constraint_func: Function that checks if a potential pairing satisfy some arbitrary constraint(s).
    Function only takes in a tuple of two names representing a potential pair.
    Any additional arguments must be partially applied prior.
    :return: List of pairings
    '''

    random.shuffle(name_list)
    candidate = name_list.pop(0)
    for name in name_list:
        potential_pair = candidate, name
        if constraint_func(potential_pair):
            new_name_list = name_list.copy()
            new_name_list.remove(name)
            if len(new_name_list) == 0:
                return [potential_pair]

            result: list[tuple[str, str]] = find_pair(new_name_list, constraint_func)
            if result is not None:
                result.insert(0, potential_pair)
                return result

    return None


def find():
    csv_data = load_csv(CSV_FILE_PATH)
    name_list = get_name_list(csv_data)
    role_map = get_name_role_mapping(csv_data)

    if not os.path.isfile("constraints.json"):
        with open("constraints.json", "w") as f:
            json.dump({name: [] for name in name_list}, f)

    with open("constraints.json", "r") as f:
        constraints: dict[str, list[str]] = json.load(f)

    constraint_func = partial(satisfy_constraint, constraints, role_map)
    pairings = find_pair(name_list, constraint_func)
    if pairings is None:
        return

    for pair in pairings:
        constraints[pair[0]].append(pair[1])
        constraints[pair[1]].append(pair[0])

    with open("constraints.json", "w") as f:
        json.dump(constraints, f)

    return pairings



