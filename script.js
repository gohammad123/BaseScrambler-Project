document.addEventListener("DOMContentLoaded", function() {
    const correctPassword = "sigma";  // Set your correct password here

    function verifyPassword() {
        const inputPassword = document.getElementById("password").value;
        console.log("Password entered:", inputPassword);  // For debugging

        if (inputPassword === correctPassword) {
            console.log("Password correct. Adding animation...");
            document.getElementById("login-container").classList.add("pulse");
            setTimeout(function() {
                document.getElementById("login-container").classList.remove("pulse");
                document.getElementById("login-container").style.display = "none";
                document.getElementById("main-container").classList.remove("hidden");
                document.getElementById("main").style.display = "block";
                document.getElementById("body").classList.add("wave");
                console.log("Password verified successfully. Transition completed.");  // For debugging
            }, 1000); // Wait for the pulse animation to complete
        } else {
            document.getElementById("password-message").textContent = "Incorrect password. Try again.";
            console.log("Password verification failed.");  // For debugging
        }
    }

    function encodeText() {
        const text = document.getElementById("encode-text").value;
        const encodedText = btoa(text);  // Base64 encoding for simplicity
        document.getElementById("encoded-result").textContent = `Encoded: ${encodedText}`;
        console.log("Encoded text:", encodedText);  // For debugging
    }

    function decodeText() {
        const text = document.getElementById("decode-text").value;
        try {
            const decodedText = atob(text);  // Base64 decoding for simplicity
            document.getElementById("decoded-result").textContent = `Decoded: ${decodedText}`;
            console.log("Decoded text:", decodedText);  // For debugging
        } catch (e) {
            document.getElementById("decoded-result").textContent = "Invalid input for decoding.";
            console.log("Decoding failed with error:", e);  // For debugging
        }
    }

    function showEncode() {
        document.getElementById("encode").style.display = "block";
        document.getElementById("decode").style.display = "none";
        console.log("Showing encode section.");  // For debugging
    }

    function showDecode() {
        document.getElementById("encode").style.display = "none";
        document.getElementById("decode").style.display = "block";
        console.log("Showing decode section.");  // For debugging
    }

    function exitApp() {
        alert("Exiting the application. Goodbye!");
        console.log("Exiting application.");  // For debugging
        window.close();
    }

    document.getElementById("password").addEventListener("keyup", function(event) {
        if (event.key === "Enter") {
            verifyPassword();
        }
    });

    document.getElementById("encode-text").addEventListener("keyup", function(event) {
        if (event.key === "Enter") {
            encodeText();
        }
    });

    document.getElementById("decode-text").addEventListener("keyup", function(event) {
        if (event.key === "Enter") {
            decodeText();
        }
    });

    document.getElementById("submit").addEventListener("click", function() {
        console.log("Submit button clicked.");  // For debugging
        verifyPassword();
    });
    document.getElementById("encode-button").addEventListener("click", encodeText);
    document.getElementById("decode-button").addEventListener("click", decodeText);
    document.getElementById("encode-button").addEventListener("click", showEncode);
    document.getElementById("decode-button").addEventListener("click", showDecode);
    document.getElementById("exit-button").addEventListener("click", exitApp);
});
