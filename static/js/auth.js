const API_BASE = "/api";

const loginForm = document.getElementById("loginForm");

if (loginForm) {

    loginForm.addEventListener("submit", async function (e) {

        e.preventDefault();

        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        try {

            const response = await fetch(`${API_BASE}/auth/login/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    email,
                    password
                })
            });

            const data = await response.json();

            if (!response.ok) {
                alert(data.detail || data.non_field_errors || "Login Failed");
                return;
            }

            localStorage.setItem("access", data.access);
            localStorage.setItem("refresh", data.refresh);

            localStorage.setItem("role", data.user.role);
            localStorage.setItem("name", data.user.full_name);
            localStorage.setItem("email", data.user.email);

            if (data.user.role === "PATIENT") {
                window.location.href = "/patient/dashboard/";
            }
            else if (data.user.role === "DOCTOR") {
                window.location.href = "/doctor/dashboard/";
            }
            else if (data.user.role === "ADMIN") {
                alert("Admin Dashboard Coming Soon");
            }

        }

        catch (error) {

            console.log(error);
            alert("Server Error");

        }

    });

}

async function logout() {

    const refresh = localStorage.getItem("refresh");
    const access = localStorage.getItem("access");

    try {

            await fetch(
    `       ${API_BASE}/auth/logout/`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + access,
                },
                body: JSON.stringify({
                    refresh: refresh
                }),
            }
        );

    } catch (e) {
        console.log(e);
    }

    localStorage.clear();
    window.location.href = "/";
}