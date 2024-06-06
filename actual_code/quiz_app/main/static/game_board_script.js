window.onload = () => {

    const teams = JSON.parse(sessionStorage.getItem('teams'));  // gets the list of teams who are playing the game 
    const teamElm = document.createElement('h1');  // creates an h1 tag to display the name of the team whose turn in currently is 
    teamElm.textContent = `${teams[sessionStorage.getItem('currentTeam')]}'s turn now`;  // sets the text conent using the currentTeam key in the browser storage
    document.querySelector('.board').appendChild(teamElm);  // appends the element to the correct position

    const completedQuestions = JSON.parse(sessionStorage.getItem('completedQuestions'));  // gets the list of completed questions

    
    if (completedQuestions.length == document.getElementById('num-qs-holder').textContent) {  // checks if all the questions have been answerd and if so, it moves to the results view
        window.location = document.getElementById('results-url-holder').textContent;
    }

    // mechanism to prevent the same question from being answered twice
    for (question of completedQuestions) {
        const qButton = document.getElementById(question);
        qButton.removeAttribute('onclick');
        qButton.style.backgroundColor = 'transparent';
    }
};

