

let age = window.prompt("შეიყვანეთ თქვენი ასაკი: ")
let gender = window.prompt("შეიყვანეთ თქვენი სქესი: ")
let money = window.prompt("შეიყვანეთ თქვენი ფინანსური მდგომარეობა: ")

if(money > 5000){
    console.log("თქვენი ფინანსური მგომარეობა უზრუნველყოფილია")
}
else if(money < 5000 || money > 3000){
    console.log("ფინანსური პოზიცია სტაბილურია. უკეთესი გეგმაა საჭირო.")
}
else if(money < 3000){
    console.log("გჭირდებათ ფინანსური გეგმის გაუმჯობესება")
}

if(age < 18){
    console.log("ჯერ პატარა ხარ ისწავლე")
}
