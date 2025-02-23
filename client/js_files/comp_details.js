const params = new URLSearchParams(window.location.search);
const computerName = params.get('name');
document.getElementById('computerName').innerText = computerName || "Unknown Computer";

document.addEventListener("DOMContentLoaded", function () {
    const logsList = document.getElementById("logsList");

    fetch(`http://localhost:5000/computers/${encodeURIComponent(computerName)}/logs`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("Received data:", data);

            if (!data || !Array.isArray(data.logs)) {
                throw new Error("Invalid data format: 'logs' must be an array.");
            }

            logsList.innerHTML = "";

            data.logs.forEach(log => {
                const li = document.createElement('li');
                li.innerHTML = `<a href="../html_files/log.html?name=${encodeURIComponent(computerName)}&logFile=${encodeURIComponent(log)}">${log}</a>`;
                logsList.appendChild(li);
            });
        })
        .catch(error => {
            console.error("Error fetching data:", error.message);
            logsList.innerHTML = `<li style="color: red;">Failed to load data. Please try again later.</li>`;
        });
});

