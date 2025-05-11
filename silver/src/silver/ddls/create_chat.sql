CREATE TABLE IF NOT EXISTS silver.chat (
    id SERIAL PRIMARY KEY,
    channel_name TEXT,
    channel_id INT,
    chat_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
