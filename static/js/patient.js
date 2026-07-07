const API_BASE = "/api";
const token = localStorage.getItem("access");

if (!token) {
    window.location.href = "/";
}

async function loadAppointments() {

    try {

        const response = await fetch(
    `${API_BASE}/appointments/`,
    {
        method: "GET",
        headers: {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json",
        },
    }
);

        if (!response.ok) {
            throw new Error("Failed to fetch appointments");
        }

        const appointments = await response.json();

        console.log(appointments);

        const tbody = document.querySelector("#appointmentTable tbody");
        tbody.innerHTML = "";

        appointments.forEach(appointment => {

            tbody.innerHTML += `
                <tr>
                    <td>${appointment.doctor_name}</td>
                    <td>${appointment.appointment_date}</td>
                    <td>${appointment.appointment_time}</td>
                    <td>${appointment.status}</td>
                    <td>${appointment.symptom_summary || "-"}</td>
                    <td>${appointment.doctor_notes || "-"}</td>
                    <td>${appointment.patient_summary || "-"}</td>
                </tr>
            `;
        });

    } catch (error) {

        console.error(error);
        alert("Unable to load appointments.");

    }
}

loadAppointments();