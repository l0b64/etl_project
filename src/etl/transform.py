from typing import List
import pandas as pd

pd.set_option("mode.chained_assignment", None)


def flatten_json_data(raw_data: pd.DataFrame):
    flattened_df = pd.json_normalize(raw_data)
    return flattened_df


def normalize_fuel_json_dataset(raw_data: pd.DataFrame):
    normalized_df = flatten_json_data(raw_data["records"])
    return normalized_df


def clean_fuel_dataset(normalized_df: pd.DataFrame):
    normalized_df = normalized_df[
        [
            "fields.id",
            "fields.address",
            "fields.reg_name",
            "fields.brand",
            "fields.price_e10",
            "fields.price_sp98",
            "fields.price_gazole",
            "fields.fuel",
            "fields.price_e85",
            "fields.price_gplc",
            "fields.price_sp95",
        ]
    ]
    replace_columns_names(
        normalized_df,
        [
            "id",
            "address",
            "reg_name",
            "brand",
            "price_e10",
            "price_sp98",
            "price_gazole",
            "fuel",
            "price_e85",
            "price_gplc",
            "price_sp95",
        ],
    )
    return normalized_df


def replace_columns_names(dataframe: pd.DataFrame, new_columns_names: List):
    new_columns_names = dict(zip(dataframe.columns, new_columns_names))
    dataframe.rename(columns=new_columns_names, inplace=True)
