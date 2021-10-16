# Creating read_yaml function to read the yaml file and return the data as a dictionary.
import yaml
import os


def read_yaml(path_to_yaml: str) -> dict:
    """
    Reads the yaml file and returns the data as a dictionary
    """
    with open(path_to_yaml, 'r') as stream:
        try:
            data = yaml.safe_load(stream) # loading the yaml file
        except yaml.YAMLError as exc:
            print(exc)
    return data # returning the data as a dictionary