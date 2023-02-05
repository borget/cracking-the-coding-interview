import os
import glob
from pathlib import Path
from typing import Dict
import pandas as pd

from app.schema_validator import (
    SchemaValidator,
    WidthError,
    LineValue,
    InvalidColumnName,
    BooleanError
)


class FileUtils:

    def __init__(self):
        self.validator = SchemaValidator()

    @staticmethod
    def files(directory: str, extension: str) -> Dict[str, str]:
        current_dir = os.path.dirname(os.path.realpath(__file__))
        dir_path = os.path.join(current_dir, directory, f"*.{extension}")
        file_list = glob.glob(dir_path)

        def file_name(file_path: str):
            f = Path(file_path).stem
            return f.split("_")[0].lower()

        return {file_name(f): f for f in file_list}

    def parse(self, file_path: str, schema: pd.DataFrame) -> pd.DataFrame:
        valid_line_len = schema[SchemaValidator.WIDTH].sum()

        data = []
        with open(file_path, mode="r") as file:
            for line in file:
                line_len = len(line) - 1
                if line_len == valid_line_len:
                    has_error, new_line = self.__validate_line(line, schema)
                    if not has_error:
                        data.append(new_line)
                else:
                    print(f"Length of line is not equal than the schema specification.")

        columns = schema[SchemaValidator.COLUMN_NAME].to_list()
        return pd.DataFrame(data, columns=columns)

    def __validate_line(self, line, schema):
        new_line = []
        has_error = False
        str_idx = 0
        for i, schema_row in schema.iterrows():
            validate = self.validator.validate(schema_row[SchemaValidator.DATATYPE])
            if validate:
                try:
                    line_value: LineValue = validate(str_idx, line, schema_row)
                    str_idx = line_value.str_idx
                    value = line_value.value

                    new_line.append(value)
                except (WidthError, InvalidColumnName, BooleanError) as error:
                    has_error = True
                    break
            else:
                print(f"`{schema_row[SchemaValidator.DATATYPE]}` validation is not registered.")
                has_error = True
                break
        return has_error, new_line
