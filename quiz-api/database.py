# database.py
import sqlite3

def create_question(token, question):
    try:
        # Create a connection to the database
        db_connection = sqlite3.connect('your_database_path.db')
        db_connection.isolation_level = None
        cur = db_connection.cursor()

        # Start transaction
        cur.execute("begin")

        # Save the question to the database
        insertion_result = cur.execute(
            f"INSERT INTO Question (title, text, position, image) VALUES "
            f"('{question['title']}', '{question['text']}', {question['position']}, '{question['image']}')")

        # Commit the transaction in SQLite
        cur.execute("commit")

        # Return the ID of the newly created question
        return {"question_id": insertion_result.lastrowid}

    except Exception as e:
        # In case of exception, rollback the transaction in SQLite
        cur.execute('rollback')
        raise e

    finally:
        # Close the SQLite cursor and connection
        cur.close()
        db_connection.close()
