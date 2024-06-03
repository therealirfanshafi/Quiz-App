window.onload = () => {
    sessionStorage.clear()
}


document.getElementById('team-selector').addEventListener('submit', (e) => {
    e.preventDefault();

    
    teams = []
    for (let i = 0; i<=3; i ++) {
        teams[i] = document.getElementById(`team-${i+1}`).value;
        sessionStorage.setItem(teams[i], 0);
    }

    sessionStorage.setItem('teams', JSON.stringify(teams));
    sessionStorage.setItem('currentTeam', 0);
    sessionStorage.setItem('completedQuestions', JSON.stringify([]))

    window.location = document.getElementById('url-holder').textContent;
    return false;
})