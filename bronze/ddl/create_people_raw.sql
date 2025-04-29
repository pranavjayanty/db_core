CREATE SCHEMA IF NOT EXISTS bronze;

CREATE TABLE IF NOT EXISTS bronze.people_raw (
    id SERIAL PRIMARY KEY,
    source_id TEXT,
    full_name TEXT,
    email TEXT,
    role TEXT,
    is_committee BOOLEAN,
    join_date TIMESTAMP,
    last_active_date TIMESTAMP,
    notes TEXT,
    ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
