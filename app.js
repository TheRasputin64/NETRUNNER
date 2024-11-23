// ═══════════════════════════════════════════════════════════════════════════════════════════════════
// ████████╗██╗  ██╗███████╗    ███╗   ██╗███████╗████████╗██████╗ ██╗   ██╗███╗   ██╗███╗   ██╗███████╗██████╗ 
// ╚══██╔══╝██║  ██║██╔════╝    ████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║   ██║████╗  ██║████╗  ██║██╔════╝██╔══██╗
//    ██║   ███████║█████╗      ██╔██╗ ██║█████╗     ██║   ██████╔╝██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
//    ██║   ██╔══██║██╔══╝      ██║╚██╗██║██╔══╝     ██║   ██╔══██╗██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
//    ██║   ██║  ██║███████╗    ██║ ╚████║███████╗   ██║   ██║  ██║╚██████╔╝██║ ╚████║██║ ╚████║███████╗██║  ██║
//    ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
// ═══════════════════════════════════════════════════════════════════════════════════════════════════
// CORE ENCRYPTION/DECRYPTION ENGINE
// ═══════════════════════════════════════════════════════════════════════════════════════════════════

class NetrunnerCipher {
    constructor() {
        this.CYBER_MASK = 0xF0;  // Binary: 11110000
    }

    // Layer 1: ICE_BREAKER encryption
    layer1Encrypt(text) {
        let shift = text.length % 26;  // Dynamic shift based on text length
        let encrypted = [];
        for (let i = 0; i < text.length; i++) {
            let shifted = (text.charCodeAt(i) + shift) % 256;  // Shifted ASCII (wraps at 256)
            let scrambled = (shifted + (i * shift)) % 256;  // Position-based scramble (wraps at 256)
            encrypted.push(scrambled);
        }
        return encrypted;
    }

    // Layer 2: GHOST_RUNNER encryption
    layer2Encrypt(values) {
        let encrypted = [];
        for (let i = 0; i < values.length; i++) {
            let reversedBits = parseInt(values[i].toString(2).padStart(8, '0').split('').reverse().join(''), 2);
            let shifted = (reversedBits + i) % 256;
            encrypted.push(shifted);
        }
        return encrypted;
    }

    // Layer 3: MATRIX_DIVE encryption
    layer3Encrypt(values) {
        let final = [];
        for (let i = 0; i < values.length; i++) {
            let dynamicMask = (this.CYBER_MASK + i) % 256;
            let xored = values[i] ^ dynamicMask;
            let substituted = (xored + i) % 256;
            final.push(substituted);
        }
        return final;
    }

    encrypt(text) {
        let asciiValues = [...text].map(c => c.charCodeAt(0));
        let iceBreaker = this.layer1Encrypt(text);
        let ghostRunner = this.layer2Encrypt(iceBreaker);
        let matrixDive = this.layer3Encrypt(ghostRunner);
        
        return {
            input: text,
            ascii: asciiValues,
            ice_breaker: iceBreaker,
            ghost_runner: ghostRunner,
            matrix_dive: matrixDive.map(n => n.toString(16).padStart(2, '0')).join(''),
        };
    }

    decrypt(hexData) {
        let data = [];
        for (let i = 0; i < hexData.length; i += 2) {
            data.push(parseInt(hexData.substring(i, i + 2), 16));
        }

        // Reverse Layer 3: MATRIX_DIVE decryption
        let ghostExit = this.layer3Decrypt(data);

        // Reverse Layer 2: GHOST_RUNNER decryption
        let iceExit = this.layer2Decrypt(ghostExit);

        // Reverse Layer 1: ICE_BREAKER decryption
        return this.layer1Decrypt(iceExit);
    }

    // Decryption layers (reverse of encryption)
    layer3Decrypt(values) {
        let decrypted = [];
        for (let i = 0; i < values.length; i++) {
            let unsubstituted = (values[i] - i + 256) % 256; // Ensure no negative values
            let dynamicMask = (this.CYBER_MASK + i) % 256;
            let unxored = unsubstituted ^ dynamicMask;
            decrypted.push(unxored);
        }
        return decrypted;
    }

    layer2Decrypt(values) {
        let decrypted = [];
        for (let i = 0; i < values.length; i++) {
            let unshifted = (values[i] - i + 256) % 256; // Ensure no negative values
            let unreversed = parseInt(unshifted.toString(2).padStart(8, '0').split('').reverse().join(''), 2);
            decrypted.push(unreversed);
        }
        return decrypted;
    }

    layer1Decrypt(values) {
        let shift = values.length % 26;
        let decrypted = [];
        for (let i = 0; i < values.length; i++) {
            let unscrambled = (values[i] - (i * shift) + 256) % 256; // Ensure no negative values
            let unshifted = (unscrambled - shift + 256) % 256; // Ensure no negative values
            decrypted.push(unshifted);
        }

        // Convert to string, ensuring no negative or out-of-range values
        return decrypted.map(val => String.fromCharCode(val)).join('');
    }
}

// ═══════════════════════════════════════════════════════════════════════════════════════════════════
// ██╗   ██╗██╗███████╗██╗   ██╗ █████╗ ██╗         ██╗███╗   ██╗████████╗███████╗██████╗ ███████╗ █████╗  ██████╗███████╗
// ██║   ██║██║██╔════╝██║   ██║██╔══██╗██║         ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝
// ██║   ██║██║███████╗██║   ██║███████║██║         ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝█████╗  ███████║██║     █████╗  
// ╚██╗ ██╔╝██║╚════██║██║   ██║██╔══██║██║         ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗██╔══╝  ██╔══██║██║     ██╔══╝  
//  ╚████╔╝ ██║███████║╚██████╔╝██║  ██║███████╗    ██║██║ ╚████║   ██║   ███████╗██║  ██║██║     ██║  ██║╚██████╗███████╗
//   ╚═══╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝
// ═══════════════════════════════════════════════════════════════════════════════════════════════════

// Event listener for encryption and decryption
document.getElementById('sendBtn').addEventListener('click', function() {
    const message = document.getElementById('messageInput').value;
    if (message === '') return alert('Please enter a message.');
    
    const cipher = new NetrunnerCipher();
    const encrypted = cipher.encrypt(message);
    const decrypted = cipher.decrypt(encrypted.matrix_dive);

    // Output results
    document.getElementById('encryptedOutput').innerText = encrypted.matrix_dive;
    document.getElementById('decryptedOutput').innerText = decrypted;
});

//╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣                     ╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╠╩╦╔═╗║╝╚╬╣╠╩╦╔═╗║╝╣╠╩╦╔═╗║╝╚╬╣╠╩╦╔═╗║═╗                ╔═╗║╝╚╬╣╠╩╦╔═╗║═╗
//╣╠╩╦╔═╗║╝╚╬╣╠╩╦╔═╗║╝ by mostafa mohamed  ╣╠╩╦╔═╗║╝╚╬╣╠╩╦╔═╗║╝╣╠╩╦╔═╗║╝╚╬╣╠╩╦╔═╗║╝╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╗ The_Rasputin64 ╔═╗║╝╚╬╣╠╩╦╔═╗║═╗
//╣╩╔╗╝╬╠╦═║╚╣╩╔╗╝╬╠╦═                     ╣╩╔╗╝╬╠╦═║╚╣╩╔╗╝╬╠╦═╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╣╩╔╗╝╬╠╦═║╚╣╩╔╗╝╬╠╦═╣                ╔═╗║╝╚╬╣╠╩╦╔═╗║═╗
