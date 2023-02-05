from app.file_utils import FileUtils
from app.repository import Repository
from app.schema_validator import SchemaValidator


class Parser:

    def __init__(self):
        self.validator = SchemaValidator()
        self.repository = Repository()
        self.file_utils = FileUtils()

    def load(self, data_path: str, spec_path: str):
        schema = self.validator.validate_schema(spec_path)

        if schema is not None and not schema.empty:
            data = self.file_utils.parse(data_path, schema)
            print("Saving data: \n", data.head(5))
            self.repository.save(data, schema)
        else:
            print("Data could not be saved at this time.")
