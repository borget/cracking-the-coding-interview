import re
from collections import namedtuple

import pandas as pd
import pandera as pa
from pandas.errors import EmptyDataError
from pandera.errors import SchemaError
from pandera import Check

from app.exceptions import (
    BooleanError,
    WidthError,
    InvalidColumnName,
    IntegerError
)

LineValue = namedtuple("LineValue", "str_idx value")


class SchemaValidator:
    BOOLEAN = "BOOLEAN"
    TEXT = "TEXT"
    INTEGER = "INTEGER"
    DATA_TYPES = [TEXT, BOOLEAN, INTEGER]
    COLUMN_NAME = "column name"
    WIDTH = "width"
    DATATYPE = "datatype"

    def validate_schema(self, spec_path: str) -> pd.DataFrame:
        spec_schema = pa.DataFrameSchema({
            self.COLUMN_NAME: pa.Column(pa.String,
                                        nullable=False,
                                        required=True),
            self.WIDTH: pa.Column(pa.Int,
                                  Check.greater_than_or_equal_to(0),
                                  nullable=False,
                                  required=True),
            self.DATATYPE: pa.Column(pa.String,
                                     Check.isin(self.DATA_TYPES),
                                     nullable=False,
                                     required=True)
        })

        try:
            spec_input = pd.read_csv(spec_path, index_col=False, encoding="UTF-8")
            spec_input.columns = spec_input.columns.str.lower()
            if SchemaValidator.DATATYPE in spec_input.columns:
                spec_input[SchemaValidator.DATATYPE] = spec_input[SchemaValidator.DATATYPE].str.upper()
            spec_schema.validate(spec_input)
            self._validate_boolean_column(spec_input)

            return spec_input
        except EmptyDataError as e:
            print(f"Spec file is empty. [{spec_path}]")
        except SchemaError as se:
            print(f"Spec schema error in file [{spec_path}].")
            print(f"Error [{se.args[0]}]")
        except BooleanError as be:
            print(f"Boolean columns have incorrect values in file [{spec_path}].")

    def _validate_boolean_column(self, spec_input: pd.DataFrame):
        boolean_items = spec_input[spec_input.datatype.str.contains(self.BOOLEAN)]
        is_boolean = True
        if not boolean_items.empty:
            is_boolean = boolean_items[self.WIDTH].isin([0, 1]).all()

        if not is_boolean:
            raise BooleanError

    def to_text(self, str_idx: int, line: str, schema: pd.DataFrame) -> LineValue:
        return self._get_line_value(str_idx, line, schema)

    def to_int(self, str_idx: int, line: str, schema: pd.DataFrame) -> LineValue:
        line_value = self._get_line_value(str_idx, line, schema)
        value = line_value.value
        try:
            value = int(line_value.value)
        except ValueError as e:
            print(f"['{value}'] is not a valid Integer value.")
            raise IntegerError() from e   # dig into from syntax

        return LineValue(line_value.str_idx, value)

    def to_boolean(self, str_idx: int, line: str, schema: pd.DataFrame) -> LineValue:
        self._is_valid_column_name(schema[SchemaValidator.COLUMN_NAME])

        from_idx = str_idx
        str_idx += 1
        value = line[from_idx: str_idx]

        if value not in ["0", "1"]:
            print(f"['{value}'] is not a valid Boolean value.")
            raise BooleanError()

        return LineValue(str_idx, value)

    def validate(self, datatype: str):
        validations = {
            self.TEXT: self.to_text,
            self.BOOLEAN: self.to_boolean,
            self.INTEGER: self.to_int
        }
        return validations.get(datatype, None)

    def _get_line_value(self, str_idx: int, line: str, schema: pd.DataFrame) -> LineValue:
        self._is_valid_column_name(schema[SchemaValidator.COLUMN_NAME])
        from_idx = str_idx
        width = schema[SchemaValidator.WIDTH]
        if width <= 0:
            raise WidthError()

        str_idx += width

        value = line[from_idx: str_idx]
        value = value.strip()
        return LineValue(str_idx, value)

    @staticmethod
    def _is_valid_column_name(column_name: str):
        if not column_name:
            raise InvalidColumnName()

        col_name = column_name.strip()
        is_valid = bool(re.match("^[a-zA-Z]+\\w*$", col_name))
        if not is_valid:
            print(f"Invalid column name [{column_name}]")
            raise InvalidColumnName()
