window.onload = () => {
    const teams = JSON.parse(sessionStorage.getItem('teams'));
    const scores = []
    for (team of teams) { 
        scores.push({name: team, score: sessionStorage.getItem(team)})
    }

    scores.sort((a, b) => a.score - b.score);

    for (let i = 0; i < scores.length; i ++) {
        document.getElementById(`${4 - i}-place`).textContent = `Postion ${4-i}: \n ${scores[i].name} \n with ${scores[i].score} points`
    }

    sessionStorage.clear();


}