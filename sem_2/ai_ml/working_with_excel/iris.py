from sklearn.datasets import load_iris
import pandas as pd

# सही तरीका (no link here)
# load_iris() does NOT take a URL
# 👉 It already contains the dataset internally inside scikit-learn
iris = load_iris()

X = iris.data
y = iris.target

df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y

print(df.head())