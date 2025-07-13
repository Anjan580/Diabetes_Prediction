import joblib

def make_prediction(input_data):
    model = joblib.load('save/DecisiontreeDiabetes.plk')

    prediction = model.predict([input_data])
    return prediction