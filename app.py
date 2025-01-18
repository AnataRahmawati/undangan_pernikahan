from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint untuk menerima data lokasi
@app.route('/track', methods=['POST'])
def track_location():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if latitude and longitude:
        # Simpan lokasi ke file atau database
        with open('locations.txt', 'a') as file:
            file.write(f"Latitude: {latitude}, Longitude: {longitude}\n")
        return jsonify({"message": "berhasil disimpan."}), 200
    return jsonify({"error": "Data lokasi tidak lengkap."}), 400

# Menyediakan frontend HTML
@app.route('/')
def home():
    return open('templates/index.html').read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

