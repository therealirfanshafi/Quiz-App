window.onload = () => {

    const teams = JSON.parse(sessionStorage.getItem('teams')); // gets the teams
    const scores = [];
    for (team of teams) { 
        scores.push({name: team, score: sessionStorage.getItem(team)});  // creates an array of objects with the team name and score
    }

    scores.sort((a, b) => a.score - b.score);  // sorts it according to the score

    for (let i = 0; i < scores.length; i ++) {
        document.getElementById(`${4 - i}-place`).textContent = `Postion ${4-i}: \n ${scores[i].name} \n with ${scores[i].score} points`;  // populates the empty paragraph elements with appropriate messages
    }

    sessionStorage.clear();  // since the game is over the stored data is no longer required

};