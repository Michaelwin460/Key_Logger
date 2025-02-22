const computers = ["PC-101", "Server-202", "Laptop-303"];
const list = document.getElementById('computerList');
computers.forEach(computer => {
    const li = document.createElement('li');
    li.innerHTML = `<a href="../html_files/comp_details.html?name=${computer}">${computer}</a>`;
    list.appendChild(li);
});