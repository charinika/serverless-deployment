
// API Gateway endpoint
const API_URL = "https://x2a8qxtbl7.execute-api.ap-south-1.amazonaws.com/greet";

const form = document.querySelector("form");
const greeting = document.querySelector("#greeting");
const counter = document.querySelector(".counter-number");

// Handle form submission
form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const name = document.querySelector("#name").value.trim();

    if (!name) {
        greeting.textContent = "Please enter your name.";
        return;
    }

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: name
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Request failed");
        }

        greeting.textContent = data.message;
        counter.textContent = "Views: " + data.count;

    } catch (error) {
        console.error("Error:", error);
        greeting.textContent = "Unable to connect to server.";
    }
});
