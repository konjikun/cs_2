// Problem
let x = 0


function startNoodle() {
    timebox = document.getElementById('time')
    n =timebox.value
    allen = setInterval(count,1000)
    shintani = setTimeout(timeup,n*1000*60)
}

function stopNoodle() {
    clearInterval(allen)
}

function count() {
    x++;
    displayBox = document.getElementById('message')
    displayBox.textContent = 'あと' + String((n*60)-x) + '秒'

}
function timeup(){
    alert (String(n) + '分経ちました')
}