import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix


# Datasæt: alder, kolesteroltal og sygdomsstatus (1 = ja, 0 = nej)
data = np.array([
    [25, 200, 0],
    [30, 210, 0],
    [35, 230, 0],
    [40, 250, 1],
    [45, 270, 1],
    [50, 290, 1],
    [55, 310, 1],
    [60, 330, 1]
])

# Uafhængige variabler (alder og kolesteroltal)
X = data[:, :2]
print("X: ")
print(X)

# Afhængig variabel (sygdomsstatus)
y = data[:, 2]

# Opdeling i trænings- og testdata
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("X_train: ")
print(X_train)

# Opret og træn logistisk regressionsmodel
model = LogisticRegression()
model.fit(X_train, y_train)

# Forudsigelser på testdata
y_pred = model.predict(X_test)
print("y_pred: ")
print(y_pred)
print("y_test: ")
print(y_test)   

# Modelpræcision
accuracy = accuracy_score(y_test, y_pred)
print(f"Modelpræcision: {accuracy:.2f}")


# Definer grænser for alderen og kolesteroltallet
x_min, x_max = X[:, 0].min() - 5, X[:, 0].max() + 5
y_min, y_max = X[:, 1].min() - 20, X[:, 1].max() + 20

# Opret et gitter af punkter
xx, yy = np.meshgrid(np.arange(x_min, x_max, 1),
                     np.arange(y_min, y_max, 1))

# Forudsig sandsynligheder for hvert punkt i gitteret
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot beslutningsgrænsen
plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.Paired)

# Plot data
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor="k", cmap=plt.cm.Paired)
plt.xlabel("Alder")
plt.ylabel("Kolesteroltal")
plt.title("Logistisk Regression: Beslutningsgrænse")
plt.colorbar(label="Sygdomsstatus")
plt.show()
