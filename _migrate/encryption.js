// Helper: Convert string key/iv to Uint8Array
const textEncoder = new TextEncoder();
const textDecoder = new TextDecoder();

// Web Crypto requires importing the raw bytes into a Key object first
async function importKey(key) {
    const keyBytes = textEncoder.encode(key);
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

// --- Test Usage (Must be in an async function) ---
(async () => {
    const KEY_STR = '12345678901234567890123456789012';
    const original = "Hello from Python!";
    
    // // Encrypt
    const encrypted = "hnJlsZZGD9YcyFnLNW4y0Mu2FqzT1nCAXeIoQzjL0jNVaNtoxGi6DNVNH76qp1UO";
    console.log("Encrypted:", encrypted);

    // Decrypt
    const decrypted = await decrypt(KEY_STR, encrypted);
    console.log("Decrypted:", decrypted, decrypted==original);

    const newencrypted = await encrypt(KEY_STR, original);
    console.log("Encrypted again :", newencrypted, newencrypted==encrypted);
})();