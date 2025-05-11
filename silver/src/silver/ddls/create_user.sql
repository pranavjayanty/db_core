CREATE TABLE IF NOT EXISTS silver.user (
    id SERIAL PRIMARY KEY,
    name TEXT,
    role TEXT,
    notion_id TEXT,
    discord_id TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);