const mainImages = document.getElementsByClassName('main-img');

window.onload = () => {
    stateHandler.shouldHideHeader();
    
    if (mainImages != null && mainImages.length > 0) { //if there is a dominant image in the page, add the 'window.onscroll()' event listener
        window.onscroll = () => {
            stateHandler.shouldHideHeader();
        }
    }
}

stateHandler = {
    shouldHideHeader: () => {
        if(mainImages != null && mainImages.length > 0) { //we need to check this here also as 'window.onload()' will run this method separately
            for (let i = 0; i < mainImages.length; i++) {
                if (events.isOnScreen(mainImages[i])) //hide the dominant navbar elements if there is a main background image visible
                    stateHandler.modifyHeader(0, 'var(--transparent)');
                else
                    stateHandler.modifyHeader(100, 'var(--header-gradient)');
            }
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
    },
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
                    topicItemLevel.setAttribute('test', topic.tests[j].test_id);
                    topicItemLevel.addEventListener("click", () => { window.location.href = Flask.url_for('quiz_page')});
                    topicItemLevels.appendChild(topicItemLevel);
                }

                document.getElementById('topics-menu').appendChild(topicItem);
            }
        }
    }
}