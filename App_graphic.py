import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def Graphic():
    df = pd.read_csv("archivos\\data_for_graphic.csv",encoding="UTF-8")
    sns.lineplot(x="intervalos",y="frecuencias", data=df)
    plt.show()

Graphic()