function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    let chatBox = document.getElementById("chat-box");

    if (userInput.trim() === "") return;

    // Display user message
    let userMessage = document.createElement("div");
    userMessage.textContent = "You: " + userInput;
    chatBox.appendChild(userMessage);

    // Send request to Flask server
    fetch("/chat", {
        method: "POST",
        body: JSON.stringify({ message: userInput }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        // Display bot response
        let botMessage = document.createElement("div");
        botMessage.textContent = "Bot: " + data.response;
        chatBox.appendChild(botMessage);
    });

    // Clear input
    document.getElementById("user-input").value = "";
}