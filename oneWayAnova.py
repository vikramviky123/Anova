import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway
from scipy.stats import f


def oneWayAnova(df: pd.DataFrame) -> None:
    """The function Conducts Test for One Way Anova

    Args:
        df (pd.DataFrame): Give the dataframe containing values of any numnber of columns

    Returns:
        None : Returns None
        Prints various parameters and satistical values with Hypothesis Inference
    """

    alpha = 0.05
    n = df.count().sum()
    c = df.count().count()

    Xg = np.mean(df)  # Mean of DataFrame
    # Sum of total squares SST = Σ(Xij - XG)2
    SST = ((df-Xg)**2).sum().sum()
    # Sum of squares Among Group SSTR = Σ nj (X̅j - XG)2
    SSTR = (((df.mean() - Xg)**2)*df.count()).sum()
    # Sum of squares Across Groups SSE = Σ(X̅ij - Xj)^2
    SSE = (df.subtract(df.mean())**2).sum().sum()
    # SSTR/(c-1)
    MSTR = SSTR/(c-1)
    # SSE/(n-c)
    MSE = SSE/(n-c)

    F_stat = MSTR/MSE

    p_value = 1 - f.cdf(F_stat, c-1, n-c)

    print("Total number of Data Points --> n =", n)
    print("Total number of Columns/Groups --> c =", c)
    print("-"*50)
    print("Mean of Data :", round(Xg, 4))
    print("-"*50)
    print("Sum of total squares SST = Σ(Xij - XG)^2           =", round(SST, 4))
    print("Sum of squares Among Group SSTR = Σ nj (X̅j - XG)^2 =", round(SSTR, 4))
    print("Sum of squares Across Groups SSE = Σ(X̅ij - Xj)^2   =", round(SSE, 4))
    print("-"*50)
    print("MSTR = SSTR/(c-1)           =", round(MSTR, 4))
    print("MSE = SSE/(n-c) =", round(MSE, 4))
    print("-"*50)
    print("F_Statistic = MSTR/MSE =", round(F_stat, 4))
    print("P_Value................=", round(p_value, 4))

    print("-"*100)
    if p_value < alpha:
        print("HENCE, We Reject Null Hypothesis------> atleast one set of means NOT Equal")
    else:
        print(
            f"HENCE, We Accept Null Hypothesis------> with {100-alpha*100}% confidence all means are Equal")
    print("-"*100)

    return None
