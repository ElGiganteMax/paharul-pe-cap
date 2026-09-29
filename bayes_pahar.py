# Probabilitati inventate, doar pentru exercitiu
p_repetitii = 0.7            # cat de probabil e sa fi repetat (nunta, miza mare)

p_cade_cu_rep = 0.02         # daca au repetat, paharul cade rar
p_cade_fara_rep = 0.15       # daca n-au repetat, cade mai des

# probabilitatea totala ca paharul sa cada (formula probabilitatii totale)
p_cade = p_repetitii * p_cade_cu_rep + (1 - p_repetitii) * p_cade_fara_rep
print(f"P(cade) inainte sa stim ceva: {p_cade:.1%}")

# Bayes: stiind ca paharul NU a cazut, cat de probabil e ca au repetat?
p_nu_cade_cu_rep = 1 - p_cade_cu_rep
p_nu_cade = 1 - p_cade
p_rep_dat_nu_cade = p_nu_cade_cu_rep * p_repetitii / p_nu_cade
print(f"P(au repetat | paharul nu a cazut): {p_rep_dat_nu_cade:.1%}")