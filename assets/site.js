// Dil: telefonu Türkçe olan ziyaretçi İngilizce sayfaya ilk geldiğinde Türkçe
// karşılığına yönlenir. Dil anahtarına dokunulursa seçim hatırlanır ve bir daha
// yönlendirilmez. Depolama kapalıysa (gizli sekme) sessizce geçer.
(function () {
  var KEY = "dv-lang";
  var html = document.documentElement;
  var current = html.getAttribute("lang");
  // Dil anahtarındaki göreli bağlantı (site nerede yayınlanırsa yayınlansın çalışır).
  var alt = document.querySelector('a[data-set-lang="tr"]');

  function read() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function save(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }

  document.querySelectorAll("[data-set-lang]").forEach(function (a) {
    a.addEventListener("click", function () { save(a.getAttribute("data-set-lang")); });
  });

  var chosen = read();
  var prefersTr = (navigator.languages || [navigator.language || ""])
    .some(function (l) { return String(l).toLowerCase().indexOf("tr") === 0; });
  if (current === "en" && !chosen && prefersTr && alt) {
    save("tr");
    location.replace(alt.getAttribute("href") + location.hash);
  }
})();
