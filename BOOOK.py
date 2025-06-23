import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

books = pd.read_csv(
    "data/BX-Books.csv",
    sep=";",                 # columns are semicolon-separated
    encoding="ISO-8859-1",   # same as 'latin-1' but clearer name
    quotechar='"',           # book titles/descriptions are wrapped in "
    escapechar="\\",         # backslash escapes stray quotes
    on_bad_lines="skip",     # skip the handful of badly formed rows
    low_memory=False         # load in one pass to keep dtypes consistent
)

books