TRUNCATE TABLE silver.user;

INSERT INTO silver.user (name, role, notion_id, discord_id)
SELECT
    name,
    role,
    notion_id,
    discord_id
FROM bronze.user_raw;
