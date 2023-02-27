import sys
import os
import pytest
from src.etl import transform
import pandas as pd

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")


class TestFuelDataset:
    def test_uc_fuels_prices(self):
        # Given

        path = os.path.dirname(os.path.abspath(__file__))
        data_raw_file = open(path + "/input.json")
        expected_file = open(path + "/output.json")

        raw_data_df = pd.read_json(data_raw_file)
        expected_df = pd.read_json(expected_file)

        # When
        final_df = transform.clean_fuel_dataset(raw_data_df)

        # Then
        assert final_df.equals(expected_df)
