#todo: call the distance value here, collect the predicted value and send it to pygame code via api
import numpy as np


def predicted_distance(calculated_irl_distance):
    try:
        #zuzun = min(distances)
        x = [20, 25, 30, 35, 40, 45, 50]
        y = [0.0404, 0.0487, 0.0576, 0.0605, 0.0661, 0.0782, 0.0871]
        mymodel = np.poly1d(np.polyfit(x, y, 3))
        gen = calculated_irl_distance*mymodel(calculated_irl_distance)
        print(gen)
        return gen
    except:
        print("Error: Predicted Value Error")


