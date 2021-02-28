# ------------------- Library for Graphs --------------------

from numpy import random
import matplotlib.pyplot as graphics
import seaborn as abu_kowser_  # create object as "abu_kowser_"

# ------------ Create Graph -----------------

abu_kowser_.distplot(random.poisson(lam=2, size=1000), kde=False, color='green')

graphics.show()
