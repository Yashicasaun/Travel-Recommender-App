import pandas as pd
import numpy as np
import os


def read_data(city):
    path = os.path.join(r"../data", city + ".csv")
    df = pd.read_csv(path)
    return df


def group_based_imputation(df, radius):
    # Iterate over the DataFrame
    for index, row in df.iterrows():
        if pd.isnull(row['rating']):
            lat = row['latitude']
            lon = row['longitude']
            # Filter the DataFrame to nearby locations within the specified radius
            nearby_df = df[(df['latitude'] - lat) ** 2 + (df['longitude'] - lon) ** 2 <= radius ** 2]
            if not nearby_df.empty:
                group_rating_mean = nearby_df['rating'].mean()
                # group_rating_median = nearby_df['rating'].median()
                imputed_rating = group_rating_mean
                df.loc[index, 'rating'] = imputed_rating

    return df


def get_profit_table(df):
    i = 0
    radius = 5 / 111  # 5 km radius. 1 degree lat/long shift is 111 kms
    while df['rating'].isna().any():
        radius = radius + i / 111
        df = group_based_imputation(df, radius)
        i = i + 1

    df = df[["name", "rating"]]
    df.set_index("name", inplace=True)
    return df

