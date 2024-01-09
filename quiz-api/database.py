# database.py
import sqlite3
from question import Question
import json

def create_question(token, question):
    try:
        # Create a connection to the database
        db_connection = sqlite3.connect('quiz.db')
        db_connection.isolation_level = None
        cur = db_connection.cursor()

        # Start transaction
        cur.execute("begin")

        question_model = Question(
            title=question['title'],
            text=question['text'],
            position=question['position'],
            image=question['image'],
            possibleAnswers=question["possibleAnswers"]
        )

        # Serialize the list before saving it to the database
        serialized_answers = json.dumps(question_model.possibleAnswers)

        # Save the question to the database
        insertion_result = cur.execute(
            "INSERT INTO Question (title, text, position, image, possibleAnswers) VALUES (?, ?, ?, ?, ?)",
            (question_model.title, question_model.text, question_model.position, question_model.image, serialized_answers)
        )

        # Commit the transaction in SQLite
        cur.execute("commit")

        # Return the ID of the newly created question
        return {"question_id": insertion_result.lastrowid}

    except sqlite3.Error as e:
        # Handle SQLite database errors
        cur.execute('rollback')
        raise e

    except Exception as e:
        # Handle other exceptions
        cur.execute('rollback')
        raise e

    finally:
        # Close the SQLite cursor and connection
        cur.close()
        db_connection.close()


def get_all_questions():
    try:
        # Create a connection to the database
        db_connection = sqlite3.connect('quiz.db')
        db_connection.isolation_level = None
        cur = db_connection.cursor()

        # Retrieve all questions from the database
        cur.execute("SELECT * FROM Question")
        rows = cur.fetchall()

        # Create a list to store Question objects
        questions = []

        # Iterate through the rows and create Question objects
        for row in rows:
            question = Question(
                title=row[1],
                text=row[2],
                position=row[3],
                image=row[4],
                possibleAnswers=json.loads(row[5])  # Deserialize the possibleAnswers
            )
            questions.append(question)

        return questions

    except sqlite3.Error as e:
        # Handle SQLite database errors
        raise e

    finally:
        # Close the SQLite cursor and connection
        cur.close()
        db_connection.close()