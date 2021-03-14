console.log("hellOwO world")

const h2 = document.querySelector("h2")
const currency = h2.textContent.split(" ")[1]
const value = h2.textContent.split(" ")[0]



const symbols = {
EUR: "&euro;",
GBP:"&pound;",
YEN:"&yen;",
CNY:"&yen;"

    }

h2.innerHTML = `${value}${symbols[currency.toUpperCase()] || "$"} `






