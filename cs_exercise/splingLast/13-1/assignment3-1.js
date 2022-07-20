function abbrev (text) {
    result = ''
    for (let x of text){
        if(x!='a' && x!='i' && x!='u' && x !='e' && x != 'o'){
           result += x
        }
        
    }return result
}