if(!localStorage.getItem){
    localStorage.setItem('counter',0);
}
let counter = localStorage.getItem('counter');
function count(){
    counter++;
    document.querySelector('h1').innerHTML = counter;
    if(counter % 10 === 0){
        alert(`Counter is ${counter}`);
    }
    localStorage.setItem('counter', counter);
}
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = count;
})
