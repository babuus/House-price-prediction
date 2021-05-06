import utill
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/get_location_name')
def hi():
    response = jsonify({
        # 'artifacts' : utill.load_saved_artifacts(),
        'locations': utill.get_location_names()
    })
    return response

@app.route('/predict', methods=['post'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = float(request.form['bhk'])
    bath = float(request.form['bath'])
    balcony = float(request.form['balcony'])
    response = jsonify({
        # 'artifacts': utill.load_saved_artifacts(),
        'locations': utill.get_estimated_price(location,total_sqft, bhk, bath, balcony)
        # 'location': utill.get_estimated_price("Ejipura",1000.0, 2.0, 2.0, 0)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
if __name__ == "__main__":
    print("starting python server")
    app.run()