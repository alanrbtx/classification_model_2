from flask import Flask, request
import pickle
from skimage import io
from skimage.transform import resize
from skimage.color import rgb2gray

pkl_path = '/classification/neigh.pkl'
def load_pickle(file_path):
    neigh = pickle.load(open(file_path, 'rb'))
    return neigh

def predict_image(file_path):
    image = io.imread(file_path)
    if len(image.shape) == 4:
        image = image.squeeze(0)
    image = rgb2gray(resize(image, (200,200)))
    image = image.reshape(1, -1)

    neigh = load_pickle(pkl_path)
    res = neigh.predict(image)[0]
    if res == 0:
        print("MODEL PREDICTION: CAT")
        return {"result": "cat"}
    else:
        print("MODEL PREDICTION: DOG")
        return {"result": "dog"}

app = Flask(__name__)

@app.route('/get_test_prediction', methods=['GET'])
def get_test_result():
    res = predict_image("data/PetImages/Cat/3004.jpg")
    return res

@app.route('/get_real_prediction', methods=['POST'])
def get_real_result():
    res = predict_image(request.files["media"])
    return res


class TestClass():
    def test_load_picke(self):
        assert load_pickle('/classification/neigh.pkl')

    def test_predict(self):
        assert predict_image('/dataset/PetImages/Cat/3004.jpg')

    
if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')