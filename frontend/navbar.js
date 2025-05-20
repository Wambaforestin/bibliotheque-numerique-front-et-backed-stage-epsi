// navbar.js
document.addEventListener("DOMContentLoaded", () => {
  const navbarContainer = document.getElementById("navbar");
  if (!navbarContainer) return;

  const role = localStorage.getItem("role");
  const token = localStorage.getItem("token");

  let html = `
    <nav class="bg-white p-4 shadow flex justify-between items-center mb-4">
      <h1 class="text-xl font-bold text-blue-800">Bibliothèque</h1>
      <div id="menu" class="space-x-4">
  `;

  if (!token) {
    html += `<a href="login.html" class="text-blue-600">Connexion</a>`;
  } else {
    html += `<a href="index.html" class="text-gray-700">Accueil</a>`;
    html += `<a href="explore.html" class="text-gray-700">Explorer</a>`;

    if (role === "admin" || role === "enseignant") {
      html += `<a href="upload.html" class="text-gray-700">Uploader</a>`;
      html += `<a href="dashboard.html" class="text-gray-700">Dashboard</a>`;
    }

    html += `<button onclick="logout()" class="text-red-500">Déconnexion</button>`;
  }

  html += `</div></nav>`;
  navbarContainer.innerHTML = html;
});

function logout() {
  localStorage.removeItem("token");
  localStorage.removeItem("role");
  window.location.href = "login.html";
}
