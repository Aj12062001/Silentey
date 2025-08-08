// moved to static/script.js
document.getElementById('encryptForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const text = document.getElementById('text').value;
    const expiry = document.getElementById('expiry').value;
    const passphrase = document.getElementById('passphrase').value;
    const formData = new FormData();
    formData.append('text', text);
    formData.append('expiry', expiry);
    formData.append('passphrase', passphrase);
    const res = await fetch('/encrypt', {
        method: 'POST',
        body: formData
    });
    if (res.ok) {
        const blob = await res.blob();
        const url = URL.createObjectURL(blob);
        document.getElementById('qrResult').innerHTML = `<img src="${url}" alt="QR Code" />`;
    } else {
        document.getElementById('qrResult').textContent = 'Encryption failed.';
    }
});

document.getElementById('decryptForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const fileInput = document.getElementById('qrfile');
    if (!fileInput.files.length) return;
    const passphrase = document.getElementById('decryptPassphrase').value;
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    formData.append('passphrase', passphrase);
    const res = await fetch('/decrypt', {
        method: 'POST',
        body: formData
    });
    const resultDiv = document.getElementById('decryptedResult');
    if (res.ok) {
        const data = await res.json();
        resultDiv.textContent = 'Decrypted: ' + data.decrypted;
    } else {
        const err = await res.json();
        resultDiv.textContent = 'Error: ' + (err.error || 'Decryption failed.');
    }
});
