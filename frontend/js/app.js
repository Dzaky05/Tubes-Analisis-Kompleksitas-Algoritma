const btn = document.getElementById("btnAnalisis");
const inputN = document.getElementById("inputN");
const hasilDiv = document.getElementById("hasil");
const loading = document.getElementById("loading");

btn.addEventListener("click", jalankan);

function generateRandomData(n) {
  const data = [];
  for (let i = 0; i < n; i++) {
    data.push(Math.floor(Math.random() * 100) + 1);
  }
  return data;
}

async function jalankan() {
  const n = parseInt(inputN.value);

  if (!n || n <= 0) {
    alert("Masukkan nilai n yang valid");
    return;
  }

  const data = generateRandomData(n);

  loading.classList.remove("hidden");
  hasilDiv.classList.add("hidden");

  try {
    const res = await fetch("http://127.0.0.1:5000/api/analisis-modus", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ data })
    });

    const json = await res.json();

    if (json.status !== "berhasil") {
      throw new Error(json.pesan);
    }

    tampilkan(json);

  } catch (err) {
    alert("Gagal menghubungi backend:\n" + err.message);
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
    <div class="result-item">Jumlah Data (n): <b>${res.jumlahData}</b></div>
    <div class="result-item">⏱ Iteratif: <b>${it.toFixed(2)} µs</b></div>
    <div class="result-item">⏱ Rekursif: <b>${rek.toFixed(2)} µs</b></div>
    <div class="winner">🏆 Lebih Cepat: ${winner}</div>
  `;

  hasilDiv.classList.remove("hidden");
  tampilkanGrafik(it, rek);
}

function tampilkanGrafik(iteratif, rekursif) {
  const card = document.getElementById("grafikCard");
  const ctx = document.getElementById("grafikWaktu");

  card.classList.remove("hidden");

  if (chart) chart.destroy();

  chart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["Iteratif", "Rekursif"],
      datasets: [{
        label: "Waktu Eksekusi (µs)",
        data: [iteratif, rekursif],
        backgroundColor: ["#43c06d", "#ff6b6b"]
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: { beginAtZero: true }
      }
    }
  });
}
