// let a = "Hello World";
// const b = 2
// b += 1

// console.log(a);
// console.log(b);
    // console.log(`Кнопка нажата ${a}`)}
// const on_btn_click = () => {console.log(`Кнопка нажата ${a}`)}
// let btn = document.querySelector(".button_map");

let btn_feedback = document.getElementById("feedback_btn");
let modal_feedback = document.getElementById("feedback_modal")
let modal_feedback_close = document.getElementById("feedback_modal_close")

let btn_search = document.getElementById("btn_search")
let modal_search = document.getElementById("modal_search")

let btn_enter = document.getElementById("btn_enter")
let modal_enter = document.getElementById("modal_enter")

let btn_cart = document.getElementById("btn_cart")
let modal_cart = document.getElementById("modal_cart")

let switchers = document.querySelectorAll(".switcher")
let slides = document.querySelectorAll(".special_offer")
let body = document.querySelector("body")

let on_btn_switcher_click = function(index){
    let colors = ["#849D8F", "#8996A6", "#9D8B84"]
    switchers.forEach((switcher)=>{switcher.classList.remove("offer_button_active")})
    switchers[index].classList.add("offer_button_active")
    slides.forEach((slide)=>{slide.classList.remove("special_offer_active")})
    slides[index].classList.add("special_offer_active")
    body.style.backgroundColor = colors[index]
}

let on_btn_feedback_click = function(){
    modal_feedback.classList.add("modal_show");
}

let on_modal_feedback_close = function(){
    modal_feedback.classList.remove("modal_show");
}

let on_btn_search_click = function(){
    modal_search.classList.toggle("modal_show");
    modal_enter.classList.remove("modal_show");
    modal_cart.classList.remove("modal_show");
}

let on_btn_enter_click = function(){
    modal_enter.classList.toggle("modal_show");
    modal_search.classList.remove("modal_show");
    modal_cart.classList.remove("modal_show");
}

let on_btn_cart_click = function(){
    modal_cart.classList.toggle("modal_show");
    modal_search.classList.remove("modal_show");
    modal_enter.classList.remove("modal_show");
}

if (btn_feedback) {
    btn_feedback.addEventListener("click", on_btn_feedback_click);
    btn_feedback.addEventListener("click", on_btn_feedback_click);
    modal_feedback_close.addEventListener("click", on_modal_feedback_close);
    switchers.forEach((switcher, index)=>{
    switcher.addEventListener("click", ()=>{on_btn_switcher_click(index)})
})
}

btn_search.addEventListener("click", on_btn_search_click)
if (btn_enter) {
btn_enter.addEventListener("click", on_btn_enter_click)
}
btn_cart.addEventListener("click", on_btn_cart_click)

// switchers.addEventListener("click", ()=>{on_btn_switcher_click(switchers)})
