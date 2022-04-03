function max(numbers) {
    let max_number = numbers[0];
    for(let i=1; i<numbers.length; i++){
        if (numbers[i] > max_number) {
            max_number = numbers[i];
        }
    }
    return max_number;
}

function findPosition(numbers, target) {
    let position = -1;
    for (i=0; i<numbers.length; i++){
        if (numbers[i] === target){
            position = i;
            break;
        }
    }
    return position;
}
console.log( max([1, 2, 4, 5]) );
console.log( max([5, 2, 7, 1, 6]) ); 

console.log( findPosition([5, 2, 7, 1, 6], 5) ); 
console.log( findPosition([5, 2, 7, 1, 6], 7) );
console.log( findPosition([5, 2, 7, 7, 7, 1, 6], 7) ); 
console.log( findPosition([5, 2, 7, 1, 6], 8) );