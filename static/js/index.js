// API URL
API_URL = "http://localhost:8000";

// Div element Initialization
const sendBtn = document.getElementById("send-button");
const chatMessages = document.getElementById("chat-messages");
const userInput = document.getElementById("user-input");

// Button Function
sendBtn.addEventListener("click", sendMessage);

// Other Functions
window.onload = function () {
    generateChatId();
};

function loadChatIds() {
    return JSON.parse(localStorage.getItem("chat_ids")) || [];
}

function clearInputField() {
    userInput.value = "";
}

async function generateChatId() {
    try {
        const response = await fetch(`${API_URL}/generate`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        });

        const data = await response.json();
        // console.log("Response", data.chat_id);
        const chatId = data.chat_id;

        saveChatId(chatId);

        const chat_ids = loadChatIds();

        if (!chat_ids.includes(chatId)) {
            saveChatId(chat_ids);
        }

        // console.log("ChatIds", chat_ids);

        return chatId;
    } catch (error) {
        console.error(error);
    }
}

function saveChatId(chatId) {
    localStorage.setItem("chat_id", JSON.stringify(chatId));
}

function createMessageElement(text, isOutgoing) {
    const messageDiv = document.createElement("div");
    messageDiv.className = `message ${
        isOutgoing ? "outgoing-message" : "incoming-message"
    }`;
    messageDiv.textContent = text;
    return messageDiv;
}

async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    chatMessages.appendChild(createMessageElement(message, true));

    try {
        console.log("Sending request to:", `${API_URL}/chat`);
        const response = await fetch(`${API_URL}/chat`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ message: message }),
        });

        const data = await response.json();
        console.log("Data:", data);

        clearInputField();
    } catch (error) {
        console.log("error", error);
    }
}
