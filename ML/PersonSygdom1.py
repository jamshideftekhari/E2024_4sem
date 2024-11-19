import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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

# Afhængig variabel (sygdomsstatus)
y = data[:, 2]

# Opdeling i trænings- og testdata
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Opret og træn logistisk regressionsmodel
model = LogisticRegression()
model.fit(X_train, y_train)

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
