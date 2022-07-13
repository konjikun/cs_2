function result(p1, p2) {
    if(p1 > p2){
    console.log('win')}
    else if (p2 > p1){
    console.log('lose')
    }
    else if ( p2 === p1 ) {
    console.log('draw')
    }
    }
    
    console.log(result(1, 10));
    console.log(result(1, 1));
    console.log(result(10, 1));