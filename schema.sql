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
	topic_id INTEGER,
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
	FOREIGN KEY (topic_id) REFERENCES topics(topic_id)
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
	is_retakeable BOOLEAN,
	is_official BOOLEAN NOT NULL,
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
	user_id INTEGER NOT NULL PRIMARY KEY,
	username VARCHAR(50) NOT NULL,
	password VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL
);