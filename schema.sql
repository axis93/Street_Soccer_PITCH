DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Topic;
DROP TABLE IF EXISTS FormativeAssessment;
DROP TABLE IF EXISTS Test;
DROP TABLE IF EXISTS Quiz;

CREATE TABLE users(
	user_iD INTEGER PRIMARY KEY,
	username VARCHAR(50) NOT NULL ,
	password VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL,
	PRIMARY KEY user_iD
);


CREATE TABLE topics(
	topic_id INTEGER(10) PRIMARY KEY ,
	is_unlocked BOOLEAN NOT NULL,
	name VARCHAR(50) NOT NULL,
	needed_credit INTEGER(10)
);

CREATE TABLE formativeAssessments(
	fa_ID INTEGER NOT NULL PRIMARY KEY,
	test_id INTEGER
	is_unlocked BOOLEAN NOT NULL,
	order_num INTEGER NOT NULL,
	gained_credit INTEGER,
	answer TEXT,
	pass_credit INTEGER,
	instructions TEXT,
	title VARCHAR(100) NOT NULL,
	path_to_attachment TEXT,
	deadline DATE,
	reviewer_comment TEXT,
	is_marked BOOLEAN,
	FOREIGN KEY (test_id) REFERENCES Topic(topic_id)
);

CREATE TABLE tests(
	test_id INTEGER NOT NULL PRIMARY KEY ,
	topic_id INTEGER NOT NULL,
	is_unlocked BOOLEAN,
	max_credit INTEGER NOT NULL,
	order_num INTEGER NOT NULL,
	gained_credit INTEGER,
	pass_credit INTEGER NOT NULL,
	time_limit TIME,
	description text,
	is_retakable BOOLEAN,
	FOREIGN KEY (topic_id) REFERENCES Topic(topic_id)
);



CREATE TABLE quizzes(
	quiz_id INTEGER NOT NULL PRIMARY KEY ,
	test_id INTEGER NOT NULL,
	order_num INTEGER NOT NULL,
	credit_value INTEGER NOT NULL,
	gained_credit INTEGER,
	type TEXT CHECK(type in ('info', 'multiple_choice', 'short_answer'),
	text TEXT,
	title VARCHAR(100),
	answer_id INTEGER,
	instructions TEXT,
	FOREIGN KEY (test_id) REFERENCES Test(test_id),
	FOREIGN KEY (answer_id) REFERENCES Answer(answer_id)

);

CREATE TABLE answers(
	answer_id INTEGER NOT NULL PRIMARY KEY ,
	body TEXT,
	is_correct BOOLEAN

);

