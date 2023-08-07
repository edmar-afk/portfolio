// Your JavaScript code
// Replace the fixedExchangeRate with the current exchange rate between PHP and USD
const fixedExchangeRate = 0.019; // 1 PHP = 0.019 USD (example rate)

// Function to convert PHP to USD
function convertToUSD(pesoAmount) {
  return pesoAmount * fixedExchangeRate;
}

// Get the Peso value from the HTML p tag
const pesoValueElement = document.getElementById('pesoValue');
const pesoAmount = parseFloat(pesoValueElement.textContent);

// Convert Peso to USD
const usdAmount = convertToUSD(pesoAmount);

// Display the converted value in another p tag
const usdValueElement = document.getElementById('usdValue');
usdValueElement.textContent = `${usdAmount.toFixed(2)} USD`;