const navMenu = document.querySelector('.nav-menu')
const hamburger = document.querySelector('.hamburger')

hamburger.addEventListener("click", () => {
    hamburger.classList.toggle('active')
    navMenu.classList.toggle('active')
})