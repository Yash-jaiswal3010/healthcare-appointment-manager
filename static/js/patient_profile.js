const token = localStorage.getItem("access");

if (!token) {
    window.location.href = "/";
}

async function loadProfile() {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/api/patients/profile/",
            {
                headers: {
                    Authorization: "Bearer " + token
                }
            }
        );

        // No patient profile exists yet
        if (response.status === 404) {
            window.location.href = "/patient/create-profile/";
            return;
        }

        if (!response.ok) {
            throw new Error("Failed to load profile");
        }

        const data = await response.json();

        document.getElementById("name").innerText =
            data.patient_name;

        document.getElementById("email").innerText =
            data.email;

        document.getElementById("dob").innerText =
            data.date_of_birth;

        document.getElementById("gender").innerText =
            data.gender;

        document.getElementById("phone").value =
            data.phone_number || "";

        document.getElementById("address").value =
            data.address || "";

        document.getElementById("emergency_contact").value =
            data.emergency_contact || "";

        document.getElementById("blood_group").value =
            data.blood_group || "";

    }

    catch (error) {

        console.error(error);
        alert("Unable to load profile.");

    }

}

loadProfile();

function enableEdit() {

    document.getElementById("phone").disabled = false;
    document.getElementById("address").disabled = false;
    document.getElementById("emergency_contact").disabled = false;
    document.getElementById("blood_group").disabled = false;

    document.getElementById("saveBtn").style.display = "inline-block";

}

async function saveProfile() {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/api/patients/profile/",
            {
                method: "PATCH",
                headers: {
                    Authorization: "Bearer " + token,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({

                    phone_number:
                        document.getElementById("phone").value,

                    address:
                        document.getElementById("address").value,

                    emergency_contact:
                        document.getElementById("emergency_contact").value,

                    blood_group:
                        document.getElementById("blood_group").value

                })
            }
        );

        if (response.ok) {

            alert("Profile Updated Successfully");
            location.reload();

        } else {

            const error = await response.json();
            alert(JSON.stringify(error));

        }

    }

    catch (error) {

        console.error(error);
        alert("Something went wrong.");

    }

}