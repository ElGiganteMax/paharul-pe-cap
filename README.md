# Paharul pe cap 🥤

Estimarea probabilității ca un pahar așezat pe cap să cadă în timpul
unui dans tradițional — folosind **inferență bayesiană** și o **rețea neuronală**.

## Cum a început

Clip: O mare vedeta pop, executa un dans tradițional, cu un paharpe cap partial umplut, la o nuntă la Pristina.

Primul meu gând: *„paharul ăla nu are cum să cadă."*
Al doilea gând: *„dar cât de sigur sunt, matematic?"*
Al treilea gând: *„și dacă totuși cade — ce magnitudine ar avea eșecul?"*

Așa au apărut trei întrebări diferite:

1. **Probabilitate** — P(pahar cade)?
2. **Condiționare** — cum se schimbă P dacă au fost N repetiții reușite?
3. **Decizie** — care e costul asimetric al unei greșeli, ținând cont
   că un eșec ar deveni viral?

## Abordare

| Fișier | Metodă | Idee |
|--------|--------|------|
| `bayes_pahar.py` | Teorema lui Bayes | Pornește de la un prior intuitiv, îl ajustează cu factori |
| `keras_pahar.py` | Rețea neuronală | Învață relația parametri → cădere din date |

Dacă ambele metode ajung la concluzii similare, câștigăm încredere.
Dacă diferă, avem întrebări noi de explorat.

## Structură
paharul-pe-cap/
├── bayes_pahar.py # model bayesian
├── keras_pahar.py # rețea neuronală
└── README.md


## Factori luați în considerare

| Factor | Efect asupra P(cade) |
|--------|----------------------|
| Tip pahar (înalt, greu) | ↑ |
| Unghiul capului | ↑ |
| Viteza mișcării | ↑ |
| Experiența dansatorului | ↓ |
| Repetiții anterioare reușite | ↓ |
| Suprafață (păr, pălărie) | ↑ sau ↓ |
| Oboseală / alcool | ↑ |
| Prezența publicului | ↑ sau ↓ |

## Instalare

```bash
pip install numpy tensorflow

python bayes_pahar.py
python keras_pahar.py

Proiect de explorare — combinație între curiozitate personală
și exersarea metodelor probabilistice.
