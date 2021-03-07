const mainImage = document.getElementsByClassName('main-img');

window.onload = () => {
    stateHandler.shouldHideHeader();
    
    if (mainImage != null && mainImage.length > 0) { //if there is a dominant image in the page, add the 'window.onscroll()' event listener
        window.onscroll = () => {
            stateHandler.shouldHideHeader();
        }
    }
}

stateHandler = {
    shouldHideHeader: () => {
        if(mainImage != null && mainImage.length > 0) { //we need to check this here also as 'window.onload()' will run this method separately
            /* hide the dominant navbar elements if there is a main background image visible
             * we only do this for the first one as ones lower down in the page would cause the nav bar to hide when the image isn't filling the whole page
             */
            if (events.isOnScreen(mainImage[0]))
                stateHandler.modifyHeader(0, 'var(--transparent)');
            else
                stateHandler.modifyHeader(100, 'var(--header-gradient)');
        }
        else
            stateHandler.modifyHeader(100, 'var(--header-gradient)');
    },

    modifyHeader: (opacity, background) => {
        $('#logo').css({
            'opacity': opacity
        });
        $('#page-header').css({
            'background-image': `${background}`
        });
    }
}

events = {
    isOnScreen: (element) => { //used to determine if an HTML element is on screen - https://stackoverflow.com/a/5354536/11136104
		var rect = element.getBoundingClientRect();
		var viewHeight = Math.max(document.documentElement.clientHeight, window.innerHeight);
		return !(rect.bottom < 0 || rect.top - viewHeight >= 0);
	},

    navOperationClicked: (display) => { //this parameter used to be 'operation', which determined whether we are opening or closing the navigation menu via animation
        $('#nav-menu').css({
            'display': display
            //'animation': `${operation}-mobile-nav 0.5s ease forwards`
        });
    }
}

request = {
    get: ({endpoint, extension=null, data=null, handler}={}) => {
        $.ajax({
            url: extension === null ? `${endpoint}` : `${endpoint}/${extension}`,
            method: "GET",
            data: data,
            success: (data) => {
                if(handler != null && data != null) //if we got data from the backend and we have something to do with it
                    handler(data); //handler is the method (based on the parameter) that used the data from this request
            }
        });

        //old implementation of doing a GET request
        /*$.get(`/${endpoint}/${extension}`, (data) => {
            handler(data); //'handler' is the JavaScript function that will handle the data returned from the backend
        });*/
    },
}

requestHandlers = {
    listTopics: (data) => {
        if(data != null) {
            for(let i = 0; i < data.topics.length; i++) {
                const topic = data.topics[i];

                //this topic's container in the menu
                var topicItem = document.createElement('div');
                topicItem.className = "topic-item";

                //the element in the container which displays this topic's name
                var topicItemName = document.createElement('b');
                topicItemName.className = "topic-name";
                topicItemName.innerHTML = topic.name;
                topicItem.appendChild(topicItemName);

                //the line in the container that separates the name and buttons
                var topicItemLine = document.createElement('div');
                topicItemLine.className = "topics-line";
                topicItem.appendChild(topicItemLine);

                //the container, in this topic's container, which contains the buttons
                var topicItemLevels = document.createElement('div');
                topicItemLevels.className = "topic-levels";
                topicItem.appendChild(topicItemLevels);

                //for every test in this topic, add a button to the button container for it
                for(let j = 0; j < topic.tests.length; j++) {
                    var topicItemLevel = document.createElement('button');
                    topicItemLevel.innerHTML = j + 1;
                    topicItemLevel.className = "level-button";

                    topicItemLevel.setAttribute('data-test_id', topic.tests[j].test_id); //store the ID of the test in which this button relates to
                    topicItemLevel.addEventListener("click", (event) => { //'event' is used to get the HTML element which this event is attached to
                        storageUtils.storeSessionValue(storageUtils.testID, event.target.getAttribute('data-test_id')); //get the ID and store it in the session so it's carried over to 'quiz-page'
                        window.location.href = Flask.url_for('quiz_page');
                    });

                    topicItemLevels.appendChild(topicItemLevel);
                }

                document.getElementById('topics-menu').appendChild(topicItem);
            }
        }
    },

    displayTest: (data) => { // ----- TODO ----- it may be better to store the data in session storage as it will be easier to record and manage
        storageUtils.removeSessionValue(storageUtils.testID);
        storageUtils.storeSessionValue(storageUtils.testDataID, data);

        quiz.length = data.quizzes.length;

        const navbar = document.getElementById('quizzes-navigation');
        for(let i = 0; i < quiz.length; i++) {
            var navButton = document.createElement('button');
            navButton.innerHTML = i + 1;
            navButton.className = "level-button quizzes-navigation-btn";

            navButton.setAttribute('data-quiz_id', i + 1);
            navButton.addEventListener("click", (event) => {
                quiz.navigateQuestion(parseInt(event.target.getAttribute('data-quiz_id')));
            });

            navbar.appendChild(navButton);
        }

        if(data.quizzes != null && quiz.length > 0)
            quiz.loadQuestion(quiz.findQuestion(data.quizzes, 1));
        else 
            throw Error(`There are no questions available for the test with ID ${data.test_id}`);
    }
}

