import json
from jsonschema import validate
from .utils import load_file

def assert_valid_schema(test_data, schema_file):

    schema = json.loads(load_file(schema_file, 'schemas'))
    return validate(test_data, schema)
