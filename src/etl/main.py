import extract_data, transform, load
import os

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
HOST = os.getenv("POSTGRES_HOST")
DB = os.getenv("POSTGRES_DB")
PORT = os.getenv("POSTGRES_PORT")
amqp_url = os.environ["AMQP_URL"]
api_url = os.environ["API_URL"]
URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{HOST}:{PORT}/{DB}"


def main():

    print("--- ETL job started ---")
    extracted_df = extract_data.extract_json_data_from_url(api_url)

    print("--- EXTRACTION DONE ---")

    normalized_data_df = transform.normalize_fuel_json_dataset(extracted_df)
    cleaned_df = transform.clean_fuel_dataset(normalized_data_df)
    print("--- DATA NORMALIZED ---")

    load.load_to_db(cleaned_df, "fuels_dataset", URL)
    print("--- DATA LOADED TO DATABASE ---")

    serialized_df = cleaned_df.to_json(orient="records")
    load.push_message_to(amqp_url, serialized_df, "fuel_dataset")

    print("--- ETL job finished ---")


if __name__ == "__main__":
    main()
