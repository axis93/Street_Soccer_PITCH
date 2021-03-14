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

insert_queries = ( # these are queries used only for inserting test data, this should not be needed once the form to make quizzes is implemented
    # Topic 1 - Child Protection Policy
    "INSERT INTO topics (topic_id, is_unlocked, name, needed_credit) VALUES (1, 1, 'Child Protection Policy', 170);",
        # Test 1
        "INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakeable, is_official) VALUES (1, 1, 1, 30, 1, 0, 15, 'This test will cover the introduction to Child Protection Policy.', 1, 1);",
            # Quiz 1
            "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES (1, 1, 1, 10, 0, 'multiple_choice', 'What should be avoided except in emergencies?', 'Question 1', 'To complete this quiz please select an answer and then click next. You can, however, come to the question later and change your answer.');",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (1, 1, 'Spending time alone with children away from others', 1, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (2, 1, 'Making sport fun and enjoyable', 0, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (3, 1, 'Promoting fair play', 0, 0);",
            # Quiz 2
            "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES(2, 1, 2, 10, 0, 'multiple_choice', 'Choose the most appropriate from the following options that best describes the aim of the Child Protection Policy:', 'Question 2', 'To complete this quiz please select an answer and then click next');",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (4, 2, 'Children should be safely protected with appropriate gear, so that we can minimize injuries to happen', 0, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (5, 2, 'Make sure that every young person can integrate with each other, in a safe and positive environment', 0, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (6, 2, 'Promoting good practice by providing young people with appropriate safety and protection, whilst in care of Slum Soccer', 1, 0);",
            # Quiz 3 - Info Page
            "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, path_to_attachment, title, instructions) VALUES(3, 1, 3, 0, 0, 'info', 'Any  suspicion  that  a  child  has  been  abused  by  either a  member of  staff  or a  volunteer should  be reported  to  the  Slum  Soccer  Child  Protection  Officer, who  will take  such  steps  as considered necessary  to  ensure  the  safety  of  the  child  in  question  and  any  other child  who  may  be  at  risk. The  Slum  Soccer  Child  Protection  Officer will  refer the  allegation  to  the  social services department  who  may  involve  the  police. The  parents  or carers  of  the  child  will be  contacted  as soon  as possible  following  advice  from the  social services  department. The  Slum  Soccer  Child  Protection  Officer should  also  notify  the  relevant  Sport  Governing Body  officer who  in  turn  will inform  the  Sport  Governing  Body  Child  Protection  Officer who  will deal with  any  media  enquiries. If  the  Slum  Soccer  Child  Protection  Officer is the  subject  of  the  suspicion/allegation,  the  report must  be  made  to  the  appropriate  Manager or  in  his/her absence  the  Sport Governing Body  Child  Protection  Officer who  will  refer  the  allegation  to  Social  Services. ', 'cps.jpg', 'Reporting  concerns about  suspected abuse ', 'Read carefully the text and when you are ensure you understand everything, click next. You won t be able to return to this page when you leave it, so read carefully.');",
            # Quiz 4
            "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES(4, 1, 4, 10, 0, 'multiple_choice', 'If there is suspicion that a child has been abused by either a member of staff or a volunteer, what is the order of people/roles to be appointed and the steps as considered necessary to be undertaken?','Question 4', 'To complete this quiz please select an answer and then click next');",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (10, 4, 'It should be reported to the appropriate Manager who will refer to the Slum Soccer Child Protection Officer who will contact the police or any social services department', 0, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (11, 4, 'It should be reported to the Slum Soccer Child Protection Officer, who will refer to the social services department. He should also notify the relevant Sport Governing body office',1, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (12, 4, 'It should be reported to the police that after their investigations, will contact the Slum Soccer Child Protection Officer, who will inform the Sport Governing Body Child Protection Officer', 0, 0);",

        # Test 2
        "INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakeable, is_official) VALUES (2, 1, 1, 40, 2, 0, 20, 'This test tests you on the aim of the Child Protection Policy. You have only one attempt for this test.', 0, 1);",
            # Quiz 1 - Info Page
            "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES (5, 2, 1, 0, 0, 'info', 'Slum Soccer has a duty of care to safeguard all children involved in Slum Soccer from harm. All children have a right to protection, and the needs of disabled children and others who may be particularly vulnerable must be taken into account. Slum Soccer will ensure the safety and protection of all children involved in Slum Soccer through adherence to the Child Protection guidelines adopted by Slum Soccer. A child is defined as a person under the age of 18.', 'Aim of the Child Protection Policy', 'After leaving this page you won t be able to return. Read carefully.');",
            # Quiz 2
            "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES (6, 2, 2, 10, 0, 'multiple_choice', 'What children does Slum Soccer ensures safety and protection to?', 'Question 1', 'Select your answer and click on continue...');",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (13, 6, 'All children around the globe', 0, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (14, 6, 'All children involved in Slum Soccer', 1, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (16, 6, 'All children involved in Slum Soccer who have a signature from their parents', 0, 0);",
            # Quiz 3
            "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES(7, 2, 3, 10, 0, 'multiple_choice', 'What is the correct statement from the choices bellow?', 'Question 2', 'Select one answer from the answers provided. Only one of them is correct. When you feel ready click continue to continue with the test.');",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (17, 7, 'A child is defined as a person between 5 and 18 years of age.', 0, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (18, 7, 'Disabled children don t need to be taken into account as all children should be treated equally.', 0, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (19, 7, 'Slum Soccer has a duty of care to safeguard all children involved in Slum Soccer from Slum Soccer enemies.', 0, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (20, 7, 'Adherance to the Child Protection guidelines ensures the safety and protection of children in Slum Soccer.', 1, 0);",
            # Quiz 4 - Info Page
            "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES (8, 2, 4, 0, 0, 'info', 'The aim of the Slum Soccer Child Protection Policy is to promote good practice by: Firstly, providing children and young people with appropriate safety and protection whilst in the care of Slum Soccer. Sceondly, allow all staff/volunteers to make informed and confident responses to specific child protection issues.', 'Policy Aims', 'After leaving this page you won t be able to return. Read carefully.');",
            # Quiz 5
            "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES(9, 2, 5, 10, 0, 'multiple_choice', 'What is the aim of Slum Soccer Child Protectiion Policy?', 'Question 3', 'Select one answer from the answers bellow. Only one of them answers the question correctly. When you feel ready click continue.');",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (21, 9, 'Spread the awaraness of endangerment of human children.', 0, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (22, 9, 'Promote good practice.', 1, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (23, 9, 'Advertise Slum Soccer practices.', 0, 0);",
            # Quiz 6
            "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES(10, 2, 6, 10, 0, 'multiple_choice', 'What doesn t belong among the aims of the Slum Soccer Child Protection Policy?', 'Question 4', 'Only one of them answers is incorrect. Select your answer and when you feel ready click continue.');",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (24, 10, 'Allow all staff /volunteers to make informed and confident responses to specific child protection issues.', 0, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (25, 10, 'Providing children and young people with appropriate safety and protection whilst in the care of Slum Soccer.', 0, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (26, 10, 'Find the most gifted children withing the Slum Soccer and train them to join Slum Soccer Professional Children League.', 1, 0);",

        # Test 3 - empty an locked
        "INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakeable, is_official) VALUES (3, 1, 1, 50, 3, 0, 25, 'This test might looked locked as of now. It is because it is locked and you cannot access it right now.', 1, 1);",
     
        # Test 4 - empty an locked
        "INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakeable, is_official) VALUES (4, 1, 1, 50, 4, 0, 25, 'Can t you believe this? This is locked too. What a nightmare... Maybe you should work harder to unlock it. Or maybe this is just an empty test to show how an unlocked test looks like, since it s quite difficult to create a new test.', 0, 1);",
  
    # Topic 2 - Another Topic
    "INSERT INTO topics (topic_id, is_unlocked, name, needed_credit) VALUES (2, 1, 'Another Topic', 150);",

        # Test 1
        "INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakeable, is_official) VALUES (5, 2, 1, 50, 1, 0, 25, 'This is a practice test teaching you about colours. IT s not official so you can take it as often as you wish.', 1, 0);",
            # Quiz 1 - Info page
            "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, path_to_attachment, text_body, title, instructions) VALUES(11, 5, 1, 0, 0, 'info', 'eye.jpg', 'The ability of the human eye to distinguish colors is based upon the varying sensitivity of different cells in the retina to light of different wavelengths. Humans are trichromatic—the retina contains three types of color receptor cells, or cones. One type, relatively distinct from the other two, is most responsive to light that is perceived as blue or blue-violet, with wavelengths around 450 nm; cones of this type are sometimes called short-wavelength cones or S cones (or misleadingly, blue cones). The other two types are closely related genetically and chemically: middle-wavelength cones, M cones, or green cones are most sensitive to light perceived as green, with wavelengths around 540 nm, while the long-wavelength cones, L cones, or red cones, are most sensitive to light that is perceived as greenish yellow, with wavelengths around 570 nm. Light, no matter how complex its composition of wavelengths, is reduced to three color components by the eye. Each cone type adheres to the principle of univariance, which is that each cone s output is determined by the amount of light that falls on it over all wavelengths. For each location in the visual field, the three types of cones yield three signals based on the extent to which each is stimulated. These amounts of stimulation are sometimes called tristimulus values. The response curve as a function of wavelength varies for each type of cone. Because the curves overlap, some tristimulus values do not occur for any incoming light combination. For example, it is not possible to stimulate only the mid-wavelength so-called green cones; the other cones will inevitably be stimulated to some degree at the same time. The set of all possible tristimulus values determines the human color space. It has been estimated that humans can distinguish roughly 10 million different colors. The other type of light-sensitive cell in the eye, the rod, has a different response curve. In normal situations, when light is bright enough to strongly stimulate the cones, rods play virtually no role in vision at all.[12] On the other hand, in dim light, the cones are understimulated leaving only the signal from the rods, resulting in a colorless response. Furthermore, the rods are barely sensitive to light in the red range. In certain conditions of intermediate illumination, the rod response and a weak cone response can together result in color discriminations not accounted for by cone responses alone. These effects, combined, are summarized also in the Kruithof curve, that describes the change of color perception and pleasingness of light as function of temperature and intensity. SOURCE: https://en.wikipedia.org/wiki/Color', 'Colours in the eye', 'This is an info page... read carefully. PICTURE SOURCE: https://en.wikipedia.org/wiki/Human_eye');",
            # Quiz 2
            "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES(12, 5, 2, 10, 0, 'multiple_choice', 'What is the opposite colour of blue?', 'Question 1', 'Only one of them answers is correct. Select your answer and when you feel ready click continue.');",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (27, 12, 'Red', 0, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (28, 12, 'Yellow', 1, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (29, 12, 'Purple', 0, 0);",
            # Quiz 3
            "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, path_to_attachment, type, text_body, title, instructions) VALUES(13, 5, 3, 10, 0, 'red.jpg','multiple_choice', 'What colour is on the picture?', 'Question 2', 'Only one of them answers is correct. Select your answer and when you feel ready click continue. PICTURE SOURCE: https://colourlex.com/project/chrome-red/');",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (30, 13, 'Red', 1, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (31, 13, 'Blue', 0, 0);",
            # Quiz 4
            "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES(14, 5, 4, 10, 0, 'multiple_choice', 'What color reflects all colours?', 'Question 3', 'Only one of them answers is correct. Select your answer and when you feel ready click continue.');",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (32, 14, 'Yellow', 0, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (33, 14, 'Red', 0, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (34, 14, 'Black', 0, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (35, 14, 'White', 1, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (36, 14, 'Green', 0, 0);",
            # Quiz 5 - Info page
            "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, path_to_attachment,text_body, title, instructions) VALUES(15, 5, 5, 0, 0, 'info', 'brain.jpg', 'While the mechanisms of color vision at the level of the retina are well-described in terms of tristimulus values, color processing after that point is organized differently. A dominant theory of color vision proposes that color information is transmitted out of the eye by three opponent processes, or opponent channels, each constructed from the raw output of the cones: a red–green channel, a blue–yellow channel, and a black–white luminance channel. This theory has been supported by neurobiology, and accounts for the structure of our subjective color experience. Specifically, it explains why humans cannot perceive a reddish green or yellowish blue, and it predicts the color wheel: it is the collection of colors for which at least one of the two color channels measures a value at one of its extremes. The exact nature of color perception beyond the processing already described, and indeed the status of color as a feature of the perceived world or rather as a feature of our perception of the world—a type of qualia—is a matter of complex and continuing philosophical dispute. https://en.wikipedia.org/wiki/Color', 'Colour in the brain', 'This information should be read carefully. You might not be able to see this page again. PICTURE SOURCE: https://slate.com/technology/2016/03/how-big-is-the-brain-who-knows-even-our-best-efforts-to-calculate-its-capacity-are-flawed-and-meaningless.html');",
            # Quiz 6
            "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES(16, 5, 6, 10, 0, 'multiple_choice', 'How many hemispheres does human brain have?', 'Question 4', 'Only one of them answers is correct. Select your answer and when you feel ready click continue.');",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (37, 16, 'Two', 1, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (38, 16, 'None', 0, 0);",
            # Quiz 7
            "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES(17, 5, 7, 10, 0, 'multiple_choice', 'Do all animals see the same colours?', 'Question 5', 'Only one of them answers is correct. Select your answer and when you feel ready click continue.');",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (39, 17, 'No', 1, 0);",
                "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (40, 17, 'Yes', 0, 0);",
 
        # Test 2 - locked and empty
        "INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakeable, is_official) VALUES (6, 2, 0, 20, 2, 0, 10, 'Very interesting test you shall never see.', 1, 1);",
        # Test 3 - locked and empty
        "INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakeable, is_official) VALUES (7, 2, 0, 20, 3, 0, 10, 'Just another empty test that you cannot see being empty.', 1, 1);",
        # Test 4 - locked and empty
        "INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakeable, is_official) VALUES (8, 2, 0, 20, 4, 0, 10, 'Empty as well...', 0, 0);",
        # Test 5 - locked and empty
        "INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakeable, is_official) VALUES (9, 2, 0, 20, 5, 0, 10, 'Nothing to see here', 0, 1);",
        # Test 6 - locked and empty
        "INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakeable, is_official) VALUES (10, 2, 0, 20, 6, 0, 10, 'Empty, lonely just incomplete...', 1, 0);",

    # Topic 3 - Yet One More Topic Here
    "INSERT INTO topics (topic_id, is_unlocked, name, needed_credit) VALUES (3, 0, 'Yet One More Topic Here', 600);",
        # Test 1 - locked and empty
        "INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakeable, is_official) VALUES (11, 3, 1, 100, 1, 0, 50, 'Very small locked test', 1, 0);",
        # Test 2 - locked and empty
        "INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakeable, is_official) VALUES (12, 3, 0, 100, 2, 0, 50, 'Sad test full of emptyness.', 1, 1);",
        # Test 3 - locked and empty
        "INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakeable, is_official) VALUES (13, 3, 0, 100, 3, 0, 50, 'The secrets you shall never see.', 1, 1);",
        # Test 4 - locked and empty
        "INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakeable, is_official) VALUES (14, 3, 0, 100, 4, 0, 50, 'Empty too...', 0, 0);",
        # Test 5 - locked and empty
        "INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakeable, is_official) VALUES (15, 3, 0, 100, 5, 0, 50, 'I was once unlocked I have hread..', 0, 1);",

    # Topic 4 - Topic
    "INSERT INTO topics (topic_id, is_unlocked, name, needed_credit) VALUES (4, 0, 'Topic', 100);",

    # Topic 5 - Topicnic
    "INSERT INTO topics (topic_id, is_unlocked, name, needed_credit) VALUES (5, 0, 'Topicnic', 20);",

    # Topic 6 - Topic of all the topics
    "INSERT INTO topics (topic_id, is_unlocked, name, needed_credit) VALUES (6, 0, 'Topic of all the topics', 10);",

    # Topic 7 - Topic as well
    "INSERT INTO topics (topic_id, is_unlocked, name, needed_credit) VALUES (7, 0, 'Topic as well', 1000);",

    # Topic 8 - Incomplete topic
    "INSERT INTO topics (topic_id, is_unlocked, name, needed_credit) VALUES (8, 0, 'Incomplete topic', 50);",

    # Topic 9 - Very old topic
    "INSERT INTO topics (topic_id, is_unlocked, name, needed_credit) VALUES (9, 0, 'Very old topic', 140);"
)

    # HELP TEMPLATE INSERTS
    # "INSERT INTO topics (topic_id, is_unlocked, name, needed_credit) VALUES (ID, boolUnlocked, 'NAME', neededCred);",
    # "INSERT INTO tests (test_id, topic_id, is_unlocked, max_credit, order_num, gained_credit, pass_credit, description, is_retakeable, is_official) VALUES (ID, topicID, boolUnlocked, maxCred, orderNum, gainedCred, passCred, 'description', boolRetakeable, boolOfficial);",
    # "INSERT INTO quizzes (quiz_id, test_id, order_num, credit_value, gained_credit, type, text_body, title, instructions) VALUES(ID, testID, orderNum, credNum, gainedCred, 'multiple_choice/info', 'mainText', 'title', 'instructions');",
    # "INSERT INTO answers (answer_id, quiz_id, body, is_correct, is_selected) VALUES (ID, quizID, 'text', boolCorrect, boolSelected);",

init_db(insert_queries)