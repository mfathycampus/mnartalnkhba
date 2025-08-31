const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");
const closeBtn = document.querySelector(".close-btn");
const sections = document.querySelectorAll("section");

// فتح القائمة عند الضغط على أيقونة الهامبرغر
hamburger.addEventListener("click", () => {
    navLinks.classList.add("active");
});

// إغلاق القائمة عند الضغط على زر الإغلاق
closeBtn.addEventListener("click", () => {
    navLinks.classList.remove("active");
});

// إغلاق القائمة عند الضغط على أي رابط
navLinks.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", () => {
        navLinks.classList.remove("active");
    });
});

// Intersection Observer for animations
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        } else {
            entry.target.classList.remove('visible');
        }
    });
}, {
    threshold: 0.2
});

document.querySelectorAll('.fade-in-up, .fade-in-right, .fade-in-left').forEach(element => {
    observer.observe(element);
});
