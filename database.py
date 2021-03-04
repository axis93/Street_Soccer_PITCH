from app import init_db

"""
this would prevent having to duplicate the 'query_db'
method in every Model

this can't be used because we need to import this in the
models, but the models are imported in 'app.py', so this
becomes a circular dependancy

def query_db(self, query, args):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    result = cursor.execute(query, args)
    row = result.fetchone()

    connection.close()

    return row
"""

insert_queries = (
    "INSERT INTO topics (topic_id, is_unlocked, name, needed_credit) VALUES (1, 1, 'Child Protection Policy', 60);",
    "INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakable) VALUES (1, 1, 1, 80, 5, 0, 60, 'For this test you will need to complete two quizzes, please pres the button to carry on', 1);",
    "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES (1, 1, 5, 0, 0, 'multiple_choice', 'Here there is some text', 'What should be avoided except in emergencies?', 'To complete this quiz please select an answer and then click next');",
    "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (1, 1, 'Spending time alone with children away from others', 1, 0);"
)

init_db(insert_queries)