// Wait for DOM content to load before attaching event listener
document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('loginForm');
    const errorMessage = document.getElementById('error-message');

    // Attach submit event listener to the form
    loginForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission behavior

        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        // Validate credentials (you can customize this part)
        if (email === 'admin@gmail.com' && password === '609911') {
            window.location.href = '../Doctor Details/doctor_details.html'; // Redirect to the details page on successful login
        } else {
            errorMessage.textContent = 'Invalid email or password. Please try again.';
        }
    });
});