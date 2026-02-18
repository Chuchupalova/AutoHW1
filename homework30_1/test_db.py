import pytest
import psycopg2
import allure

@allure.feature("Database tests")
@allure.story("Connection tests")
def test_connection(db_connection):
    with allure.step("Check DB connection is not None"):
        assert db_connection is not None

@allure.feature("Database tests")
@allure.story("Create table")
def test_create_table(db_connection):
    with allure.step("Create user table"):
        cursor = db_connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100)
        );
    ''')
    db_connection.commit()
    cursor.close()

@allure.feature("Database tests")
@allure.story("Insert user")
def test_insert_user(db_connection):
    with allure.step("Insert user into users table"):
        cursor = db_connection.cursor()
        cursor.execute(
            'INSERT INTO users (name) VALUES (%s);',
            ('Lena',)
        )
        db_connection.commit()
        cursor.close()

@allure.feature("Database tests")
@allure.story("Select user")
def test_select_user(db_connection):
    with allure.step("Select user from users table"):
        cursor = db_connection.cursor()
        cursor.execute(
            'SELECT name FROM users WHERE name = %s;',
            ('Lena',)
        )
        result = cursor.fetchone()
        cursor.close()
    with allure.step("Verify selected user name"):
        assert result is not None
        assert result[0] == 'Lena'




