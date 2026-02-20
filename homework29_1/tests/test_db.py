def test_connection(db_connection):
    assert db_connection is not None

def test_create_table(db_connection):
    cursor = db_connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100)
        );
    ''')
    db_connection.commit()
    cursor.close()

def test_insert_user(db_connection):
    cursor = db_connection.cursor()
    cursor.execute('INSERT INTO users (name) VALUES (%s);', ('Lena',))
    db_connection.commit()
    cursor.close()

def test_select_user(db_connection):
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM users WHERE id = %s;', (1,))
    result = cursor.fetchone()
    cursor.close()

    assert result is not None
    assert result == (1, 'Lena',)
