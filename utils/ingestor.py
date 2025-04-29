import pandas as pd
from sqlalchemy import text
from config.db_config import engine

class BronzeIngestor:
    def __init__(self, csv_path, table_name, schema="bronze", truncate=True):
        self.csv_path = csv_path
        self.schema = schema
        self.table_name = table_name
        self.truncate = truncate
        self.df = None

    def load_csv(self):
        self.df = pd.read_csv(self.csv_path)
        self.df.columns = [col.lower() for col in self.df.columns]
        print(f"📄 Loaded {len(self.df)} rows from {self.csv_path}")

    def truncate_table(self):
        full_table = f"{self.schema}.{self.table_name}"
        with engine.begin() as connection:
            connection.execute(text(f"TRUNCATE TABLE {full_table};"))
            print(f"🧹 Truncated table {full_table}")

    def insert_into_table(self):
        full_table = f"{self.schema}.{self.table_name}"
        with engine.begin() as connection:
            self.df.to_sql(
                self.table_name,
                con=connection,
                schema=self.schema,
                if_exists='append',
                index=False
            )
            print(f"🚀 Inserted {len(self.df)} rows into {full_table}")

    def run(self):
        self.load_csv()
        if self.truncate:
            self.truncate_table()
        self.insert_into_table()
