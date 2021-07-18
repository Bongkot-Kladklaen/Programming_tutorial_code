const btn = document.querySelector('#request');
const bio = document.querySelector('#bio');

const request = new XMLHttpRequest();

request.onreadystatechange = function(){
    if (request.readyState === 4) {
        bio.getElementsByClassName.border = '1px solid #e8e8e8';

        if (request.status === 200) {
            bio.innerHTML = request.responseText;
        }else{
            bio.innerHTML = 'Error' + request.status + " " + request.statusText;
        }
    }
}

request.open('get','https://baconipsum.com/api/?type=meat-and-filler');

btn.addEventListener('click',function () {
    this.style.display = "none";

    request.send();
});
