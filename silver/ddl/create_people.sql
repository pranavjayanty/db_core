CREATE SCHEMA IF NOT EXISTS silver;

CREATE TABLE IF NOT EXISTS silver.people (
    person_id SERIAL PRIMARY KEY,
    source_id TEXT UNIQUE,
    full_name TEXT NOT NULL,
    email TEXT,
    role TEXT,
    is_committee BOOLEAN DEFAULT FALSE,
    join_date TIMESTAMP,
    last_active_date TIMESTAMP,
    notes TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);