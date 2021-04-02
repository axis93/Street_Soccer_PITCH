from models.topic import TopicModel
from models.test import TestModel
from models.formativeAssessment import FormativeAssessmentModel
from models.quiz import QuizModel
from models.answer import AnswerModel

def insert_test_data(): # these are queries used only for inserting test data, this should not be needed once the form to make quizzes is implemented
    # Topic 1 - Child Protection Policy
    TopicModel(1, 1, 'Child Protection Policy', 100).save_to_database()
    # Test 1
    TestModel(1, 1, 1, 30, 1, 0, 15, None, 'This test will cover the introduction to Child Protection Policy.', 1, 1).save_to_database()
    # Quiz 1
    QuizModel(1, 1, 1, 10, 0, 'multiple_choice', 'What should be avoided except in emergencies?', None, 'Question 1', 'To complete this quiz please select an answer and then click next. You can, however, come to the question later and change your answer.').save_to_database()
    AnswerModel(1, 1, 'Spending time alone with children away from others', 1, None, 0).save_to_database()
    AnswerModel(2, 1, 'Making sport fun and enjoyable', 0, None, 0).save_to_database()
    AnswerModel(3, 1, 'Promoting fair play', 0, None, 0).save_to_database()
    # Quiz 2
    QuizModel(2, 1, 2, 10, 0, 'multiple_choice', 'Choose the most appropriate from the following options that best describes the aim of the Child Protection Policy:', None, 'Question 2', 'To complete this quiz please select an answer and then click next').save_to_database()
    AnswerModel(4, 2, 'Children should be safely protected with appropriate gear, so that we can minimize injuries to happen', 0, None, 0).save_to_database()
    AnswerModel(5, 2, 'Make sure that every young person can integrate with each other, in a safe and positive environment', 0, None, 0).save_to_database()
    AnswerModel(6, 2, 'Promoting good practice by providing young people with appropriate safety and protection, whilst in care of Slum Soccer', 1, None, 0).save_to_database()
    # Quiz 3 - Info Page
    QuizModel(3, 1, 3, 0, 0, 'info', 'Any  suspicion  that  a  child  has  been  abused  by  either a  member of  staff  or a  volunteer should  be reported  to  the  Slum  Soccer  Child  Protection  Officer, who  will take  such  steps  as considered necessary  to  ensure  the  safety  of  the  child  in  question  and  any  other child  who  may  be  at  risk. The  Slum  Soccer  Child  Protection  Officer will  refer the  allegation  to  the  social services department  who  may  involve  the  police. The  parents  or carers  of  the  child  will be  contacted  as soon  as possible  following  advice  from the  social services  department. The  Slum  Soccer  Child  Protection  Officer should  also  notify  the  relevant  Sport  Governing Body  officer who  in  turn  will inform  the  Sport  Governing  Body  Child  Protection  Officer who  will deal with  any  media  enquiries. If  the  Slum  Soccer  Child  Protection  Officer is the  subject  of  the  suspicion/allegation,  the  report must  be  made  to  the  appropriate  Manager or  in  his/her absence  the  Sport Governing Body  Child  Protection  Officer who  will  refer  the  allegation  to  Social  Services. ', 'cps.jpg', 'Reporting  concerns about  suspected abuse ', 'Read carefully the text and when you are ensure you understand everything, click next. You won t be able to return to this page when you leave it, so read carefully.').save_to_database()
    # Quiz 4
    QuizModel(4, 1, 4, 10, 0, 'multiple_choice', 'If there is suspicion that a child has been abused by either a member of staff or a volunteer, what is the order of people/roles to be appointed and the steps as considered necessary to be undertaken?', None, 'Question 4', 'To complete this quiz please select an answer and then click next').save_to_database()
    AnswerModel(10, 4, 'It should be reported to the appropriate Manager who will refer to the Slum Soccer Child Protection Officer who will contact the police or any social services department', 0, None, 0).save_to_database()
    AnswerModel(11, 4, 'It should be reported to the Slum Soccer Child Protection Officer, who will refer to the social services department. He should also notify the relevant Sport Governing body office',1, None, 0).save_to_database()
    AnswerModel(12, 4, 'It should be reported to the police that after their investigations, will contact the Slum Soccer Child Protection Officer, who will inform the Sport Governing Body Child Protection Officer', 0, None, 0).save_to_database()

    # Test 2
    TestModel(2, 1, 1, 40, 2, 0, 20, None, 'This test tests you on the aim of the Child Protection Policy. You have only one attempt for this test.', 0, 1).save_to_database()
    # Quiz 1 - Info Page
    QuizModel(5, 2, 1, 0, 0, 'info', 'Slum Soccer has a duty of care to safeguard all children involved in Slum Soccer from harm. All children have a right to protection, and the needs of disabled children and others who may be particularly vulnerable must be taken into account. Slum Soccer will ensure the safety and protection of all children involved in Slum Soccer through adherence to the Child Protection guidelines adopted by Slum Soccer. A child is defined as a person under the age of 18.', None, 'Aim of the Child Protection Policy', 'After leaving this page you won t be able to return. Read carefully.').save_to_database()
    # Quiz 2
    QuizModel(6, 2, 2, 10, 0, 'multiple_choice', 'What children does Slum Soccer ensures safety and protection to?', None, 'Question 1', 'Select your answer and click on continue...').save_to_database()
    AnswerModel(13, 6, 'All children around the globe', 0, None, 0).save_to_database()
    AnswerModel(14, 6, 'All children involved in Slum Soccer', 1, None, 0).save_to_database()
    AnswerModel(16, 6, 'All children involved in Slum Soccer who have a signature from their parents', 0, None, 0).save_to_database()
    # Quiz 3
    QuizModel(7, 2, 3, 10, 0, 'multiple_choice', 'What is the correct statement from the choices bellow?', None, 'Question 2', 'Select one answer from the answers provided. Only one of them is correct. When you feel ready click continue to continue with the test.').save_to_database()
    AnswerModel(17, 7, 'A child is defined as a person between 5 and 18 years of age.', 0, None, 0).save_to_database()
    AnswerModel(18, 7, 'Disabled children don t need to be taken into account as all children should be treated equally.', 0, None, 0).save_to_database()
    AnswerModel(19, 7, 'Slum Soccer has a duty of care to safeguard all children involved in Slum Soccer from Slum Soccer enemies.', 0, None, 0).save_to_database()
    AnswerModel(20, 7, 'Adherance to the Child Protection guidelines ensures the safety and protection of children in Slum Soccer.', 1, None, 0).save_to_database()
    # Quiz 4 - Info Page
    QuizModel(8, 2, 4, 0, 0, 'info', 'The aim of the Slum Soccer Child Protection Policy is to promote good practice by: Firstly, providing children and young people with appropriate safety and protection whilst in the care of Slum Soccer. Sceondly, allow all staff/volunteers to make informed and confident responses to specific child protection issues.', None, 'Policy Aims', 'After leaving this page you won t be able to return. Read carefully.').save_to_database()
    # Quiz 5
    QuizModel(9, 2, 5, 10, 0, 'multiple_choice', 'What is the aim of Slum Soccer Child Protectiion Policy?', None, 'Question 3', 'Select one answer from the answers bellow. Only one of them answers the question correctly. When you feel ready click continue.').save_to_database()
    AnswerModel(21, 9, 'Spread the awaraness of endangerment of human children.', 0, None, 0).save_to_database()
    AnswerModel(22, 9, 'Promote good practice.', 1, None, 0).save_to_database()
    AnswerModel(23, 9, 'Advertise Slum Soccer practices.', 0, None, 0).save_to_database()
    # Quiz 6
    QuizModel(10, 2, 6, 10, 0, 'multiple_choice', 'What doesn t belong among the aims of the Slum Soccer Child Protection Policy?', None, 'Question 4', 'Only one of them answers is incorrect. Select your answer and when you feel ready click continue.').save_to_database()
    AnswerModel(24, 10, 'Allow all staff /volunteers to make informed and confident responses to specific child protection issues.', 0, None, 0).save_to_database()
    AnswerModel(25, 10, 'Providing children and young people with appropriate safety and protection whilst in the care of Slum Soccer.', 0, None, 0).save_to_database()
    AnswerModel(26, 10, 'Find the most gifted children withing the Slum Soccer and train them to join Slum Soccer Professional Children League.', 1, None, 0).save_to_database()

    # Test 3 - empty an locked
    TestModel(3, 1, 0, 50, 3, 0, 25, None, 'This test might looked locked as of now. It is because it is locked and you cannot access it right now.', 1, 1).save_to_database()
    # Test 4 - empty an locked
    TestModel(4, 1, 0, 50, 4, 0, 25, None, 'Can t you believe this? This is locked too. What a nightmare... Maybe you should work harder to unlock it. Or maybe this is just an empty test to show how an unlocked test looks like, since it s quite difficult to create a new test.', 0, 1).save_to_database()
    
    # Topic 2 - Another Topic
    TopicModel(2, 1, 'Another Topic', 120).save_to_database()
    # Test 1
    TestModel(5, 2, 1, 50, 1, 0, 25, None, 'This is a practice test teaching you about colours. IT s not official so you can take it as often as you wish.', 1, 0).save_to_database()
    # Quiz 1 - Info page
    QuizModel(11, 5, 1, 0, 0, 'info', 'The ability of the human eye to distinguish colors is based upon the varying sensitivity of different cells in the retina to light of different wavelengths. Humans are trichromatic—the retina contains three types of color receptor cells, or cones. One quiz_type, relatively distinct from the other two, is most responsive to light that is perceived as blue or blue-violet, with wavelengths around 450 nm; cones of this quiz_type are sometimes called short-wavelength cones or S cones (or misleadingly, blue cones). The other two types are closely related genetically and chemically: middle-wavelength cones, M cones, or green cones are most sensitive to light perceived as green, with wavelengths around 540 nm, while the long-wavelength cones, L cones, or red cones, are most sensitive to light that is perceived as greenish yellow, with wavelengths around 570 nm. Light, no matter how complex its composition of wavelengths, is reduced to three color components by the eye. Each cone quiz_type adheres to the principle of univariance, which is that each cone s output is determined by the amount of light that falls on it over all wavelengths. For each location in the visual field, the three types of cones yield three signals based on the extent to which each is stimulated. These amounts of stimulation are sometimes called tristimulus values. The response curve as a function of wavelength varies for each quiz_type of cone. Because the curves overlap, some tristimulus values do not occur for any incoming light combination. For example, it is not possible to stimulate only the mid-wavelength so-called green cones; the other cones will inevitably be stimulated to some degree at the same time. The set of all possible tristimulus values determines the human color space. It has been estimated that humans can distinguish roughly 10 million different colors. The other quiz_type of light-sensitive cell in the eye, the rod, has a different response curve. In normal situations, when light is bright enough to strongly stimulate the cones, rods play virtually no role in vision at all.[12] On the other hand, in dim light, the cones are understimulated leaving only the signal from the rods, resulting in a colorless response. Furthermore, the rods are barely sensitive to light in the red range. In certain conditions of intermediate illumination, the rod response and a weak cone response can together result in color discriminations not accounted for by cone responses alone. These effects, combined, are summarized also in the Kruithof curve, that describes the change of color perception and pleasingness of light as function of temperature and intensity. SOURCE: https://en.wikipedia.org/wiki/Color', 'eye.jpg', 'Colours in the eye', 'This is an info page... read carefully. PICTURE SOURCE: https://en.wikipedia.org/wiki/Human_eye').save_to_database()
    # Quiz 2
    QuizModel(12, 5, 2, 10, 0, 'multiple_choice', 'What is the opposite colour of blue?', None, 'Question 1', 'Only one of them answers is correct. Select your answer and when you feel ready click continue.').save_to_database()
    AnswerModel(27, 12, 'Red', 0, None, 0).save_to_database()
    AnswerModel(28, 12, 'Yellow', 1, None, 0).save_to_database()
    AnswerModel(29, 12, 'Purple', 0, None, 0).save_to_database()
    # Quiz 3
    QuizModel(13, 5, 3, 10, 0, 'multiple_choice', 'What colour is on the picture?', 'red.jpg', 'Question 2', 'Only one of them answers is correct. Select your answer and when you feel ready click continue. PICTURE SOURCE: https://colourlex.com/project/chrome-red/').save_to_database()
    AnswerModel(30, 13, 'Red', 1, None, 0).save_to_database()
    AnswerModel(31, 13, 'Blue', 0, None, 0).save_to_database()
    # Quiz 4
    QuizModel(14, 5, 4, 10, 0, 'multiple_choice', 'What color reflects all colours?', None, 'Question 3', 'Only one of them answers is correct. Select your answer and when you feel ready click continue.').save_to_database()
    AnswerModel(32, 14, 'Yellow', 0, None, 0).save_to_database()
    AnswerModel(33, 14, 'Red', 0, None, 0).save_to_database()
    AnswerModel(34, 14, 'Black', 0, None, 0).save_to_database()
    AnswerModel(35, 14, 'White', 1, None, 0).save_to_database()
    AnswerModel(36, 14, 'Green', 0, None, 0).save_to_database()
    # Quiz 5 - Info page
    QuizModel(15, 5, 5, 0, 0, 'info', 'While the mechanisms of color vision at the level of the retina are well-described in terms of tristimulus values, color processing after that point is organized differently. A dominant theory of color vision proposes that color information is transmitted out of the eye by three opponent processes, or opponent channels, each constructed from the raw output of the cones: a red–green channel, a blue–yellow channel, and a black–white luminance channel. This theory has been supported by neurobiology, and accounts for the structure of our subjective color experience. Specifically, it explains why humans cannot perceive a reddish green or yellowish blue, and it predicts the color wheel: it is the collection of colors for which at least one of the two color channels measures a value at one of its extremes. The exact nature of color perception beyond the processing already described, and indeed the status of color as a feature of the perceived world or rather as a feature of our perception of the world—a quiz_type of qualia—is a matter of complex and continuing philosophical dispute. https://en.wikipedia.org/wiki/Color', 'brain.jpg', 'Colour in the brain', 'This information should be read carefully. You might not be able to see this page again. PICTURE SOURCE: https://slate.com/technology/2016/03/how-big-is-the-brain-who-knows-even-our-best-efforts-to-calculate-its-capacity-are-flawed-and-meaningless.html').save_to_database()
    # Quiz 6
    QuizModel(16, 5, 6, 10, 0, 'multiple_choice', 'How many hemispheres does human brain have?', None, 'Question 4', 'Only one of them answers is correct. Select your answer and when you feel ready click continue.').save_to_database()
    AnswerModel(37, 16, 'Two', 1, None, 0).save_to_database()
    AnswerModel(38, 16, 'None', 0, None, 0).save_to_database()
    # Quiz 7
    QuizModel(17, 5, 7, 10, 0, 'multiple_choice', 'Do all animals see the same colours?', None, 'Question 5', 'Only one of them answers is correct. Select your answer and when you feel ready click continue.').save_to_database()
    AnswerModel(39, 17, 'No', 1, None, 0).save_to_database()
    AnswerModel(40, 17, 'Yes', 0, None, 0).save_to_database()
    
    # Test 2
    TestModel(6, 2, 1, 20, 2, 0, 10, None, 'Koalas.. just koalas', 1, 1).save_to_database()
    # Quiz 1 - Info page
    QuizModel(18, 6, 1, 0, 0, 'info', 'This is a video about koalas, watch it.', 'https://www.youtube.com/embed/oI3ADcDH0Uc', 'Koalas', 'Watch it carefully and as many times as you want. However when you leave this page you cannot return. VIDEO SOURCE: https://www.youtube.com/watch?v=oI3ADcDH0Uc').save_to_database()
    # Quiz 2
    QuizModel(19, 6, 2, 10, 0, 'multiple_choice', 'How many species of Eucalypt do koalas prefer?', None, 'Question 1', 'Only one of them answers is correct. Select your answer and when you feel ready click continue.').save_to_database()
    AnswerModel(41, 19, '3', 0, None, 0).save_to_database()
    AnswerModel(42, 19, '30', 1, None, 0).save_to_database()
    AnswerModel(43, 19, '65', 0, None, 0).save_to_database()
    AnswerModel(44, 19, '6', 0, None, 0).save_to_database()
    AnswerModel(45, 19, '650', 0, None, 0).save_to_database()
    # Quiz 3
    QuizModel(20, 6, 3, 10, 0, 'multiple_choice', 'How many hours a day do koalas sleep?', 'https://www.youtube.com/embed/NnRcxHreJFM', 'Question 2', 'Only one of them answers is correct. Select your answer and when you feel ready click continue. VIDEO SOURCE: https://www.youtube.com/watch?v=NnRcxHreJFM').save_to_database()
    AnswerModel(46, 20, 'They can sleep for days.', 0, None, 0).save_to_database()
    AnswerModel(47, 20, 'Around 12 hours a day', 0, None, 0).save_to_database()
    AnswerModel(48, 20, 'Up to 20 hours a day.', 0, None, 0).save_to_database()
    AnswerModel(49, 20, 'Up to 22 hours a day.', 1, None, 0).save_to_database()
    

    # Test 3 - locked and empty
    TestModel(7, 2, 0, 20, 3, 0, 10, None, 'Just another empty test that you cannot see being empty.', 1, 1).save_to_database()
    # Test 4 - locked and empty
    TestModel(8, 2, 0, 20, 4, 0, 10, None, 'Empty as well...', 0, 0).save_to_database()
    # Test 5 - locked and empty
    TestModel(9, 2, 0, 20, 5, 0, 10, None, 'Nothing to see here', 0, 1).save_to_database()
    # Test 6 - locked and empty
    TestModel(10, 2, 0, 20, 6, 0, 10, None, 'Empty, lonely just incomplete...', 1, 0).save_to_database()

    # FA 1 - not started
    FormativeAssessmentModel(1, 2, 1, 1, 40, 0, None, 20, 'Write an essay of 2000 words comparing the life of koalas in captivity and in wilderness. You can gain maximum of 40 credits. For passing the module you need 20 credits. IMG SOURCE: https://en.wikipedia.org/wiki/Koala', 'Compare the life of koalas in captivity and in wilderness', 'koala.png', '1/6/2021', None, 0).save_to_database()
    # FA 2 - answered
    FormativeAssessmentModel(2, 2, 1, 2, 20, 0, 'my_colour_essay.docx', 10, 'Write an essay of 1500 words about the colour perception through a human eye. You can gain maximum of 20 credits. For passing the module you need 10 credits.', 'Colours through the eye', None, '20/4/2021', None, 0).save_to_database()
    # FA 3 - reviewed
    FormativeAssessmentModel(3, 2, 1, 3, 30, 16, 'self_reflection.docx', 15, 'Write a self reflection about your progress and improvements during this topic. It can be maximum 1000 words. You can gain maximum of 30 credits. For passing the module you need 15 credits. VIDEO SOURCE: https://www.youtube.com/watch?v=avHRLqVPYwg', 'Self reflection', 'https://www.youtube.com/embed/avHRLqVPYwg', '1/3/2021', 'Good job. But there is a lack of detail in the progress section. Be more specific about how you have improved.', 1). save_to_database()


    # Topic 3 - Yet One More Topic Here
    TopicModel(3, 0, 'Yet One More Topic Here', 250).save_to_database()
    # Test 1 - locked and empty
    TestModel(11, 3, 0, 100, 1, 0, 50, None, 'Very small locked test', 1, 0).save_to_database()
    # Test 2 - locked and empty
    TestModel(12, 3, 0, 100, 2, 0, 50, None, 'Sad test full of emptyness.', 1, 1).save_to_database()
    # Test 3 - locked and empty
    TestModel(13, 3, 0, 100, 3, 0, 50, None, 'The secrets you shall never see.', 1, 1).save_to_database()
    # Test 4 - locked and empty
    TestModel(14, 3, 0, 100, 4, 0, 50, None, 'Empty too...', 0, 0).save_to_database()
    # Test 5 - locked and empty
    TestModel(15, 3, 0, 100, 5, 0, 50, None, 'I was once unlocked I have hread..', 0, 1).save_to_database()

    # Topic 4 - Topic
    TopicModel(4, 0, 'Topic', 60).save_to_database()
    # Test 1 - locked and empty
    TestModel(16, 4, 0, 50, 1, 0, 25, None, 'Nothin..', 1, 0).save_to_database()
    # Test 2 - locked and empty
    TestModel(17, 4, 0, 50, 2, 0, 25, None, 'Empty', 1, 1).save_to_database()
    # FA 1
    FormativeAssessmentModel(4, 4, 1, 1, 20, 0, None, 10, 'Write an essay of 2000 words. You can gain maximum of 40 credits. For passing the module you need 20 credits.', 'Some title', None, '5/6/2021', None, 0).save_to_database()
    # FA 2
    FormativeAssessmentModel(5, 4, 1, 2, 20, 0, None, 10, 'Write an essay of 5000 words. You can gain maximum of 40 credits. For passing the module you need 20 credits.', 'Some title 2', None, '17/6/2021', None, 0).save_to_database()


    # Topic 5 - Topicnic
    TopicModel(5, 0, 'Topicnic', 12).save_to_database()
    # Test 1 - locked and empty
    TestModel(18, 5, 0, 5, 1, 0, 3, None, 'Locked test', 1, 0).save_to_database()
    # Test 2 - locked and empty
    TestModel(19, 5, 0, 5, 2, 0, 3, None, 'Test of emptyness.', 1, 1).save_to_database()
    # Test 3 - locked and empty
    TestModel(20, 5, 0, 5, 3, 0, 3, None, 'The secrets...', 1, 1).save_to_database()
    # Test 4 - locked and empty
    TestModel(21, 5, 0, 5, 4, 0, 3, None, 'Empty2', 0, 0).save_to_database()

    # Topic 6 - Topic of all the topics
    TopicModel(6, 0, 'Topic of all the topics', 5).save_to_database()
    # Test 1 - locked and empty
    TestModel(22, 6, 0, 10, 1, 0, 5, None, 'ONLY ONE TEST BUT IT S HARD', 1, 0).save_to_database()

    # Topic 7 - Topic as well
    TopicModel(7, 0, 'Topic as well', 500).save_to_database()
    # Test 1 - locked and empty
    TestModel(23, 7, 0, 333, 1, 0, 150, None, 'Smallest Test', 1, 0).save_to_database()
    # Test 2 - locked and empty
    TestModel(24, 7, 0, 333, 2, 0, 200, None, 'Smaller Test', 1, 1).save_to_database()
    # Test 3 - locked and empty
    TestModel(25, 7, 0, 334, 3, 0, 250, None, 'Small Test', 1, 1).save_to_database()

    # Topic 8 - Incomplete topic
    TopicModel(8, 0, 'Incomplete topic', 25).save_to_database()
    # Test 1 - locked and empty
    TestModel(26, 8, 0, 10, 1, 0, 5, None, 'Very small locked test', 1, 0).save_to_database()
    # Test 2 - locked and empty
    TestModel(27, 8, 0, 10, 2, 0, 5, None, 'VERY LOCKED.', 1, 1).save_to_database()
    # Test 3 - locked and empty
    TestModel(28, 8, 0, 10, 3, 0, 5, None, 'Nothing to see here in this world.', 1, 1).save_to_database()
    # Test 4 - locked and empty
    TestModel(29, 8, 0, 10, 4, 0, 5, None, 'Sorry, empty', 0, 0).save_to_database()
    # Test 5 - locked and empty
    TestModel(30, 8, 0, 10, 5, 0, 5, None, 'I am empty', 0, 1).save_to_database()
    # FA 1
    FormativeAssessmentModel(6, 8, 1, 1, 20, 0, None, 10, 'Write an essay of 5000 words. You can gain maximum of 40 credits. For passing the module you need 20 credits.', 'Some great title', None, '30/6/2021', None, 0).save_to_database()


    # Topic 9 - Very old topic
    TopicModel(9, 0, 'Very old topic', 75).save_to_database()
    # Test 1 - locked and empty
    TestModel(31, 9, 0,70, 1, 0, 35, None, 'I am first but locked.', 1, 0).save_to_database()
    # Test 2 - locked and empty
    TestModel(32, 9, 0, 70, 2, 0, 35, None, 'I am second but locked.', 1, 1).save_to_database()