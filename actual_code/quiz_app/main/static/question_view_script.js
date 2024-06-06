window.onload = () => {

    // marks the current question as complete
    const completedQuestions = JSON.parse(sessionStorage.getItem('completedQuestions'));
    completedQuestions.push(document.getElementById('question-id-holder').textContent);
    sessionStorage.setItem('completedQuestions', JSON.stringify(completedQuestions));

    const questionsPoints = Number(document.getElementById('question-points-holder').textContent);  // the points of the current question
    
    let id = setInterval(timer, 10);  // interval to create a timer
    const progressBar = document.getElementById('progess-bar');  // the timer element
    let callCount = 3000;  // the number of times the function for the timer is to be called. 3000 * 10 = 30000 ms = 30 s 

    const stealDiv = document.getElementById('steal');  // an initially hidden container to store the teams which can steal the question being answer upon incorrect answer by the current team
    const teams = JSON.parse(sessionStorage.getItem('teams'));  // list of the teams playing the game
    let stealTeam;  // a variable which stores the team which has buzzed to steal

    /* 
    state of 0 corresponds to a state in which the current team answering
    state of 1 corresponds to a state in which the question can be stolen
    state of 2 represents the timer running out in state 1
    */
    let state = 0;

    let currentTeam = sessionStorage.getItem('currentTeam');  // gets the team answering the question

    let stealButton;  // a variable to hold the button elm created for each team which can possibly steal this question
    for (let i = 0; i < teams.length; i++) {
        if (i != currentTeam){  // if the team is not the current team they are legible to steal

            stealButton = document.createElement('button');
            stealButton.addEventListener('click', (e) => {
                stopTimer();
                stealTeam = teams.indexOf(e.target.textContent);
            })

            stealButton.textContent = teams[i];
            stealDiv.appendChild(stealButton);
        }
    }


    // function which is repeatedly called to create the timer
    function timer() {
        if (callCount === 0) {  // timer has run out
            state++;  // moves to the next state if the timer runs out

            if (state === 2) {
                clearInterval(id);  // timer has run out in state 1 so it is to be stopped
                showAnswer();  // no one answered the question in time so the answer is revealed

            } else { 
                callCount = 3000;  // resets the timer for the steal phase
                sessionStorage.setItem(teams[currentTeam], Number(sessionStorage.getItem(teams[currentTeam])) - questionsPoints);  // deducts points from the current team for not answering the question in time
                document.getElementById('steal').style.display = 'block';  // makes the container for the steal buttons visible 
                document.getElementById('stop-timer').style.display = 'none';  // removes the timer stopping button
            }
        }

        progressBar.style.width = (callCount/3000 * 100) + '%';  // updates the width of the bar every call
        callCount--;  // decreases the width with each call to create a bar which shrinks in size
    };


    // function to stop timer when the button is clicked
    function stopTimer() {
        clearInterval(id);
        progressBar.style.width = 0;
        document.getElementById('stop-timer').style.display = 'none';
        document.getElementById('check-answer').style.display = 'block';  // adds a button to check the answer once the timer is stopped
    };

    // adds the above function as an event listener to the button to stop the timer
    document.getElementById('stop-timer').addEventListener('click', stopTimer);


    // adds an event listener to the check answer button to check the answer
    document.getElementById('check-answer').addEventListener('mouseup', (e) => {

        if (e.button === 0) { // a left click means a correct answer from the user
            if (state === 0) {  // checks the state to determine which teams is answering. In this case, the current team is answering
                sessionStorage.setItem(teams[currentTeam], Number(sessionStorage.getItem(teams[currentTeam])) + questionsPoints);  //adds points to the team
                
            } else {  // other team is stealing
                sessionStorage.setItem(teams[stealTeam], Number(sessionStorage.getItem(teams[stealTeam])) + questionsPoints);
            }

            showAnswer();  // in either case the answer is shown since some team got it correct

        } else {  // the question was answered incorrectly
            
            if (state === 0) {
                sessionStorage.setItem(teams[currentTeam], Number(sessionStorage.getItem(teams[currentTeam])) - questionsPoints);  // deducts points
                
                // updates the view
                document.getElementById('steal').style.display = 'block';  // reveals the steal button container
                document.getElementById('stop-timer').style.display = 'none';  // hides the stop timer button
                document.getElementById('check-answer').style.display = 'none';  // hides the answer checking button

                // moves to next state and restarts timer
                state++;
                callCount = 3000;
                id = setInterval(timer, 10);
                
            } else {
                sessionStorage.setItem(teams[stealTeam], Number(Number(sessionStorage.getItem(teams[stealTeam])) - questionsPoints));
                showAnswer();  // everyone answered inccorectly so the answer is revealed
            }

        }
    });

    
    // function to move to the next team
    function updateTeam() {
        currentTeam++;
    
        if (currentTeam > 3) {
            currentTeam = 0;
        }
        sessionStorage.setItem('currentTeam', currentTeam);
    };


    // function to reveal the answer
    function showAnswer() {
        document.getElementById('main').style.display = 'none';
        document.getElementById('answer').style.display = 'block';
        updateTeam();
    };
};


// an event listner to prevent the context menu from being opened upon a right click
window.addEventListener('contextmenu', (e) => {
    e.preventDefault();
});

