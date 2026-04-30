
const getarray = (arr)=>{
    return arr.filter(num => num%2===0)
}
arr=[10,3,567,3,5,235,566,4,23,346,9]
console.log(getarray(arr));