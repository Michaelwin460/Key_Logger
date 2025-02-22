


document.addEventListener("DOMContentLoaded", function () {
    const dataList = document.getElementById("data-list");

    fetch("http://localhost:5000/computers")
        .then(response => response.json())
        .then(data => {

            console.log("Received data:", data['computers']); 

            if (!Array.isArray(data['computers'])) {
                throw new Error("Data is not an array");            }


            dataList.innerHTML = "";
            data['computers'].forEach(item => {
                const li = document.createElement("li");
                li.textContent = item;
                dataList.appendChild(li);
            });
        })
        .catch(error => console.error("Error fetching data:", error));
});
