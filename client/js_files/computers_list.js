// const computers = ["PC-101", "Server-202", "Laptop-303"];
// const list = document.getElementById('computerList');
// computers.forEach(computer => {
//     const li = document.createElement('li');
//     li.innerHTML = `<a href="../html_files/comp_details.html?name=${computer}">${computer}</a>`;
//     list.appendChild(li);
// });


document.addEventListener("DOMContentLoaded", function () {
    const computersList = document.getElementById("computerList");

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

            computersList.innerHTML = "";

            data.computers.forEach(computer => {
                const li = document.createElement('li');
                li.innerHTML = `<a href="../html_files/comp_details.html?name=${computer}">${computer}</a>`;
                computersList.appendChild(li);
            });
        })
        .catch(error => {
            console.error("Error fetching data:", error.message);
            computersList.innerHTML = `<li style="color: red;">Failed to load data. Please try again later.</li>`;
        });
});


// function login() {
//     const username = document.getElementById('username').value;
//     const password = document.getElementById('password').value;

//     const data = {
//         username: username,
//         password: password
//     };

//     fetch('http://localhost:5000/login', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(data)
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.success) {
//             window.location.href = 'computers_list.html';
//         } else {
//             alert('Invalid username or password');
//         }
//     })
//     .catch(error => {
//         console.error('Error:', error);
//         alert('An error occurred');
//     });
// }