import pytest
import pickle
import pandas as pd
import numpy as np

@pytest.fixture(scope="session") # Everytime i run pytest, this model will be loaded only once
def model():
    with open("xgb_car_price_model.pkl", "rb") as f:
        return pickle.load(f)

# Makes any input model ready to be passed to the model for prediction
def make_input(
    km_driven,
    mileage,
    age,
    fuel_type
):
    fuel_encoding = {
        "Petrol": [1, 0, 0],
        "Diesel": [0, 1, 0],
        "Electric": [0, 0, 1]
    }

    petrol, diesel, electric = fuel_encoding[fuel_type]

    return pd.DataFrame(
        [[km_driven, mileage, age, petrol, diesel, electric]],
        columns=["km_driven", "mileage", "age", "Petrol", "Diesel", "Electric"]
    )

def test_prediction_reasonable_range_multiple_samples(model):
    for _ in range(100):   # test 100 random combinations
        X = make_input(
            mileage=np.random.randint(5, 20),
            age=np.random.randint(0, 20),
            km_driven=np.random.randint(5000, 300000),
            fuel_type=np.random.choice(["Petrol", "Diesel", "Electric"])
        )

        price = model.predict(X)[0]
        if price<0:
            price=0
        assert 0 <= price <= 100

def test_age_pred_compare(model):
     
    X1 = make_input(
            mileage=10,
            age=5,
            km_driven=20000,
            fuel_type="Petrol"
        )
    X2 = make_input(
            mileage=10,
            age=15,
            km_driven=20000,
            fuel_type="Petrol"
        )

    price1 = model.predict(X1)[0]
    price2 = model.predict(X2)[0]


    assert price1>price2
