import numpy as np

def predict_fire(model, temperature, humidity, wind, rain):
    data = np.array([[temperature, humidity, wind, rain]])
    prediction = model.predict(data)

    return prediction[0]
