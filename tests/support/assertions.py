import json
from os.path import join, dirname
from jsonschema import validate
from .utils import load_file

def assert_valid_schema(data, schema_file):

    schema = json.loads(load_file(schema_file, 'schemas'))
    return validate(data, schema)
