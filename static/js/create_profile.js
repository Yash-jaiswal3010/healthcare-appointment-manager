const token = localStorage.getItem("access");

document
.getElementById("profileForm")
.addEventListener("submit", async function(e){

e.preventDefault();

const API_BASE = "/api";


const response = await fetch(
    `${API_BASE}/patients/`,
    {
        method: "POST",
        headers: {
            Authorization: "Bearer " + token,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            date_of_birth: document.getElementById("dob").value,
            gender: document.getElementById("gender").value,
            blood_group: document.getElementById("blood_group").value,
            phone_number: document.getElementById("phone").value,
            address: document.getElementById("address").value,
            emergency_contact: document.getElementById("emergency").value
        })
    }
);

if(response.ok){

alert("Profile Created Successfully");

window.location.href="/patient/profile/";

}

else{

const error=await response.json();

alert(JSON.stringify(error));

}

});