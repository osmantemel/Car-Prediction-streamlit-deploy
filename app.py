import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import streamlit as st

df = pd.read_excel("cars.xls")

X = df.drop("Price", axis=1)
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing pipeline
preprocess = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), ["Doors", "Cylinder", "Mileage", "Liter"]),
        ("cat", OneHotEncoder(), ["Make", "Model", "Trim", "Type"])
    ]
)

my_model = LinearRegression()

pipe = Pipeline(steps=[
    ('preprocess', preprocess),
    ('model', my_model)
])

pipe.fit(X_train, y_train)

# Price tahmin fonksiyonu
def price(make, model, trim, mileage, car_type, cylinder, liter, doors, cruise, sound, leather):
    input_data = pd.DataFrame({'Make': [make],
                               'Model': [model],
                               'Trim': [trim],
                               'Mileage': [mileage],
                               'Type': [car_type],
                               'Cylinder': [cylinder],
                               'Liter': [liter],
                               'Doors': [doors],
                               'Cruise': [cruise],
                               'Sound': [sound],
                               'Leather': [leather]})
    prediction = pipe.predict(input_data)[0]
    return prediction

st.title("Car Price Prediction")
st.write("Araba özelliklerini seçin")

make = st.selectbox("Marka", df['Make'].unique())
model = st.selectbox("Model", df[df['Make'] == make]['Model'].unique())
trim_options = df[(df['Make'] == make) & (df['Model'] == model)]['Trim'].unique()
Trim = st.selectbox("Trim", trim_options)
mileage = st.number_input('Kilometre', 100, 60000)
car_type = st.selectbox("Araç Tipi", df['Type'].unique())

cylinder = st.number_input('Silindir Sayısı', 1, int(df['Cylinder'].max()))

liter = st.number_input('Litre', 1.0, float(df['Liter'].max()))

doors = st.number_input('Kapı Sayısı', 1, int(df['Doors'].max()))

cruise = st.radio("Cruise Control", [True, False])

sound = st.radio("Sound System", [True, False])

leather = st.radio("Leather Seats", [True, False])

if st.button("Tahmin"):
    prediction = price(make, model, Trim, mileage, car_type, cylinder, liter, doors, cruise, sound, leather)
    st.write(f"Tahmin edilen fiyat: {prediction}")
