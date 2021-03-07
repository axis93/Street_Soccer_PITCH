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
            if (events.isOnScreen(mainImage[0])) //hide the dominant navbar elements if there is a main background image visible - we only do this for the first one as ones lower down in the page would cause the nav bar to hide when the image isn't filling the whole page
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
                var topicItem = elemUtils.createElement({type: 'div', className: "topic-item", parent: document.getElementById('topics-menu')})

                //the element in the container which displays this topic's name
                elemUtils.createElement({type: 'b', className: "topic-name", innerHTML: topic.name, parent: topicItem});

                //the line in the container that separates the name and buttons
                elemUtils.createElement({type: 'div', className: "topics-line", parent: topicItem});

                //the container, in this topic's container, which contains the buttons
                var topicItemLevels = elemUtils.createElement({type: 'div', className: "topic-levels", parent: topicItem});

                //for every test in this topic, add a button to the button container for it
                for(let j = 0; j < topic.tests.length; j++) {
                    var topicItemLevel = elemUtils.createElement({type: 'button', className: "level-button", innerHTML: j + 1, parent: topicItemLevels});

                    topicItemLevel.setAttribute('data-test_id', topic.tests[j].test_id); //store the ID of the test in which this button relates to
                    topicItemLevel.addEventListener("click", (event) => { //'event' is used to get the HTML element which this event is attached to
                        storageUtils.storeSessionValue(storageUtils.testID, event.target.getAttribute('data-test_id')); //get the ID and store it in the session so it's carried over to 'quiz-page'
                        window.location.href = Flask.url_for('quiz_page');
                    });
                }
            }
        }
    },

    displayTest: (data) => {
        storageUtils.removeSessionValue(storageUtils.testID);
        storageUtils.storeSessionValue(storageUtils.testDataID, data);

        quiz.length = data.quizzes.length;

        const navbar = document.getElementById('quizzes-navigation');
        for(let i = 0; i < quiz.length; i++) {
            var navButton = elemUtils.createElement({type: 'button', className: "level-button quizzes-navigation-btn", innerHTML: i + 1, parent: navbar});
            navButton.setAttribute('data-quiz_id', i + 1);
            navButton.addEventListener("click", (event) => {
                var questionNumber = parseInt(event.target.getAttribute('data-quiz_id'));
                quiz.navigateToQuestion(questionNumber);

                //update the question number then update the appropriate elements, based on this change (back button availability and continue button text)
                quiz.currentQuestion = questionNumber;
                elemUtils.checkBackButton();
                document.getElementsByClassName('quiz-continue-space')[0].children[0].innerHTML = questionNumber === quiz.length ? "Finish" : "Continue";
            });
        }

        if(data.quizzes != null && quiz.length > 0)
            quiz.loadQuestion(quiz.findNextQuestion(data.quizzes, 1));
        else 
            throw Error(`There are no questions available for the test with ID ${data.test_id}`);
    }
}

quiz = {
    length: null,
    currentQuestion: 1,

    navigateToQuestion: (question) => {
        const data = storageUtils.getSessionValue(storageUtils.testDataID);
        quiz.loadQuestion(quiz.findNextQuestion(data.quizzes, question));
    },

    findNextQuestion: (questions, order_num) => {
        for(let i = 0; i < quiz.length; i++)
            if(questions[i].order_num === order_num)
                return questions[i];
    },

    loadQuestion: (question) => {
        if(question !== null) {
            document.getElementById('quiz-title').innerHTML = question.title;
            document.getElementById('quiz-instructions').innerHTML = question.instructions;
            document.getElementById('quiz-text').innerHTML = question.text_body;

            if(question.answers != null && question.answers.length > 0) {
                const answersSection = document.getElementById('quiz-radio-section');
                
                while(answersSection.hasChildNodes())
                    answersSection.removeChild(answersSection.firstChild);

                var attachmentContainer = document.getElementsByClassName('column quiz-attachment')[0];
                if(question.path_to_attachment != null) {
                    if(attachmentContainer == null) { //if an image doesn't already exist, create a container for a new one and add an image to it
                        attachmentContainer = elemUtils.createElement({type: 'div', className: "column quiz-attachment", parent: document.getElementsByClassName('quiz-content-row')[0]});

                        var imgElement = elemUtils.createElement({type: 'img', parent: attachmentContainer});
                        imgElement.id = 'quiz-img';
                        $(`#${imgElement.id}`).css({'width': '100%'});
                    }
                    attachmentContainer.firstChild.src = Flask.url_for('static', {'filename': `images/quiz/${question.path_to_attachment}`});
                    
                }
                else if(attachmentContainer != null) //delete the image if it is not needed
                    attachmentContainer.parentElement.removeChild(attachmentContainer);
                
                for(let i = 0; i < question.answers.length; i++) {
                    const answer = question.answers[i];

                    var answerContainer = elemUtils.createElement({type: 'div', className: "row quiz-radio-row", parent: answersSection});

                    var answerButton = elemUtils.createElement({type: 'input', className: "quiz-radio-btn", parent: answerContainer});
                    answerButton.type = 'radio';
                    answerButton.id = answer.answer_id;
                    answerButton.name = answer.type;
                    answerButton.value = answer.answer_id;

                    var buttonLabel = elemUtils.createElement({type: 'label', innerHTML: answer.body, parent: answerContainer});
                    buttonLabel.htmlFor = answer.answer_id;

                    /* doesn't work - switch to CSS padding instead
                    var br = document.createElement('br');
                    answerContainer.appendChild(br); */
                }

                elemUtils.checkBackButton();

                const continueContainer = document.getElementsByClassName('quiz-continue-space')[0]
                if(continueContainer.children.length === 0) {
                    var continueButton = elemUtils.createElement({type: 'button', className: "quiz-btn", innerHTML: "Continue", parent: continueContainer});

                    continueButton.addEventListener("click", () => {
                        quiz.navigateToQuestion(++quiz.currentQuestion > quiz.length ? --quiz.currentQuestion : quiz.currentQuestion); //same as the tenerary operator in 'elemUtils.checkBackButton()', but inverse
                    });
                }
                continueContainer.children[0].innerHTML = quiz.currentQuestion === quiz.length ? "Finish" : "Continue";
            }
            else
                throw Error(`There are no answers available for the question with ID ${question.quiz_id}`);
        }
        else 
            throw Error('There was no question specified');
    }
}

elemUtils = {
    createElement: ({type, className=null, innerHTML=null, parent}={}) => { //, attributes = [], eventListener=null
        var element = document.createElement(type);

        if(className != null)
            element.className = className;
        
        if(innerHTML != null)
            element.innerHTML = innerHTML;
        
        /*if(attributes.length > 0)
            attributes.forEach(element.setAttribute);

        if(eventListener != null)
            element.eventListener;*/
        
        parent.appendChild(element);

        return element
    },

    checkBackButton: () => {
        const backContainer = document.getElementsByClassName('quiz-back-space')[0];
        if(quiz.currentQuestion !== 1) {
            if(backContainer.children.length === 0) {
                var backButton = elemUtils.createElement({type: 'button', className: "quiz-btn", innerHTML: "Back", parent: backContainer});

                backButton.addEventListener("click", () => {
                    quiz.navigateToQuestion(--quiz.currentQuestion < 1 ? ++quiz.currentQuestion : quiz.currentQuestion); //this tenerary operator prevents the number from going out of bounds - take away 1 then, if it is lower than the minimum (1), add 1, otherwise use the number with 1 subtracted
                });
            }
        }
        else if(backContainer.children.length > 0)
            backContainer.removeChild(backContainer.children[0]); //there will only ever be 1 child: the button
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