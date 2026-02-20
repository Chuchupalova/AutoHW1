import pytest
import psycopg2

@pytest.fixture(scope='session')
def db_connection():
    conn = psycopg2.connect(
        dbname='test_db',
        user='test_user',
        password='test_password',
        host='localhost',
        port='5433'
    )
    yield conn
    conn.close()

