'''
| Data Type                              | Missing Value Treatment                                                   |
| -------------------------------------- | ------------------------------------------------------------------------- |
| Numerical (Age, Marks, Salary)         | Replace with **Mean**                                                     |
| Categorical (Gender, City, Department) | Replace with **Mode**                                                     |
| One missing value                      | Calculate mean/mode from available values                                 |
| Two or more missing values             | Calculate mean/mode from available values and replace all missing entries |
'''


# python code for pre-processing the dataset
'''
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("students.csv")

# 1. Remove duplicates
df = df.drop_duplicates()

# 2. Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())

# 3. Label Encoding
le = LabelEncoder()
df["Gender"] = le.fit_transform(df["Gender"])

# 4. Feature Scaling
scaler = StandardScaler()
df[["Age", "Marks"]] = scaler.fit_transform(df[["Age", "Marks"]])

# 5. Feature Selection
X = df.drop("Result", axis=1)
y = df["Result"]

selector = SelectKBest(score_func=f_classif, k=2)
X_selected = selector.fit_transform(X, y)

# 6. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_selected,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
'''