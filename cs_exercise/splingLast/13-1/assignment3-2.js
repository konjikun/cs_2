function max_len(xs) {
    result =''
    for (let x of xs){
    if (result.length < x.length){
    result = x
    }
    }
    console.log(result)
    }
    
    