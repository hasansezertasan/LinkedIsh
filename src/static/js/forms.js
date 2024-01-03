function processElement(element) {
    /* Toggle fields with bi-eye-leash */
    document.querySelectorAll(".bi-eye-slash").forEach((element) => {
        element.addEventListener("click", () => {
            const target = document.querySelector(`#${element.dataset.target}`);
            if (target.type === "password") {
                target.type = "text";
                element.classList.replace("bi-eye-slash", "bi-eye");
            } else {
                target.type = "password";
                element.classList.replace("bi-eye", "bi-eye-slash");
            }
        });
    });
}
