from flask import Flask
import find_park_spot as fps

app = Flask(__name__)
@app.route('/')
def hello_world():
    return "hello jsr, welcome to the parking spot finder app"

@app.route('/find_nearest_parkingspot', methods = ["GET"])
def get_spot():
   spot = fps.get_parking_spot()
   return spot

if __name__ == '__main__':
    app.run(debug=True)