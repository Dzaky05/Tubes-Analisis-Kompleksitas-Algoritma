const btn = document.getElementById("btnAnalisis");
const input = document.getElementById("inputData");
const hasilDiv = document.getElementById("hasil");
const loading = document.getElementById("loading");

btn.addEventListener("click", jalankan);
input.addEventListener("keydown", e => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    jalankan();
  }
});

async function jalankan() {
  const raw = input.value.trim();
  if (!raw) return alert("Masukkan data terlebih dahulu");

  const data = raw.split(",").map(x => Number(x.trim()));
  if (data.some(isNaN)) return alert("Input harus angka");

  loading.classList.remove("hidden");
  hasilDiv.classList.add("hidden");

  try {
    const res = await fetch("http://127.0.0.1:5000/api/analisis-modus", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ data })
    });

    const json = await res.json();
    tampilkan(json);
  } catch {
    alert("Gagal menghubungi backend");
  } finally {
    loading.classList.add("hidden");
  }
}

let chart = null;

function tampilkan(res) {
  const it = res.hasil.iteratif.rataRata * 1_000_000;
  const rek = res.hasil.rekursif.rataRata * 1_000_000;

  const winner = it < rek ? "Iteratif" : "Rekursif";

  hasilDiv.innerHTML = `
    <h2>📊 Hasil Analisis</h2>
    <div class="result-item">Jumlah Data: <b>${res.jumlahData}</b></div>
    <div class="result-item">⏱ Iteratif: <b>${it.toFixed(2)} µs</b></div>
    <div class="result-item">⏱ Rekursif: <b>${rek.toFixed(2)} µs</b></div>
    <div class="winner">🏆 Lebih Cepat: ${winner}</div>
  `;

  hasilDiv.classList.remove("hidden");

  tampilkanGrafik(it, rek);
}

function tampilkanGrafik(iteratif, rekursif) {
  const card = document.getElementById("grafikCard");
  const ctx = document.getElementById("grafikWaktu").getContext("2d");

  card.classList.remove("hidden");

  if (chart) chart.destroy();

  chart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["Iteratif", "Rekursif"],
      datasets: [{
        label: "Waktu Eksekusi (µs)",
        data: [iteratif, rekursif],
        backgroundColor: ["#43c06d", "#ff6b6b"],
        borderRadius: 10
      }]
    },
    options: {
      responsive: true,
      animation: {
        duration: 1200,
        easing: "easeOutQuart"
      },
      scales: {
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: "Mikrodetik (µs)"
          }
        }
      }
    }
  });
}

