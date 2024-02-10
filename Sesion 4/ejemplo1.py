from sklearn.linear_model import LinearRegression

X_train = [[1024], [2048], [3072], [4096], [5120], [6144], [7168], [8162]]

Y_train = [1, 2, 3, 4, 5, 6, 7, 8]

model = LinearRegression()
model.fit(X_train, Y_train)

kb = int(input("Ingrese el valor en kb: "))

kb_to_convert = [[kb]]
preddicted_mb = model.predict(kb_to_convert)

print(f"{kb} kb equivalen aproximadamente a {preddicted_mb[0]} MB")