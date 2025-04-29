from utils.ingestor import BronzeIngestor

if __name__ == "__main__":
    ingestor = BronzeIngestor(
        csv_path="data/user.csv",
        table_name="user_raw",
        schema="bronze",   # optional, defaults to "bronze"
        truncate=False      # optional, defaults to True
    )
    ingestor.run()