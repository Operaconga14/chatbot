console.log("I am loaded");

API_URL = "http://localhost:8000/chat";

const sendBtn = document.getElementById("send-button");
const chatMessages = document.getElementById("chat-messages");
const userInput = document.getElementById("user-input");

sendBtn.addEventListener("click", sendMessage);

async function sendMessage() {
    try {
        const response = await fetch(API_URL, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        });

        const data = await response.json();
        const message = userInput.value.trim();

        if (!message) return;

        chatMessages.appendChild(createMessageElement(message, true));

        console.log("Response", data.chat_id);
        console.log("User Input", message);

        clearInputField();
    } catch (error) {
        console.log("error", error);
    }
}

function clearInputField() {
    userInput.value = "";
}

function createMessageElement(text, isOutgoing) {
    const messageDiv = document.createElement("div");
    messageDiv.className = `message ${
        isOutgoing ? "outgoing-message" : "incoming-message"
    }`;
    messageDiv.textContent = text;
    return messageDiv;
}
