(function () {
  var STORAGE_KEY = "tb-theme";

  function applyTheme(dark) {
    document.documentElement.setAttribute("data-theme", dark ? "dark" : "light");
    var btn = document.getElementById("tb-theme-toggle");
    if (btn) btn.textContent = dark ? "☀️" : "🌙";
  }

  function initTheme() {
    var dark = localStorage.getItem(STORAGE_KEY) === "dark";
    applyTheme(dark);
  }

  function toggleTheme() {
    var dark = document.documentElement.getAttribute("data-theme") === "dark";
    var next = !dark;
    localStorage.setItem(STORAGE_KEY, next ? "dark" : "light");
    applyTheme(next);
  }

  function injectToggle() {
    var nav = document.querySelector("#navbarCollapse .navbar-nav.ms-auto") ||
      document.querySelector("#navbarCollapse .navbar-nav");
    if (!nav || document.getElementById("tb-theme-toggle")) return;
    var li = document.createElement("li");
    li.className = "nav-item";
    li.style.display = "flex";
    li.style.alignItems = "center";
    var btn = document.createElement("button");
    btn.id = "tb-theme-toggle";
    btn.type = "button";
    btn.setAttribute("aria-label", "Toggle dark mode");
    btn.textContent = document.documentElement.getAttribute("data-theme") === "dark" ? "☀️" : "🌙";
    btn.addEventListener("click", toggleTheme);
    li.appendChild(btn);
    nav.appendChild(li);
  }

  function injectProgressBar() {
    if (document.getElementById("tb-scroll-progress")) return;
    var bar = document.createElement("div");
    bar.id = "tb-scroll-progress";
    document.body.prepend(bar);
    var onScroll = function () {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      var p = h > 0 ? (window.scrollY / h) * 100 : 0;
      bar.style.width = Math.min(100, Math.max(0, p)) + "%";
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  initTheme();
  document.addEventListener("DOMContentLoaded", function () {
    injectToggle();
    injectProgressBar();
  });
})();
