const token = localStorage.getItem("access");

async function loadDoctorProfile() {

    const response = await fetch(
        "http://127.0.0.1:8000/api/doctors/profile/",
        {
            headers:{
                Authorization:"Bearer "+token
            }
        }
    );

    console.log("Status:", response.status);

    const doctor = await response.json();

    console.log("Response:", doctor);

    if(!response.ok){
        alert(JSON.stringify(doctor));
        return;
    }

    document.getElementById("doctor_name").innerText = doctor.doctor_name;
    document.getElementById("email").innerText = doctor.email;
    document.getElementById("specialization").innerText = doctor.specialization;
    document.getElementById("qualification").innerText = doctor.qualification;
    document.getElementById("experience").innerText = doctor.experience;
    document.getElementById("fee").innerText = doctor.consultation_fee;
    document.getElementById("hospital").innerText = doctor.hospital_name;
    document.getElementById("bio").innerText = doctor.bio;
}

loadDoctorProfile();