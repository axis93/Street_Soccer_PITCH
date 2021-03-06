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
        //console.log(element, endpoint, extension, data, handler);

        $.ajax({
            url: extension === null ? `${endpoint}` : `${endpoint}/${extension}`,
            method: "GET",
            data: data,
            success: (data) => {
                if(handler != null && data != null) //if we got data from the backend and we have something to do with it
                    handler(data); //handler is the method (based on the parameter) that used the data from this request
            }
        });

        /*$.get(`/${endpoint}/${extension}`, (data) => {
            handler(data); //'handler' is the JavaScript function that will handle the data returned from the backend
        });*/
    },
}

requestHandlers = {
    /*handleWhenReady: (element, handler, data) => {
        jQuery(document).ready(checkContainer);

        function checkContainer() {
            if(events.isOnScreen(element)){ //if the container is visible on the page
                handler(data); //Adds a grid to the html
                console.log('got here');
            }
            else {
                setTimeout(checkContainer, 50); //wait 50 ms, then try again
            }
        }
    },*/

    listTopics: (data) => {
        //console.log(data);
        if(data != null) { //
            for(let i = 0; i < data.topics.length; i++) {
                //console.log(data.topics[i]);
                const topic = data.topics[i];

                var topicItem = document.createElement('div');
                topicItem.className = "topic-item";

                var topicItemName = document.createElement('b');
                topicItemName.className = "topic-name";
                topicItemName.innerHTML = topic.name;
                topicItem.appendChild(topicItemName);

                var topicItemLine = document.createElement('div');
                topicItemLine.className = "topics-line";
                topicItem.appendChild(topicItemLine);

                var topicItemLevels = document.createElement('div');
                topicItemLevels.className = "topic-levels";
                topicItem.appendChild(topicItemLevels);

                for(let j = 0; j < topic.tests.length; j++) {
                    var topicItemLevel = document.createElement('button');
                    topicItemLevel.innerHTML = j + 1;
                    topicItemLevel.className = "level-button";
                    topicItemLevel.addEventListener("click", () => { window.location.href = Flask.url_for('quiz_page')});
                    topicItemLevel.setAttribute('test', topic.tests[j].test_id);
                    topicItemLevels.appendChild(topicItemLevel);
                    //console.log(topicItemLevel);
                }

                document.getElementById('topics-menu').appendChild(topicItem);
            }
        }
    }
}