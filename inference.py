import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))
class_names = ['setosa', 'versicolor', 'virginica']

def predict(df):
	df = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]

	numpy_array = df.to_numpy()
	# Predict
	predictions = model.predict(numpy_array)
	#return str(predictions)
	output = [class_names[class_predicted] for class_predicted in predictions]
	return output