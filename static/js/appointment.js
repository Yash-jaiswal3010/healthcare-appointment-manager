const API_BASE = "/api";

const token = localStorage.getItem("access");

if (!token) {
    window.location.href = "/";
}

// ----------------------
// Load Doctors
// ----------------------

async function loadDoctors() {

    try {

        const response = await fetch(
            `${API_BASE}/doctors/`,
            {
                headers: {
                    "Authorization": "Bearer " + token,
                },
            }
        );

        if (!response.ok) {
            throw new Error("Failed to fetch doctors");
        }

        const doctors = await response.json();

        console.log(doctors);

        const dropdown = document.getElementById("doctor");

        dropdown.innerHTML =
            '<option value="">Select Doctor</option>';

        doctors.forEach((doctor) => {

            dropdown.innerHTML += `
                <option value="${doctor.id}">
                    ${doctor.doctor_name} (${doctor.specialization})
                </option>
            `;

        });

    }

    catch (error) {

        console.error(error);
        alert("Unable to load doctors.");

    }

}

loadDoctors();


// ----------------------
// Book Appointment
// ----------------------

const form = document.getElementById("appointmentForm");

form.addEventListener("submit", async function (e) {

    e.preventDefault();

    const body = {

        doctor: document.getElementById("doctor").value,

        appointment_date: document.getElementById("appointment_date").value,

        appointment_time: document.getElementById("appointment_time").value,

        symptoms: document.getElementById("symptoms").value,

    };

    try {

        const response = await fetch(
            `${API_BASE}/appointments/`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + token,
                },

                body: JSON.stringify(body),
            }
        );

        const data = await response.json();

        if (response.ok) {

            alert("Appointment booked successfully!");

            window.location.href = "/patient/appointments/";

        } else {

            alert(JSON.stringify(data));

        }

    } catch (error) {

        console.error(error);
        alert("Server Error");

    }

});