from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/nama_provinsi', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.nama_provinsi()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_ipm', methods=['POST'])
def predict_ipm():
    harapan_hidup = float(request.form['harapan_hidup'])
    provinsi = request.form['provinsi']
    ppk = int(request.form['ppk'])
    ls_mean = float(request.form['ls_mean'])
    hls = float(request.form['hls'])

    response = jsonify({
        'predicts_ipm': util.predict_ipm(provinsi,harapan_hidup,ppk,ls_mean,hls)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Indonesia's HDI prediction")
    util.load_saved_artifacts()
    app.run()