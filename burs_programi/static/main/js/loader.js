document.addEventListener("DOMContentLoaded", function () {
  const loader = document.getElementById("loader-wrapper");

  const minDisplayTime = 1000; // Minimum 1.5 saniye görünsün
  const start = Date.now();

  window.addEventListener("load", function () {
    const elapsed = Date.now() - start;
    const remaining = minDisplayTime - elapsed;

    setTimeout(() => {
      loader.style.opacity = "0";
      setTimeout(() => {
        loader.style.display = "none";
      }, 300); // fade-out süresi
    }, remaining > 0 ? remaining : 0);
  });
});
