// Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyBb2Sh1wHOncZMaczp0pN55fmEYSS5paik",
    authDomain: "cosima2024-caa23.firebaseapp.com",
    projectId: "cosima2024-caa23",
    storageBucket: "cosima2024-caa23.appspot.com",
    messagingSenderId: "1089668841435",
    appId: "1:1089668841435:web:f26e890c6e3f16a10031fe",
    measurementId: "G-F846GN1JLC"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();

// Email/Password Login
function loginWithEmailPassword(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    auth.signInWithEmailAndPassword(email, password)
        .then(userCredential => {
            console.log('Login successful:', userCredential.user);
            window.location.href = 'dashboard.html';  // Redirect to dashboard
        })
        .catch(error => {
            console.error('Error during login:', error);
            alert(error.message);
        });
}

// Google Sign-In
function loginWithGoogle() {
    const provider = new firebase.auth.GoogleAuthProvider();
    
    auth.signInWithPopup(provider)
        .then(result => {
            console.log('Google login successful:', result.user);
            window.location.href = 'dashboard.html';  // Redirect to dashboard
        })
        .catch(error => {
            console.error('Error during Google login:', error);
            alert(error.message);
        });
}

// Email/Password Sign-up
function signUpWithEmailPassword(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    auth.createUserWithEmailAndPassword(email, password)
        .then(userCredential => {
            console.log('User signed up:', userCredential.user);
            window.location.href = 'dashboard.html';  // Redirect to dashboard
        })
        .catch(error => {
            console.error('Error during sign-up:', error);
            alert(error.message);
        });
}

// Google Sign-Up
function signUpWithGoogle() {
    const provider = new firebase.auth.GoogleAuthProvider();
    
    auth.signInWithPopup(provider)
        .then(result => {
            console.log('Google sign-up successful:', result.user);
            window.location.href = 'dashboard.html';  // Redirect to dashboard
        })
        .catch(error => {
            console.error('Error during Google sign-up:', error);
            alert(error.message);
        });
}

// Password Reset
function resetPassword(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;

    auth.sendPasswordResetEmail(email)
        .then(() => {
            document.getElementById('dialogBox').style.display = 'flex';
        })
        .catch(error => {
            console.error('Error sending password reset email:', error);
            alert(error.message);
        });
}
