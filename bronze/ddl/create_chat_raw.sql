CREATE TABLE IF NOT EXISTS bronze.chat_raw (
    id SERIAL PRIMARY KEY,
    channel_name TEXT,
    channel_id INT,
    chat_text TEXT,
    ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
