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
    "INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakeable, is_official) VALUES (1, 1, 1, 80, 5, 0, 60, 'For this test you will need to complete two quizzes, please pres the button to carry on', 1, 1);",
    "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES (1, 1, 1, 0, 0, 'multiple_choice', 'What should be avoided except in emergencies?', 'Question 1', 'To complete this quiz please select an answer and then click next');",
    "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (1, 1, 'Spending time alone with children away from others', 1, 0);",
    "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (2, 1, 'Making sport fun, enjoyable, promoting fair play', 0, 0);",
    "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (3, 1, 'Making sport fun, enjoyable, promoting fair play', 0, 0);",
    "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES(2, 1, 2, 0, 0, 'multiple_choice', 'Choose the most appropriate from the following options that best describes the aim of the Child Protection Policy:', 'Question 2', 'To complete this quiz please select an answer and then click next');",
    "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (4, 2, 'Children should be safely protected with appropriate gear, so that we can minimize injuries to happen', 0, 0);",
    "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (5, 2, 'Make sure that every young person can integrate with each other, in a safe and positive environment', 0, 0);",
    "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (6, 2, 'Promoting good practice by providing young people with appropriate safety and protection, whilst in care of Slum Soccer', 1, 0);",
    "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, path_to_attachment, title, instructions) VALUES(3, 1, 3, 0, 0, 'info', 'Any  suspicion  that  a  child  has  been  abused  by  either a  member of  staff  or a  volunteer should  be reported  to  the  Slum  Soccer  Child  Protection  Officer, who  will take  such  steps  as considered necessary  to  ensure  the  safety  of  the  child  in  question  and  any  other child  who  may  be  at  risk. The  Slum  Soccer  Child  Protection  Officer will  refer the  allegation  to  the  social services department  who  may  involve  the  police. The  parents  or carers  of  the  child  will be  contacted  as soon  as possible  following  advice  from the  social services  department. The  Slum  Soccer  Child  Protection  Officer should  also  notify  the  relevant  Sport  Governing Body  officer who  in  turn  will inform  the  Sport  Governing  Body  Child  Protection  Officer who  will deal with  any  media  enquiries. If  the  Slum  Soccer  Child  Protection  Officer is the  subject  of  the  suspicion/allegation,  the  report must  be  made  to  the  appropriate  Manager or  in  his/her absence  the  Sport Governing Body  Child  Protection  Officer who  will  refer  the  allegation  to  Social  Services. ', '/static/images/Tests/cps.jpg', 'Reporting  concerns about  suspected abuse ', 'Read carefully the text and when you are ensure you understand everything, click next');",
    "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES(4, 1, 4, 0, 0, 'multiple_choice', 'If there is suspicion that a child has been abused by either a member of staff or a volunteer, what is the order of people/roles to be appointed and the steps as considered necessary to be undertaken?','Question 3', 'To complete this quiz please select an answer and then click next');",
    "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (7, 4, 'It should be reported to the appropriate Manager who will refer to the Slum Soccer Child Protection Officer who will contact the police or any social services department', 0, 0);",
    "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (8, 4, 'It should be reported to the Slum Soccer Child Protection Officer, who will refer to the social services department. He should also notify the relevant Sport Governing body office',1, 0);",
    "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (9, 4, 'It should be reported to the police that after their investigations, will contact the Slum Soccer Child Protection Officer, who will inform the Sport Governing Body Child Protection Officer', 1, 0);",
    
    "INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakeable, is_official) VALUES (2, 1, 1, 80, 5, 0, 60, 'For this test you will need to complete two quizzes, please pres the button to carry on', 1, 1);",
    "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES (5, 2, 1, 0, 0, 'multiple_choice', 'What should be avoided except in emergencies?', 'Question 1', 'To complete this quiz please select an answer and then click next');",
    "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (10, 5, 'Spending time alone with children away from others', 1, 0);",
    "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (11, 5, 'Making sport fun, enjoyable, promoting fair play', 0, 0);",
    "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (12, 5, 'Making sport fun, enjoyable, promoting fair play', 0, 0);",
    "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES(6, 2, 2, 0, 0, 'multiple_choice', 'Choose the most appropriate from the following options that best describes the aim of the Child Protection Policy:', 'Question 2', 'To complete this quiz please select an answer and then click next');",
    "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (13, 6, 'Children should be safely protected with appropriate gear, so that we can minimize injuries to happen', 0, 0);",
    "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (14, 6, 'Make sure that every young person can integrate with each other, in a safe and positive environment', 0, 0);",
    "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (15, 6, 'Promoting good practice by providing young people with appropriate safety and protection, whilst in care of Slum Soccer', 1, 0);"
)

init_db(insert_queries)