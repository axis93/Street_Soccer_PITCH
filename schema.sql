DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS topics;
DROP TABLE IF EXISTS formativeAssessments;
DROP TABLE IF EXISTS tests;
DROP TABLE IF EXISTS quizzes;
DROP TABLE IF EXISTS answers;



CREATE TABLE topics(
	topic_id INTEGER(10) PRIMARY KEY,
	is_unlocked BOOLEAN NOT NULL,
	name VARCHAR(50) NOT NULL,
	needed_credit INTEGER(10)
);

CREATE TABLE formativeAssessments(
	fa_ID INTEGER NOT NULL PRIMARY KEY,
	test_id INTEGER,
	is_unlocked BOOLEAN NOT NULL,
	order_num INTEGER NOT NULL,
	gained_credit INTEGER,
	answer TEXT,
	pass_credit INTEGER,
	instructions TEXT,
	title VARCHAR(100) NOT NULL,
	path_to_attachment TEXT,
	deadline TEXT,	
	reviewer_comment TEXT,
	is_marked BOOLEAN,
	FOREIGN KEY (test_id) REFERENCES topics(topic_id)
);

CREATE TABLE tests(
	test_id INTEGER NOT NULL PRIMARY KEY,
	topic_id INTEGER NOT NULL,
	is_unlocked BOOLEAN,
	max_credit INTEGER NOT NULL,
	order_num INTEGER NOT NULL,
	gained_credit INTEGER,
	pass_credit INTEGER NOT NULL,
	time_limit TIME,
	description TEXT,
	is_retakable BOOLEAN,
	FOREIGN KEY (topic_id) REFERENCES topics(topic_id)
);



CREATE TABLE quizzes(
	quiz_id INTEGER NOT NULL PRIMARY KEY,
	test_id INTEGER NOT NULL,
	order_num INTEGER NOT NULL,
	credit_value INTEGER NOT NULL,
	gained_credit INTEGER,
	type TEXT CHECK(type in ('info', 'multiple_choice', 'short_answer')), 
	text_body TEXT,
	path_to_attachment TEXT,
	title VARCHAR(100),	
	instructions TEXT,
	FOREIGN KEY (test_id) REFERENCES tests(test_id)
	
);


CREATE TABLE answers(
	answer_id INTEGER NOT NULL PRIMARY KEY,
	quiz_id INTEGER NOT NULL,
	body TEXT,
	is_correct BOOLEAN,
	path_to_attachment TEXT,
	is_selected BOOLEAN,
	FOREIGN KEY (quiz_id) REFERENCES quizzes(quiz_id)
);
CREATE TABLE users(
user_iD integer NOT NULL PRIMARY KEY,
	username VARCHAR(50) NOT NULL,
	password VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL

);
INSERT INTO topics (topic_id, is_unlocked, name, needed_credit) VALUES (1, 1, 'Child Protection Policy', 60);
INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakable) VALUES (1, 1, 1, 80, 5, 0, 60, 'For this test you will need to complete two quizzes, please pres the button to carry on', 1);
INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES (1, 1, 5, 0, 0, 'multiple_choice', 'Here there is some text', 'What should be avoided except in emergencies?', 'To complete this quiz please select an answer and then click next');
INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (1, 1, 'Spending time alone with children away from others', 1, 0);