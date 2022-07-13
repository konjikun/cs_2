function permutation(n, k) {
    result = 1
    for (; k>0; k--,n--){
    result *= n
    }
    console.log(result)
    }
    
    let p = permutation(10, 3);
    console.log(p)