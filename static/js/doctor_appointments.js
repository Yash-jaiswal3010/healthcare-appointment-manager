const token = localStorage.getItem("access");

async function loadAppointments() {

    const response = await fetch(
        "http://127.0.0.1:8000/api/appointments/doctor/",
        {
            headers: {
                Authorization: "Bearer " + token
            }
        }
    );

    const appointments = await response.json();

    const tbody = document.querySelector("#doctorTable tbody");

    tbody.innerHTML = "";

    appointments.forEach(app => {

        tbody.innerHTML += `
        <tr>

            <td>${app.patient_name}</td>

            <td>${app.appointment_date}</td>

            <td>${app.appointment_time}</td>

            <td>

                <select id="status-${app.id}">

                    <option value="PENDING" ${app.status==="PENDING"?"selected":""}>Pending</option>

                    <option value="CONFIRMED" ${app.status==="CONFIRMED"?"selected":""}>Confirmed</option>

                    <option value="COMPLETED" ${app.status==="COMPLETED"?"selected":""}>Completed</option>

                    <option value="CANCELLED" ${app.status==="CANCELLED"?"selected":""}>Cancelled</option>

                </select>

            </td>

            <td>${app.symptoms}</td>

            <td>

                <textarea id="notes-${app.id}" rows="4">${app.doctor_notes || ""}</textarea>

            </td>

            <td>

                <button onclick="updateAppointment(${app.id})">
                    Update
                </button>

            </td>

        </tr>
        `;

    });

}

async function updateAppointment(id){

    const status =
        document.getElementById(`status-${id}`).value;

    const doctor_notes =
        document.getElementById(`notes-${id}`).value;

    const response = await fetch(

        `http://127.0.0.1:8000/api/appointments/doctor/${id}/`,

        {

            method:"PATCH",

            headers:{

                Authorization:"Bearer "+token,

                "Content-Type":"application/json"

            },

            body:JSON.stringify({

                status,
                doctor_notes

            })

        }

    );

    const data = await response.json();

    if(response.ok){

        alert("Appointment Updated Successfully.");

        loadAppointments();

    }

    else{

        alert(JSON.stringify(data));

    }

}

loadAppointments();