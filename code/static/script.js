document.getElementById('encryptForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const text = document.getElementById('text').value;
    const expiry = document.getElementById('expiry').value;
    const passphrase = document.getElementById('passphrase').value;
    const formData = new FormData();
    formData.append('text', text);
    formData.append('expiry', expiry);
    formData.append('passphrase', passphrase);

    try {
        const res = await fetch('/encrypt', {
            method: 'POST',
            body: formData
        });

        if (res.ok) {
            // Expecting image
            const blob = await res.blob();
            if (blob.type === "application/json") {
                const err = await res.json();
                document.getElementById('qrResult').textContent = 'Error: ' + err.error;
            } else {
                const url = URL.createObjectURL(blob);
                document.getElementById('qrResult').innerHTML = `<img src="${url}" alt="QR Code" />`;
            }
        } else {
            const err = await res.json();
            document.getElementById('qrResult').textContent = 'Error: ' + (err.error || 'Encryption failed.');
        }
    } catch (err) {
        document.getElementById('qrResult').textContent = 'Exception: ' + err.message;
    }
});


document.getElementById('decryptForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const file = document.getElementById('qrfile').files[0];
    const passphrase = document.getElementById('decryptPassphrase').value;
    const formData = new FormData();
    formData.append('qrfile', file);
    formData.append('passphrase', passphrase);

    const res = await fetch('/decrypt', {
        method: 'POST',
        body: formData
    });

    if (res.ok) {
        const data = await res.json();
        document.getElementById('decryptedResult').textContent = data.message;
        startExpiryTimer(parseInt(data.expiry, 10)); // use original duration from server
    } else {
        const err = await res.json();
        document.getElementById('decryptedResult').textContent = 'Error: ' + (err.error || 'Decryption failed.');
        document.getElementById('timer').textContent = "";
    }
});

// Timer function
function startExpiryTimer(seconds) {
    let remaining = seconds;
    document.getElementById('timer').textContent = `Message will disappear in ${remaining} seconds.`;
    const interval = setInterval(() => {
        remaining--;
        if (remaining > 0) {
            document.getElementById('timer').textContent = `Message will disappear in ${remaining} seconds.`;
        } else {
            clearInterval(interval);
            document.getElementById('decryptedResult').textContent = "";
            document.getElementById('timer').textContent = "Message expired.";
        }
    }, 1000);
}
