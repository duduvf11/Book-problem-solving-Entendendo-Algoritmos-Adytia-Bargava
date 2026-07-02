// Binary Search formula == log2(n) === number of steps

function binarySearchStepsCounter(listSize){
    listSize = Number(listSize)
    if(isNaN(listSize)){
        return 'Isso não é um número.'
    }

    return Math.ceil(Math.log2(listSize))
}

console.log(binarySearchStepsCounter(128))
console.log(binarySearchStepsCounter(256))