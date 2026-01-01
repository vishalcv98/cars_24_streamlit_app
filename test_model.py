import pytest
import pickle
import pandas as pd
import numpy as np

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

def test_prediction_reasonable_range_multiple_samples(model):
    for _ in range(100):   # test 100 random combinations
        X = make_input(
            mileage=np.random.randint(1000, 200000),
            age=np.random.randint(0, 20),
            owners=np.random.randint(0, 4),
            fuel=np.random.choice(["Petrol", "Diesel", "Electric"])
        )

        price = model.predict(X)[0]
        assert 5 < price < 500