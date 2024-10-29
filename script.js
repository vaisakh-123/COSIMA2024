// Wait for DOM content to load before attaching event listener
document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('loginForm');
    const errorMessage = document.getElementById('error-message');

    // Attach submit event listener to the form
    loginForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission behavior

        const username = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        // Validate credentials (you can customize this part)
        if (username === 'admin' && password === 'password123') {
            window.location.href = 'details.html'; // Redirect to the details page on successful login
        } else {
            errorMessage.textContent = 'Invalid username or password. Please try again.';
        }
    });
});
