// erases any existing stored data 
window.onload = () => {
    sessionStorage.clear();
};


document.getElementById('team-selector').addEventListener('submit', (e) => {
    e.preventDefault();  // prevents the page from refreshing when the form is submitted 

    /*
    session storage is used because the game data should be erased when the browser window is closed
    browser storage is used because it would be tedious to store such small temporary data while the game is running in the actual database
    it would make it very difficult to store retrieve, store and update data efficiently without writing any APIS which would add a lot of complexity
    although the browser storage can be easily modified, this is unimportant as this site will only be able to be used by admins who will not modify such data; i.e. the players of this game will only be able to view the site on a screen, so they dont have access to any data
    for a similar reason, a lot of information is stored in hidden HTML elements such that it can be easily accessed by client side static javascript without the need for APIS
    */

    // a loop to get each team's name 
    teams = [];
    for (let i = 0; i<=3; i ++) {
        teams[i] = document.getElementById(`team-${i+1}`).value;
        sessionStorage.setItem(teams[i], 0);  // initialises a score counted for each team
    }

    sessionStorage.setItem('teams', JSON.stringify(teams));  // stores the list of teams as a JSON string
    sessionStorage.setItem('currentTeam', 0);  // stores an indication to the team whos turn it currently is to answer
    sessionStorage.setItem('completedQuestions', JSON.stringify([]));  // tracks the number of completed questions 

    window.location = document.getElementById('url-holder').textContent;  // moves to the game board using the URL stored in the hidden paragraph element
    return false;
});