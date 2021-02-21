const mainImages = document.getElementsByClassName('main-img');

window.onload = () => {
    stateChecker.shouldHideHeader();
}

window.onscroll = () => {
    stateChecker.shouldHideHeader();
}

stateChecker = {
    shouldHideHeader: () => {
        if(mainImages) { //if there is a dominant image in the page
            for (let i = 0; i < mainImages.length; i++) {
                if (scrollEvents.isOnScreen(mainImages[i])) { //hide the dominant navbar elements if there is a main background image visible
                    $('#logo').css({
                        'opacity': 0
                    });
                    $('#page-header').css({
                        'background-image': 'var(--transparent)'
                    });
                }
                else {
                    $('#logo').css({
                        'opacity': 100
                    });
                    $('#page-header').css({
                        'background-image': 'var(--header-gradient)'
                    });
                }
            }
        }
    }
}

scrollEvents = {
    isOnScreen: (element) => { //used to determine if an HTML element is on screen - https://stackoverflow.com/a/5354536/11136104
		var rect = element.getBoundingClientRect();
		var viewHeight = Math.max(document.documentElement.clientHeight, window.innerHeight);
		return !(rect.bottom < 0 || rect.top - viewHeight >= 0);
	}
}