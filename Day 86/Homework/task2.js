

let num = window.prompt("enter number")

function numberCheck(num){
    if(num % 2 == 0){
        return true
    }
    else{
        return false
    }
}

console.log(numberCheck(num))