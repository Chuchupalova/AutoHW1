import os
import pytest
import psycopg2

@pytest.fixture(scope='session')
def db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME", "test_db"),
        user=os.getenv("DB_USER", "test_user"),
        password=os.getenv("DB_PASSWORD", "test_password"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
    )
    yield conn
    conn.close()

