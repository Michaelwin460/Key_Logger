function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    if (username && password) {
        localStorage.setItem('user', username);
        window.location.href = 'computers_list.html';
    } else {
        alert('Enter credentials!');
    }
}