const message = document.getElementById("message");
const keyInput = document.getElementById("key");
const result = document.getElementById("result");
const error = document.getElementById("error");

function validateKey() {
  const key = Number(keyInput.value);

  if (!Number.isInteger(key) || key < 1 || key > 25) {
    error.textContent = "Please enter a shift key between 1 and 25.";
    return null;
  }

  error.textContent = "";
  return key;
}

function caesar(text, key, direction) {
  let output = "";

  for (const char of text) {
    if (/[a-zA-Z]/.test(char)) {
      const base = char === char.toUpperCase() ? 65 : 97;
      const index = char.charCodeAt(0) - base;
      const shifted = (index + direction * key + 26) % 26;
      output += String.fromCharCode(base + shifted);
    } else {
      output += char;
    }
  }

  return output;
}

function process(direction) {
  const key = validateKey();
  if (key === null) return;

  result.value = caesar(message.value, key, direction);
}

document.getElementById("encrypt").addEventListener("click", () => process(1));
document.getElementById("decrypt").addEventListener("click", () => process(-1));
