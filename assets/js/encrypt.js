// Helper: Convert string key/iv to Uint8Array
const textEncoder = new TextEncoder();
const textDecoder = new TextDecoder();

// Web Crypto requires importing the raw bytes into a Key object first
async function importKey(key) {
    const keyBytes = await window.crypto.subtle.digest(
        "SHA-256", 
        textEncoder.encode(key)
    );

    return await window.crypto.subtle.importKey(
        "raw", 
        keyBytes, 
        { name: "AES-CBC" }, 
        false, 
        ["encrypt", "decrypt"]
    );
}

async function encrypt(secret, text) {
    const key = await importKey(secret);
    const iv = window.crypto.getRandomValues(new Uint8Array(16));
    const data = textEncoder.encode(text);

    const encryptedBuffer = await window.crypto.subtle.encrypt(
        { name: "AES-CBC", iv: iv },
        key,
        data
    );

    const encryptedBytes = new Uint8Array(encryptedBuffer);
    const combined = new Uint8Array(iv.length + encryptedBytes.length);
    combined.set(iv);
    combined.set(encryptedBytes, iv.length);

    return arrayBufferToBase64(combined.buffer);
}

async function decrypt(secret, base64Text) {
    const key = await importKey(secret);

    const combinedBuffer = base64ToArrayBuffer(base64Text);
    const combinedBytes = new Uint8Array(combinedBuffer);

    const iv = combinedBytes.slice(0, 16);
    const encryptedData = combinedBytes.slice(16);
    
    const decryptedBuffer = await window.crypto.subtle.decrypt(
        { name: "AES-CBC", iv: iv },
        key,
        encryptedData
    );

    return textDecoder.decode(decryptedBuffer);
}

// --- Helpers for Base64 Conversion ---
function arrayBufferToBase64(buffer) {
    let binary = '';
    const bytes = new Uint8Array(buffer);
    const len = bytes.byteLength;
    for (let i = 0; i < len; i++) {
        binary += String.fromCharCode(bytes[i]);
    }
    return window.btoa(binary);
}

function base64ToArrayBuffer(base64) {
    const binary_string = window.atob(base64);
    const len = binary_string.length;
    const bytes = new Uint8Array(len);
    for (let i = 0; i < len; i++) {
        bytes[i] = binary_string.charCodeAt(i);
    }
    return bytes.buffer;
}

// (async () => {
//     const KEY_STR = '';
//     const original = "Hello from Python!";
    
//     // // Encrypt
//     const encrypted = "sUzxXEHdV9qi2/tci45LWdGdLoBS1o9TgyhR/vDF1sxdx+cdsFcA1XxRRQAXLRfA3pP46TjuLMDqVNf++Hx7zQ==";
//     console.log("Encrypted:", encrypted);

//     // Decrypt
//     const decrypted = await decrypt(KEY_STR, encrypted);
//     console.log("Decrypted:", decrypted, decrypted==original);

//     const newencrypted = await encrypt(KEY_STR, original);
//     console.log("Encrypted again :", newencrypted, newencrypted==encrypted);
// })();

async function triggerDecryptFunction() {
    const key = prompt("Please enter the secret key:");
    if (!key) return;

    const encryptedElements = document.querySelectorAll('.secret.encrypted-secret');
    encryptedElements.forEach(async element => {
        const cipherText = element.innerText;
        
        // This is where your actual decryption math/library would go.
        // For now, I'm just mocking it to show it worked.
        let decryptedText = "Wrong secret key!!";
        try {
            decryptedText = await decrypt(key, cipherText)    
        } catch (error) {}

        // We look at the immediate next sibling element
        let outputBox = element.nextElementSibling;

        // Verify that the neighbor is actually one of our 'revealed' boxes
        if (outputBox && outputBox.classList.contains('decrypted-secret')) {
            // CASE 1: It already exists, just update the text
            outputBox.innerHTML = decryptedText;
            
            // Optional: Visual cue that it updated
            outputBox.style.backgroundColor = "#e8f5e9"; 
            setTimeout(() => outputBox.style.backgroundColor = "transparent", 300);
            
        } else {
            // CASE 2: It does not exist, create it
            outputBox = document.createElement('div');
            outputBox.classList.add('secret');
            outputBox.classList.add('decrypted-secret');
            outputBox.innerHTML = decryptedText;
            
            // // Add some basic styling so it stands out
            // outputBox.style.color = "green";
            // outputBox.style.fontWeight = "bold";
            // outputBox.style.marginTop = "5px";

            // Insert the new box right after the encrypted element
            element.after(outputBox);
        }
    });

}


const secretCode = 'secret';
let pressedKeys = '';

// Listen for keydown events on the whole page
document.addEventListener('keydown', (event) => {
    
    // Normalize the key to lowercase so 'Shift' or CapsLock doesn't break it
    const key = event.key.toLowerCase();

    // Add the new key to our buffer
    pressedKeys += key;

    // Keep the buffer the same length as the secret code
    // If the buffer gets too long, remove the first character (rolling window)
    if (pressedKeys.length > secretCode.length) {
        pressedKeys = pressedKeys.slice(-secretCode.length);
    }

    // Check if the buffer matches the secret
    if (pressedKeys === secretCode) {
        triggerDecryptFunction()
        pressedKeys = ''; 
    }
});