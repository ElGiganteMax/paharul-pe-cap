import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

rng = np.random.default_rng(42)
N = 5000

# caracteristici (toate inventate, pentru exercitiu)
experienta = rng.uniform(0, 10, N)      # 0 = incepator, 10 = expert
viteza     = rng.uniform(0, 10, N)      # viteza dansului
rotiri     = rng.uniform(0, 10, N)      # cate rotiri face
lichid     = rng.uniform(0, 1, N)       # cat de plin e paharul (0-1)

X = np.column_stack([experienta, viteza, rotiri, lichid])

# regula "ascunsa": ce face paharul sa cada (plus zgomot)
risc = (-4 - 0.9*experienta + 0.6*viteza + 0.5*rotiri + 2.0*lichid
        + rng.normal(0, 0.5, N) + 6)
p_real = 1 / (1 + np.exp(-risc))
y = (rng.uniform(size=N) < p_real).astype(int)

# normalizam datele
medie, std = X.mean(axis=0), X.std(axis=0)
Xn = (X - medie) / std

model = keras.Sequential([
    layers.Input(shape=(4,)),
    layers.Dense(16, activation="relu"),
    layers.Dense(8, activation="relu"),
    layers.Dense(1, activation="sigmoid"),
])
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.fit(Xn, y, epochs=30, batch_size=32, validation_split=0.2, verbose=0)

# cazul nostru: dansator foarte bun, viteza medie, multe rotiri, pahar cu putina bautura
caz = np.array([[9.5, 6, 7, 0.2]])
p = model.predict((caz - medie) / std, verbose=0)[0][0]
print(f"Probabilitatea ca paharul sa cada: {p:.1%}")
