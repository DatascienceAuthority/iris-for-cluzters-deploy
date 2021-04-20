import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))
class_names = ['setosa', 'versicolor', 'virginica']

def predict(data):
	sepal_length = float(data['Sepal Length'])
	sepal_width = float(data['Sepal Width'])
	petal_length = float(data['Petal Length'])
	petal_width = float(data['Petal Width'])

	numpy_array = np.array([sepal_length, sepal_width, petal_length, petal_width]).reshape(1, 4)
	# Predict
	class_prediced = int(model.predict(numpy_array)[0])

	output = class_names[class_prediced]
	return output

