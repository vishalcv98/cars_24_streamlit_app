import pytest
import pickle
import pandas as pd

@pytest.fixture(scope="session")
def model():
    with open("xgb_car_price_model.pkl", "rb") as f:
        return pickle.load(f)

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

def test_price_decreases_with_age(model):
    X_new = make_input(30000, 18, 2, "Petrol")
    X_old = make_input(30000, 18, 10, "Petrol")

    price_new = model.predict(X_new)[0]
    price_old = model.predict(X_old)[0]

    assert price_new >= price_old

def test_prediction_reasonable_range(model):
    X = make_input(50000, 15, 6, "Diesel")
    price = model.predict(X)[0]

    assert 5 < price < 500