// Problem
function calcTax() {
  let priceBox = document.getElementById('price-without-tax')
  let taxBox = document.getElementById('tax-rate')
  let price = priceBox.value  
  let tax = taxBox.value
  console.log(price)
  console.log(tax)
  samPrice = Number(price) + Number((price*(tax*0.01)))
  samtax = Number(samPrice) - Number(price)
  let pricedis = document.getElementById('price')
  let taxdis = document.getElementById('tax')
  pricedis.textContent = samPrice
  taxdis.textContent = samtax
}
