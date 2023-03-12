"""
Settings.
"""

DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_HOST = 'localhost'
DB_SCHEMA = 'postgres'

TZ = 'Europe/Warsaw'

LOCALE = 'pl_PL'

SEED_COUNT = 10


def db_connection_string() -> str:
    return f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_SCHEMA}'
