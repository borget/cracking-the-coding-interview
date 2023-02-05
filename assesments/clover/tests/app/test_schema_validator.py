import os

import pandas as pd
import pytest

from app.exceptions import InvalidColumnName, BooleanError, WidthError
from app.schema_validator import SchemaValidator


@pytest.mark.parametrize(
    "column_name",
    [
        None,
        "_column",
        "*column",
        "3column",
        "%u",
        " ",
    ]
)
def test_invalid_column_name(column_name):
    with pytest.raises(InvalidColumnName):
        SchemaValidator._is_valid_column_name(column_name)


@pytest.mark.parametrize(
    "column_name",
    [
        "col_1",
        "valid",
        "col1",
        "col11111",
        "col_1_1_1",
    ]
)
def test_valid_column_name(column_name):
    SchemaValidator._is_valid_column_name(column_name)


@pytest.fixture(scope="session")
def schema():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    specs = pd.read_csv(os.path.join(current_dir, "specs", "schema.csv"))
    specs.columns = specs.columns.str.lower()
    return specs


@pytest.mark.parametrize(
    "boolean",
    [
        "2",
        "-",
        "@",
        "F",
        " ",
        "*",
    ]
)
def test_raise_exception_not_a_boolean(boolean, schema):
    validator = SchemaValidator()

    boolean_schema = schema.iloc[1]
    with pytest.raises(BooleanError):
        validator.to_boolean(0, boolean, boolean_schema)


@pytest.mark.parametrize(
    "boolean",
    [
        "1",
        "0",
    ]
)
def test_to_boolean(boolean, schema):
    validator = SchemaValidator()
    boolean_schema = schema.iloc[1]
    line = validator.to_boolean(0, boolean, boolean_schema)
    assert line.str_idx == 1
    assert line.value in ["1", "0"]


@pytest.mark.parametrize(
    "text, str_idx",
    [
        ("12TEST        24", 2),
        ("TEST        1 -1", 0),
        ("1-10TEST        ", 4),
        ("1 0     TEST    ", 4),
        ("1 0         TEST", 4)
    ]
)
def test_to_text(str_idx, text, schema):
    validator = SchemaValidator()
    text_schema = schema.iloc[0]
    line = validator.to_text(str_idx, text, text_schema)
    assert line.value == "TEST"


@pytest.mark.parametrize(
    "width",
    [
        0,
        -23
    ]
)
def test_text_width_error(width, schema):
    validator = SchemaValidator()
    text_schema = schema.iloc[0]
    txt = text_schema.copy()
    txt[SchemaValidator.WIDTH] = width
    with pytest.raises(WidthError):
        validator.to_text(0, "TEST", txt)


@pytest.mark.parametrize(
    "integer,str_idx,expected",
    [
        ("-1-1-2-3-4-555-2", 10, -555),
        ("12 23     False", 2, 23),
        ("45         1111", 0, 45),
        ("1-1091         ", 4, 91),
        ("1 0   33       ", 4, 33),
        ("1 0          23", 11, 23),
        (" 23 ", 0, 23),
        ("-1-23  -1-1-2-3", 3, 23),
    ]
)
def test_to_int(expected, str_idx, integer, schema):
    validator = SchemaValidator()
    int_schema = schema.iloc[2]
    line = validator.to_int(str_idx, integer, int_schema)
    assert line.value == expected


def test_validate_schema_empty_data_error():
    validator = SchemaValidator()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    schema_path = os.path.join(current_dir, "specs", "schema_empty.csv")

    validator.validate_schema(schema_path)


@pytest.mark.parametrize(
    "schema_file",
    [
        "schema_missing_column_name.csv",
        "schema_missing_width.csv",
        "schema_missing_datatype.csv",
        "schema_empty_column_name.csv",
        "schema_empty_datatype.csv",
        "schema_empty_width.csv",
        "schema_negative_width.csv",
        "schema_invalid_datatypes.csv",
        "schema_invalid_width.csv",
        "schema_invalid_boolean.csv",
    ]
)
def test_validate_schema_error(schema_file):
    validator = SchemaValidator()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    schema_path = os.path.join(current_dir, "specs", schema_file)

    validator.validate_schema(schema_path)


@pytest.mark.parametrize(
    "schema_file",
    [
        "schema_all_required_columns_present.csv",
        "schema_columns_can_be_in_any_order.csv",
    ]
)
def test_validate_schema(schema_file):
    validator = SchemaValidator()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    schema_path = os.path.join(current_dir, "specs", schema_file)

    actual = validator.validate_schema(schema_path)
    assert set(actual.columns.to_list()).issubset({
        SchemaValidator.COLUMN_NAME,
        SchemaValidator.WIDTH,
        SchemaValidator.DATATYPE
    })
