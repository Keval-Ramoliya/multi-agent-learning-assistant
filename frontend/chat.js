let sessionId = localStorage.getItem("session_id");
let currentAgentMode = "auto";
let lastBotReply = "";

const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");




sendBtn.addEventListener("click", sendMessage);



// Set agent mode
function setAgentMode(mode) {
    currentAgentMode = mode;
    const header = document.getElementById("header-title");

   if (mode === "auto") header.innerText = "Auto Mode (Router decides)";
    else if (mode === "coding") header.innerText = "Coding Agent";
    else if (mode === "learning") header.innerText = "Learning Agent";
    else if (mode === "project") header.innerText = "Project Builder";
    else if (mode === "code_review") header.innerText = "Code Review Agent";
    else if (mode === "research") header.innerText = "Research Agent";
    else if (mode === "document_reader") header.innerText = "Document Reader Agent";

    // Toggle PDF upload UI
    if (mode === "document_reader") {
        document.getElementById("pdf-upload-area").style.display = "block";
    } else {
        document.getElementById("pdf-upload-area").style.display = "none";
    }
}

// Ensure session exists
async function ensureSession() {
    if (!sessionId) {
        const res = await fetch("http://127.0.0.1:5000/api/session");
        const data = await res.json();
        sessionId = data.session_id;
        localStorage.setItem("session_id", sessionId);
    }
}
ensureSession();

function addMessage(text, sender="bot") {
    const msg = document.createElement("div");
    msg.classList.add("message", sender === "user" ? "user-msg" : "bot-msg");
//    msg.innerText = text;
    msg.innerHTML = marked.parse(text);
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function showLoader() {
    addMessage("Thinking...", "bot");
}



async function sendMessage() {
    const text = userInput.value.trim();
    if (!text) return;

    addMessage(text, "user");
    userInput.value = "";

    addMessage("Thinking...", "bot");

    const res = await fetch("http://127.0.0.1:5000/api/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            message: text,
            session_id: localStorage.getItem("session_id"),
            agent: currentAgentMode
        })
    });

    const data = await res.json();
    lastBotReply = data.reply;

    // Remove old loader
    document.querySelectorAll(".bot-msg").forEach(el => {
        if (el.innerText === "Thinking...") el.remove();
    });

    addMessage(data.reply, "bot");
}

sendBtn.onclick = sendMessage;

userInput.addEventListener("keypress", e => {
    if (e.key === "Enter") sendMessage();
});

// Download last bot reply as TXT
function downloadLastReply(type) {
    if (!lastBotReply) return alert("No reply to download!");

    if (type === "txt") {
        const blob = new Blob([lastBotReply], { type: "text/plain" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "assistant_output.txt";
        a.click();
    }

    if (type === "pdf") {
        const blob = new Blob([lastBotReply], { type: "application/pdf" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "assistant_output.pdf";
        a.click();
    }
}
//
//async function uploadPDF() {
//    const fileInput = document.getElementById("pdf-file");
//    const file = fileInput.files[0];
//
//    if (!file) {
//        alert("Please select a PDF file first.");
//        return;
//    }
//
//    let formData = new FormData();
//    formData.append("file", file);  // MUST MATCH BACKEND KEY
//
//    console.log("Selected file:", file);
//    console.log("FormData:", formData.get("file"));
//
//    try {
//        const res = await fetch("http://127.0.0.1:5000/api/upload-pdf", {
//            method: "POST",
//            body: formData,
//        });
//
//        const data = await res.json();
////        addMessage(data.reply || "PDF processed", "bot");
//
//        addMessage("📄 PDF uploaded successfully. Processing text…", "bot");
//
//    } catch (err) {
//        console.error("Upload error:", err);
//        addMessage("❌ Upload error (network)", "bot");
//    }
//}

async function uploadPDF() {
    const fileInput = document.getElementById("pdf-file");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a PDF file first.");
        return;
    }

    let formData = new FormData();
    formData.append("file", file);

    try {
        // STEP 1 — Upload PDF & Extract Text
        const res = await fetch("http://127.0.0.1:5000/api/upload-pdf", {
            method: "POST",
            body: formData
        });

        const uploaded = await res.json();

        if (!uploaded.text) {
            addMessage("❌ Failed to extract text from PDF.", "bot");
            return;
        }

        addMessage("📄 PDF uploaded. Extracting text...", "bot");

        // STEP 2 — Send extracted text to the Document Agent
        const res2 = await fetch("http://127.0.0.1:5000/api/document-text", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                text: uploaded.text,
                session_id: localStorage.getItem("session_id")
            })
        });

        const finalData = await res2.json();

        addMessage(finalData.reply, "bot");

    } catch (err) {
        console.error("Error uploading PDF:", err);
        addMessage("❌ Network or server error.", "bot");
    }
}
//
//// Apply saved theme
//if (localStorage.getItem("theme") === "dark") {
//    document.body.classList.add("dark-theme");
//    document.getElementById("theme-toggle").innerText = "☀️ Light Mode";
//}
//
//
//
//function toggleTheme() {
//    const body = document.body;
//    const button = document.getElementById("theme-toggle");
//
//    if (body.classList.contains("dark-theme")) {
//        body.classList.remove("dark-theme");
//        button.innerText = "🌙 Dark Mode";
//        localStorage.setItem("theme", "light");
//    } else {
//        body.classList.add("dark-theme");
//        button.innerText = "☀️ Light Mode";
//        localStorage.setItem("theme", "dark");
//    }
//}
