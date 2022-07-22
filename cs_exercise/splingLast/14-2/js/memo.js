function count() {
    let inputX = document.getElementById('input-x');
    let x = inputX.value;
    let inputC = document.getElementById('input-c');
    let c = inputC.value;
    
    let num = 0;
    for (let i of x){
        if (i === c){
            num++
        }
    }
  
    let outputX = document.getElementById('output-x');
    outputX.textContent = x;
    let outputC = document.getElementById('output-c');
    outputC.textContent = c;
    let outputNum = document.getElementById('output-num');
    outputNum.textContent = String(num);
  }