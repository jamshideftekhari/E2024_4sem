import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Datasæt: Alder, kolesteroltal og sygdomsstatus (1 = ja, 0 = nej)
data = np.array([
    [18, 180, 0], [20, 190, 0], [22, 200, 0], [24, 210, 0], [26, 220, 0],
    [28, 230, 1], [30, 240, 1], [32, 250, 1], [34, 260, 0], [36, 270, 0],
    [38, 280, 1], [40, 290, 1], [42, 300, 1], [44, 310, 1], [46, 320, 0],
    [48, 330, 1], [50, 340, 1], [52, 350, 1], [54, 360, 1], [56, 370, 1],
    [58, 380, 1], [60, 390, 1]
])

# Uafhængige variabler (alder og kolesteroltal)
X = data[:, :2]

# Afhængig variabel (sygdomsstatus)
y = data[:, 2]

# Opdeling i trænings- og testdata
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Opret og træn logistisk regressionsmodel
model = LogisticRegression()
model.fit(X_train, y_train)

# Forudsigelser på testdata
y_pred = model.predict(X_test)

print("y_pred: ")
print(y_pred)
print("y_test: ")
print(y_test)

# accuracy = antal korrekte forudsigelser / samlet antal forudsigelser (labels)
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

# Plot træningsdata
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, edgecolor="k", marker='o', label="Training Data")

# Plot testdata
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, edgecolor="k", marker='s', label="Test Data")

# Labels og titel
plt.xlabel("Alder")
plt.ylabel("Kolesteroltal")
plt.title("Logistisk Regression: Trænings- og Testdata med Beslutningsgrænse")
plt.legend()
plt.show()
