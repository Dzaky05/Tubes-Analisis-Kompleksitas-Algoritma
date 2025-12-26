from flask import Flask, request, jsonify
from flask_cors import CORS

from pengujian import ujiModus
from validasi import validasiData

app = Flask(__name__)
CORS(app)

@app.route("/api/analisis-modus", methods=["POST"])
def analisisModus():
    try:
        payload = request.get_json()
        data = payload.get("data")

        validasiData(data)
        hasil = ujiModus(data)

        return jsonify({
            "status": "berhasil",
            "jumlahData": len(data),
            "hasil": hasil
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "pesan": str(e)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)
