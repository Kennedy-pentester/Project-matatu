function bookMatatu(number) {
    let matatuDivs = document.querySelectorAll(".matatu");
    let selectedMatatu = matatuDivs[number - 1];
    let seatsElement = selectedMatatu.querySelector(".seats");
    let availableSeats = parseInt(seatsElement.innerText);

    if (availableSeats > 0) {
        seatsElement.innerText = availableSeats - 1;

        let confirmationList = document.getElementById("confirmation-list");
        let listItem = document.createElement("li");
        listItem.innerHTML = `Matatu ${number} - <strong>Seat booked</strong>`;
        confirmationList.appendChild(listItem);
    } else {
        alert("Sorry, this matatu is full!");
    }
}

function addMatatu() {
    let container = document.querySelector(".matatu-container");
    let newMatatu = document.createElement("div");
    newMatatu.classList.add("matatu");
    let matatuCount = document.querySelectorAll(".matatu").length + 1;

    newMatatu.innerHTML = `
        <h2><i class="fas fa-bus"></i> Matatu ${matatuCount}</h2>
        <p>Capacity: <span class="capacity">14</span> passengers</p>
        <p>Seats available: <span class="seats">14</span></p>
        <button onclick="bookMatatu(${matatuCount})">Book Now</button>
    `;

    container.appendChild(newMatatu);
}

document.addEventListener("DOMContentLoaded", function() {
    let loginForm = document.getElementById("loginForm");
    
    if (loginForm) {
        loginForm.addEventListener("submit", function(event) {
            event.preventDefault();

            let username = document.getElementById("username").value;
            let password = document.getElementById("password").value;
            let errorMessage = document.getElementById("errorMessage");

            if (username === "admin" && password === "password123") {
                window.location.href = "dashboard.html"; // Redirect to the dashboard
            } else {
                errorMessage.textContent = "Invalid username or password. Try again.";
            }
        });
    }
});

function viewMatatuDetails(matatuId) {
    alert("Viewing details for Matatu " + matatuId);
}

function addNewMatatu() {
    alert("Feature to add a new Matatu coming soon!");
}

function goBack() {
    window.location.href = "dashboard.html";
}

// Simulated Booking Data
const bookings = [
    { matatu: "Wote Express", passenger: "Alice Kikosi", seats: 2, date: "2025-03-06" },
    { matatu: "Kinatwa sacco", passenger: "Brian Kiamba", seats: 1, date: "2025-03-06" },
    { matatu: "Kililimbi sacco", passenger: "Catherine Mutua", seats: 3, date: "2025-03-06" }
];

// Display Bookings in Table
async function displayBookings() {
    const bookingList = document.getElementById("booking-list");
    bookingList.innerHTML = "";

    const response = await fetch('http://127.0.0.1:8000/api/bookings/');
    const bookings = await response.json();

    bookings.forEach(booking => {
        const row = `<tr>
            <td>${booking.matatu}</td>
            <td>${booking.passenger}</td>
            <td>${booking.seats}</td>
            <td>${booking.date}</td>
        </tr>`;
        bookingList.innerHTML += row;
    });
}


async function displayMatatus() {
    const matatuList = document.getElementById("matatu-list");
    matatuList.innerHTML = ""; 

    try {
        const response = await fetch('http://127.0.0.1:8000/api/matatus/');
        if (!response.ok) {
            throw new Error("Failed to fetch matatus.");
        }

        const matatus = await response.json();
        matatus.forEach(matatu => {
            const matatuDiv = document.createElement("div");
            matatuDiv.classList.add("matatu-card");
            matatuDiv.innerHTML = `
                <h3>${matatu.name}</h3>
                <p><strong>Driver:</strong> ${matatu.driver}</p>
                <p><strong>Conductor:</strong> ${matatu.conductor}</p>
                <p><strong>Seats Available:</strong> ${matatu.available_seats}</p>
            `;
            matatuList.appendChild(matatuDiv);
        });

    } catch (error) {
        console.error("Error fetching matatus:", error);
        matatuList.innerHTML = "<p>Failed to load matatus.</p>";
    }
}
// Handle New Booking Form Submission
document.addEventListener("DOMContentLoaded", function () {
    const bookingForm = document.getElementById("booking-form");

    if (bookingForm) {
        bookingForm.addEventListener("submit", function (event) {
            event.preventDefault();

            // Get form values
            const matatu = document.getElementById("matatu").value;
            const passenger = document.getElementById("passenger").value;
            const seats = document.getElementById("seats").value;
            const date = document.getElementById("date").value;

            // Validate input
            if (!matatu || !passenger || !seats || !date) {
                alert("Please fill all fields.");
                return;
            }

            // Add to table
            const bookingList = document.getElementById("booking-list");
            const newRow = `<tr>
                <td>${matatu}</td>
                <td>${passenger}</td>
                <td>${seats}</td>
                <td>${date}</td>
            </tr>`;
            bookingList.innerHTML += newRow;

            // Clear form fields
            bookingForm.reset();
        });
    }
});

document.getElementById('login-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const response = await fetch('http://127.0.0.1:8000/api/login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });

    const data = await response.json();
    if (response.ok) {
        localStorage.setItem("loggedIn", "true");
        window.location.href = "dashboard.html";
    } else {
        document.getElementById('login-error').textContent = data.error;
    }
});


// Check if logged in before accessing dashboard
if (window.location.pathname.includes("dashboard.html") && localStorage.getItem("loggedIn") !== "true") {
    window.location.href = "index.html"; // Redirect to login if not logged in
}


