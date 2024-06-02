window.onload = () => {
    const teams = JSON.parse(sessionStorage.getItem('teams'));
    const teamElm = document.createElement('h1');
    teamElm.textContent = `${teams[sessionStorage.getItem('currentTeam')]}'s turn now`;
    document.querySelector('.board').appendChild(teamElm);

    const completedQuestions = JSON.parse(sessionStorage.getItem('completedQuestions'))
    console.log(completedQuestions)

    for (question of completedQuestions) {
        const qButton = document.getElementById(question);
        qButton.removeAttribute('onclick');
        qButton.style.backgroundColor = 'transparent';
    }
}