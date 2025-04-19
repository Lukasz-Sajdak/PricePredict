from flask import Flask, request, jsonify
import util
app = Flask(__name__)

util.load_saved_artifacts()  # Ładowanie danych przy starcie aplikacji

@app.route('/get_location_names')
def get_location_names():
    locations = util.get_location_names()
    print("Locations retrieved:", locations)  # Logowanie w konsoli
    response = jsonify({
        'locations': locations
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    # Pobranie danych z form-data
    total_sqft = float(request.form.get('total_sqft'))
    location = request.form.get('location')
    bhk = int(request.form.get('bhk'))
    bath = int(request.form.get('bath'))

    # Zwrócenie odpowiedzi w formacie JSON
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting server")
    app.run()
