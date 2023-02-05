from datetime import datetime

import pandas as pd
from sqlalchemy import (
    Boolean,
    create_engine,
    Column,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base
from app.schema_validator import SchemaValidator

DATA_TYPES = {
    SchemaValidator.TEXT: String,
    SchemaValidator.INTEGER: Integer,
    SchemaValidator.BOOLEAN: Boolean
}

CONNECTION_STRING = "postgresql+psycopg2://:@localhost:5432/assignment"


class Repository:

    def __init__(self):
        self.engine = create_engine(CONNECTION_STRING)

    def _create_table(self, schema: pd.DataFrame):
        base = declarative_base()
        timestamp = datetime.now().strftime("%m%d%Y%H%M_%f")

        base_table = {
            "__tablename__": f"t_{timestamp}",
            "id": Column(Integer, primary_key=True, autoincrement=True)
        }

        for i, row in schema.iterrows():
            base_table[row[SchemaValidator.COLUMN_NAME]] = Column(DATA_TYPES[row[SchemaValidator.DATATYPE]])

        table = type("Table", (base,), base_table)
        base.metadata.create_all(self.engine)

        return table

    def save(self, data: pd.DataFrame, schema: pd.DataFrame):
        table = self._create_table(schema)
        table_name = table.__tablename__
        data.to_sql(table_name, self.engine, if_exists="append", index=False)
        print(f"{len(data)} records successfully loaded into [{table_name}].")
