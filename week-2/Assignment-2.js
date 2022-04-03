const goodtime = document.getElementsByClassName('h1')[0];
const btnShow = document.getElementById('square');
const hidden = document.getElementById('hidden-box');
hidden.style.display = 'none';

goodtime.addEventListener("click", ()=>{
    goodtime.innerHTML = "Have a Good Time!";
});

btnShow.addEventListener("click", ()=> {
    hidden.style.display = '';
});
console.log(btnShow);