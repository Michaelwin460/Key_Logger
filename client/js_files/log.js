
const params = new URLSearchParams(window.location.search);
const computerName = params.get('name');
const log = params.get('logFile');

document.getElementById('logName').innerText = log || "Unknown log file";

document.addEventListener("DOMContentLoaded", function () {
    const logContent = document.getElementById("logContent");

    fetch(`http://localhost:5000/computers/${encodeURIComponent(computerName)}/logs/${encodeURIComponent(log)}`)
    .then(response => {
        if (!response.ok) throw new Error("Failed to fetch log content");
        return response.text();
    })
    .then(content => {
        logContent.innerText = content;
    })
    .catch(error => {
        console.error("Error fetching log content:", error.message);
        logContent.innerText = "Error loading log file.";
    });

});
