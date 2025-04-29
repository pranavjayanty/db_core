from config.db_config import engine
from sqlalchemy import text

def execute_sql_file(filepath):
        with engine.begin() as conn:
            with open(filepath, 'r') as file:
                print(f"Executing {filepath}...")
                conn.execute(text(file.read()))
                print(f"✅ Done: {filepath}")

def run_scripts_in_order(manifest_path):
    from utils.manifest_loader import load_manifest
    scripts = load_manifest(manifest_path)

    for script_path in scripts:
        execute_sql_file(script_path)
