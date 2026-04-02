import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r'C:\Users\piyush kumar\OneDrive\Desktop\GitHub\PESU\sem_2\ai_ml\slr_mlr\housing_data.csv')
df.head()


df.info()
df.describe()

le = LabelEncoder()


cols = ['driveway', 'recroom', 'fullbase', 
        'gashw', 'airco', 'prefarea']

for col in cols:
    df[col] = le.fit_transform(df[col])


X = df.drop('price', axis=1)   # Features
y = df['price']                # Target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,      # 20% test, 80% train
    random_state=42     # for reproducibility
)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

X = df[['lotsize']]   # only ONE feature → SLR
y = df['price']

model = LinearRegression()
model.fit(X, y)

print(model.coef_)
print(model.intercept_)

y_pred = model.predict(X_test)

# mse indicates- > understanding the magnitude of the error
# the lower mse indicate 

# it provides 