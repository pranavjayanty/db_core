CREATE TABLE IF NOT EXISTS bronze.user_raw (
    id SERIAL PRIMARY KEY,
    name TEXT,
    role TEXT,
    notion_id TEXT,
    discord_id TEXT,
    ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
