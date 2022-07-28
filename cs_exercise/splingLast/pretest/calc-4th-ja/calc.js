
function C_to_F(c) {
    return 9 * c / 5 +32;
}

function disp_fahren() {
    let celcius = parseFloat(document.getElementById('cel-temp').value);
    let fahrenheit = C_to_F(celcius);

    document.getElementById('fahren').textContent = fahrenheit;
}
