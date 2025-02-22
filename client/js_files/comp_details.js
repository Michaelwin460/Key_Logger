const params = new URLSearchParams(window.location.search);
const computerName = params.get('name');
document.getElementById('computerName').innerText = computerName || "Unknown Computer";
