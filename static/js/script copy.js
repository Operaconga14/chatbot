const API_URL = "http://localhost:8000/chat"; // Replace with your FastAPI endpoint

// Toggle theme
function toggleTheme() {
    const body = document.body;
    body.classList.toggle("dark-mode");
    localStorage.setItem("theme", body.classList.contains("dark-mode"));
}

// Initialize theme
window.onload = function () {
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "true") {
        document.body.classList.add("dark-mode");
    }
};

// Create message element
function createMessageElement(text, isOutgoing) {
    const messageDiv = document.createElement("div");
    messageDiv.className = `message ${
        isOutgoing ? "outgoing-message" : "incoming-message"
    }`;
    messageDiv.textContent = text;
    return messageDiv;
}

// Show loading indicator
function showLoading() {
    document.getElementById("loading-indicator").style.display = "flex";
}

// Hide loading indicator
function hideLoading() {
    document.getElementById("loading-indicator").style.display = "none";
}

// Send message to API
async function sendMessage() {
    const userInput = document.getElementById("user-input");
    const message = userInput.value.trim();
    const chatMessages = document.getElementById("chat-messages");

    if (!message) return;

    // Add user message
    chatMessages.appendChild(createMessageElement(message, true));
    userInput.value = "";

    // Show loading indicator
    showLoading();

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                message: message,
                session_id: Date.now().toString(),
            }),
        });

        const data = await response.json();
        hideLoading();

        // Add bot response
        chatMessages.appendChild(createMessageElement(data.response, false));
        chatMessages.scrollTop = chatMessages.scrollHeight;
    } catch (error) {
        hideLoading();
        console.error("Error:", error);
        chatMessages.appendChild(
            createMessageElement(
                "Sorry, there was an error processing your request.",
                false
            )
        );
    }
}

// Handle Enter key
document
    .getElementById("user-input")
    .addEventListener("keypress", function (e) {
        if (e.key === "Enter") {
            sendMessage();
        }
    });
