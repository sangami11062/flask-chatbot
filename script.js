document.getElementById("sendBtn").addEventListener("click", function () {
    let userMessage = document.getElementById("userInput").value;

    fetch("https://your-app-name.onrender.com/chat", {  // Replace with your actual URL
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: userMessage }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("chatbox").innerHTML += `<p><b>Bot:</b> ${data.response}</p>`;
    })
    .catch(error => console.error("Error:", error));
});
