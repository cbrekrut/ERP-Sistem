document.addEventListener("DOMContentLoaded", function() {
    var text = document.querySelector(".text");
    window.addEventListener("scroll", function() {
        var scroll = window.scrollY;

        if (scroll >= 100) {
            text.classList.remove("hidden");
        } else {
            text.classList.add("hidden");
        }
    });
});