quiz = {
    length: null,
    currentQuestion: 1,

    navigateQuestion: (question) => {
        const data = storageUtils.getSessionValue(storageUtils.testDataID);
        quiz.loadQuestion(quiz.findQuestion(data.quizzes, question));
    },

    findQuestion: (questions, order_num) => {
        for(let i = 0; i < quiz.length; i++)
            if(questions[i].order_num === order_num)
                return questions[i];
    },

    loadQuestion: (question) => {
        console.log(question);
        if(question !== null) {
            document.getElementById('quiz-title').innerHTML = question.title;
            document.getElementById('quiz-instructions').innerHTML = question.instructions;
            document.getElementById('quiz-text').innerHTML = question.text_body;

            if(question.answers != null && question.answers.length > 0) {
                // ----- TODO ----- check if a path to an image is present and if it is, try to display it

                const answersSection = document.getElementById('quiz-radio-section');
                
                while(answersSection.hasChildNodes())
                    answersSection.removeChild(answersSection.firstChild);

                for(let i = 0; i < question.answers.length; i++) {
                    const answer = question.answers[i];

                    var answerContainer = document.createElement('div');
                    answerContainer.className = "row quiz-radio-row";

                    var answerButton = document.createElement('input');
                    answerButton.type = 'radio';
                    answerButton.id = answer.answer_id;
                    answerButton.name = answer.type;
                    answerButton.value = answer.answer_id;
                    answerButton.className = "quiz-radio-btn";
                    answerContainer.appendChild(answerButton);

                    var buttonLabel = document.createElement('label');
                    buttonLabel.htmlFor = answer.answer_id;
                    buttonLabel.innerHTML = answer.body;
                    answerContainer.appendChild(buttonLabel);

                    /* doesn't work - switch to CSS padding instead
                    var br = document.createElement('br');
                    answerContainer.appendChild(br); */

                    answersSection.appendChild(answerContainer);
                }

                const backContainer = document.getElementsByClassName('quiz-back-space')[0];
                if(quiz.currentQuestion !== 1) {
                    if(backContainer.children.length === 0) {
                        var backButton = document.createElement('button');
                        backButton.className = "quiz-btn";
                        backButton.innerHTML = "Back";

                        backButton.addEventListener("click", (event) => {
                            quiz.navigateQuestion(--quiz.currentQuestion < 1 ? ++quiz.currentQuestion : quiz.currentQuestion); //this tenerary operator prevents the number from going out of bounds - take away 1 then if it is lower than the minimum (1), add 1, otherwise use the number with 1 subtracted
                        });

                        backContainer.appendChild(backButton);
                    }
                }
                else {
                    if(backContainer.children.length > 0)
                        backContainer.removeChild(backContainer.children[0]); //there will only ever be 1 child: the button
                }

                const continueContainer = document.getElementsByClassName('quiz-continue-space')[0]
                if(continueContainer.children.length === 0) {
                    var continueButton = document.createElement('button');
                    continueButton.className = "quiz-btn";
                    continueButton.innerHTML = quiz.currentQuestion === quiz.length ? "Finish" : "Continue"; //tenerary operator here also as there may only be one question in the quiz

                    continueButton.addEventListener("click", (event) => {
                        quiz.navigateQuestion(++quiz.currentQuestion > quiz.length ? --quiz.currentQuestion : quiz.currentQuestion); //same as the tenerary operator in the listener above, but inverse
                    });

                    continueContainer.appendChild(continueButton);
                }
                else
                    continueContainer.children[0].innerHTML = quiz.currentQuestion === quiz.length ? "Finish" : "Continue";
            }
            else
                throw Error(`There are no answers available for the question with ID ${question.quiz_id}`);
        }
        else 
            throw Error('There was no question specified');
    }
}

storageUtils = { //only session storage is implemented here as we do not have a need to store anything persistently in local
    //key words which identify data that will be placed in storage
    testID: "test_id",
    testDataID: "test_data",

    isObject: (obj) => { //credit - https://attacomsian.com/blog/javascript-check-variable-is-object
        return Object.prototype.toString.call(obj) === '[object Object]';
    },

    storeSessionValue: (name, value) => {
        try { //tries to store the data in temporary storage
            if(name != null && typeof name === "string" && value != null) {
                window.sessionStorage.setItem(name, storageUtils.isObject(value) ? JSON.stringify(value) : value); //JavaScript objects cannot be stored so we need to convert it to a JSON
                return true;
            }
            else
                throw Error('Invalid storage name or null name/value');
        }
        catch (e) {
            //checks if storage didn't fail because it is full (returns true if it did) - the oly other reason it would fail is if storage is made unavailable
            return e instanceof DOMException && (
                   e.code === 22 ||
                   e.code === 1014 ||
                   e.name === 'QuotaExceededError' ||
                   e.name === 'NS_ERROR_DOM_QUOTA_REACHED') &&
                   storage.length !== 0;
        }
    },

    getSessionValue: (name) => {
        try {
            var value = window.sessionStorage.getItem(name);
            try {
                return JSON.parse(value); //because we need to serilize an object, we also need to convert it from JSON back to an object
            }
            catch {
                return value;
            }
        }
        catch(e) {
            return null;
        }
    },
    
    removeSessionValue: (name) => {
        try {
            if(window.sessionStorage.getItem(name) !== null) {
                window.sessionStorage.removeItem(name);
                return true;
            }
            throw Error(`Item \"${name}\" does not exist in local storage`);
        }
        catch(e) {
            return false;
        }
    }
}