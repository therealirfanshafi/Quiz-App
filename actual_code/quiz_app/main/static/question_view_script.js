window.onload = () => {
    let callCount = 3000;
    let state = 0;
    
    const id = setInterval(a, 10);
    const progressBar = document.getElementById('progess-bar');
    const stealDiv = document.getElementById('steal');
    const teams = JSON.parse(sessionStorage.getItem('teams'));

    let currentTeam = sessionStorage.getItem('currentTeam')

    let qButton;
    for (let i = 0; i < teams.length; i++) {
        console.log(i)
        console.log(currentTeam)
        console.log(i != currentTeam)
        if (i != currentTeam){
            qButton = document.createElement('button')
            qButton.setAttribute('onlclick', `selectTeam(${teams[i]})`)
            qButton.textContent = teams[i];
            stealDiv.appendChild(qButton);
        }
    }

    currentTeam++;
    
    if (currentTeam > 3) {
        currentTeam = 0;
    }

    sessionStorage.setItem('currentTeam', currentTeam)
    
    const completedQuestions = JSON.parse(sessionStorage.getItem('completedQuestions'));
    completedQuestions.push(document.getElementById('question-id-holder').textContent)

    sessionStorage.setItem('completedQuestions', JSON.stringify(completedQuestions))
    
    function a() {
        if (callCount === 0) {
            state++;
            if (state === 2) {
                clearInterval(id);
                document.getElementById('main').style.display = 'none';
                document.getElementById('answer').style.display = 'block';
            } else {
                callCount = 3000;
                document.getElementById('steal').style.display = 'block';
            }
            
            
        };
        progressBar.style.width = (callCount/3000 * 100) + '%';
        callCount--;
    };

    let stealTeam = null;
    function selectTeam(team) {
        document.getElementById('steal').style.display = 'none';
        stealTeam = team;
    };
}


