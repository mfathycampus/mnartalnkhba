// 🔥 تفعيل الأنيميشن عند التمرير
document.addEventListener("DOMContentLoaded", () => {
  const elements = document.querySelectorAll(".fade-in-up, .fade-in-right, .fade-in-left");
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.visibility = "visible";
        entry.target.classList.add("animate");
      }
    });
  }, { threshold: 0.2 });

  elements.forEach(el => {
    el.style.visibility = "hidden";
    observer.observe(el);
  });
});
