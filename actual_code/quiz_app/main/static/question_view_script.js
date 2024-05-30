window.onload = () => {
    let callCount = 3000;
    let state = 0;
    
    const id = setInterval(a, 10);
    const progressBar = document.getElementById('progess-bar');

    
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
}


function selectTeam() {
    document.getElementById('steal').style.display = 'none';
};