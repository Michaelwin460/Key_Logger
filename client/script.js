

document.addEventListener("DOMContentLoaded", function () {
    const dataList = document.getElementById("data-list");

    fetch("http://localhost:5000/computers")
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("Received data:", data);

            if (!data || !Array.isArray(data.computers)) {
                throw new Error("Invalid data format: 'computers' must be an array.");
            }

            dataList.innerHTML = "";

            data.computers.forEach(item => {
                const li = document.createElement("li");
                li.textContent = item;
                dataList.appendChild(li);
            });
        })
        .catch(error => {
            console.error("Error fetching data:", error.message);
            dataList.innerHTML = `<li style="color: red;">Failed to load data. Please try again later.</li>`;
        });
});
