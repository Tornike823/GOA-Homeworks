let a = window.prompt("Enter num1: ")
let b = window.prompt("Enter num2: ")
let c = window.prompt("Enter num3: ")



if(a + b > c){
    console.log(true)
}
else if(b + c > a){
    console.log(true)
}
else if(a + c > b){
    console.log(true)
}
else{
    console.log(false)
}

