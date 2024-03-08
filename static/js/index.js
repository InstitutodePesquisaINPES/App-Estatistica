function setupLogin() {
    const userBox = document.getElementById('userBox');
    const closeBox = document.getElementById('closeBox');

    if (userBox && closeBox) {
        userBox.style.display = 'block';
        console.log("Ativado ");

        closeBox.addEventListener('click', function() {
            userBox.style.display = 'none';
            console.log("Fechado");
        });
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const userIcon = document.getElementById('userIcon');

    if (userIcon) {
        userIcon.addEventListener('click', setupLogin);
    }
});