import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_math = {'value' : [4, 5, 4, 5, 5, 3, 5, 4, 5, 4]}
df = pd.DataFrame(data_math)

df['value'].hist()
plt.show()