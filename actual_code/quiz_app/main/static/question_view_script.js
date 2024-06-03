window.onload = () => {
    let callCount = 3000;
    let state = 0;
    
    let id = setInterval(timer, 10);
    const progressBar = document.getElementById('progess-bar');
    const stealDiv = document.getElementById('steal');
    const teams = JSON.parse(sessionStorage.getItem('teams'));
    let stealTeam;

    let currentTeam = sessionStorage.getItem('currentTeam')

    let stealButton;
    for (let i = 0; i < teams.length; i++) {
        if (i != currentTeam){
            stealButton = document.createElement('button')
            stealButton.addEventListener('click', (e) => {
                stopTimer();
                stealTeam = teams.indexOf(e.target.textContent)
            })
            stealButton.textContent = teams[i];
            stealDiv.appendChild(stealButton);
        }
    }

    function updateTeam() {
        currentTeam++;
    
        if (currentTeam > 3) {
            currentTeam = 0;
        }
        sessionStorage.setItem('currentTeam', currentTeam)
    }
    

    
    const completedQuestions = JSON.parse(sessionStorage.getItem('completedQuestions'));
    completedQuestions.push(document.getElementById('question-id-holder').textContent)

    sessionStorage.setItem('completedQuestions', JSON.stringify(completedQuestions))


    function stopTimer() {
        console.log('called')
        clearInterval(id)
        progressBar.style.width = 0;
        document.getElementById('stop-timer').style.display = 'none';
        document.getElementById('check-answer').style.display = 'block';
    }


    document.getElementById('stop-timer').addEventListener('click', stopTimer);


    document.getElementById('check-answer').addEventListener('mouseup', (e) => {
        if (e.button === 0) {
            if (state === 0 ) {
                sessionStorage.setItem(teams[currentTeam], Number(sessionStorage.getItem(teams[currentTeam]) + Number(document.getElementById('question-points-holder').textContent)));
                
            } else {
                sessionStorage.setItem(teams[stealTeam], Number(sessionStorage.getItem(teams[stealTeam]) + Number(document.getElementById('question-points-holder').textContent)));
            }
            showAnswer()
        } else {
            if (state === 0 ) {
                sessionStorage.setItem(teams[currentTeam], Number(sessionStorage.getItem(teams[currentTeam]) - Number(document.getElementById('question-points-holder').textContent)));
                document.getElementById('steal').style.display = 'block';
                document.getElementById('stop-timer').style.display = 'none';
                document.getElementById('check-answer').style.display = 'none';
                state++;
                callCount = 3000;
                id = setInterval(timer, 10)
                
            } else {
                sessionStorage.setItem(teams[stealTeam], Number(sessionStorage.getItem(teams[stealTeam]) - Number(document.getElementById('question-points-holder').textContent)));
                showAnswer()
            }

        }
    })

    
    function timer() {
        if (callCount === 0) {
            state++;
            if (state === 2) {
                clearInterval(id);
                showAnswer()
            } else {
                callCount = 3000;
                sessionStorage.setItem(teams[currentTeam], Number(sessionStorage.getItem(teams[currentTeam]) - Number(document.getElementById('question-points-holder').textContent)));
                document.getElementById('steal').style.display = 'block';
                document.getElementById('stop-timer').style.display = 'none'
            }
            
            
        };
        progressBar.style.width = (callCount/3000 * 100) + '%';
        callCount--;
    };


    function showAnswer() {
        document.getElementById('main').style.display = 'none';
        document.getElementById('answer').style.display = 'block';
        updateTeam();
    }
}


