CREATE TABLE IF NOT EXISTS silver.fact (
    fact_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES silver.user(id) ON DELETE CASCADE,
    fact_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
