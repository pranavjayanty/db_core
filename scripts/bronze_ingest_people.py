from utils.ingestor import BronzeIngestor

if __name__ == "__main__":
    ingestor = BronzeIngestor(
        csv_path="data/people.csv",
        table_name="people_raw",
        schema="bronze",   # optional, defaults to "bronze"
        truncate=True      # optional, defaults to True
    )
    ingestor.run()