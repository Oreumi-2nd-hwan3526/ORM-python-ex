import numpy as np
from sklearn.linear_model import LinearRegression

X=np.array([[30],[40],[50],[60],[70]])

Y=np.array([100,150,200,250,300])

model=LinearRegression()

model.fit(X,Y)

size=int(input("size of house?"))
house_size=np.array([[size]])
predicted_price=model.predict(house_size)

print(f"predicted price of {size} size?",predicted_price)