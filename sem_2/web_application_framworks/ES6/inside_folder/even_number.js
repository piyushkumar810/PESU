function printEvenNumber(arr){
    for(let i=0;i<arr.length;i++){
        if(arr[i]%2===0){
            console.log(arr[i]);
        }
    }
}


export{printEvenNumber}