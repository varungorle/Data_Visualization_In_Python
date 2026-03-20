import pandas as pd
import matplotlib.pyplot as plt
data = {"Sales": [200, 400, 600, 800]}
df = pd.DataFrame(data)
df.plot(kind="bar", title="Sales Data")
plt.xlabel("Index")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()