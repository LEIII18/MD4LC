#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create Azimuthal Equidistant projection shapefiles for lunar impact craters.

This script reads crater center coordinates and diameters from a CSV file,
then generates vector shapefiles with Azimuthal Equidistant projections
centered on each crater.

"""

import os
import re
import math
import pandas as pd
from tqdm import tqdm
from shapely.geometry import Point, Polygon
import geopandas as gpd


def extract_coordinate(filename):
    """
    Extract latitude and longitude from a filename with crater naming format.

    Parameters:
        filename (str): Filename containing location codes (e.g., '177_58E58_44S').

    Returns:
        tuple: (longitude, latitude) in degrees.
    """
    matches = list(re.finditer(r'[a-zA-Z]', filename))
    if len(matches) < 2:
        raise ValueError(f"Filename '{filename}' does not contain valid lat/lon codes.")

    lon_index = matches[0].start()
    lat_index = matches[1].start()

    lon_char = filename[lon_index]
    lat_char = filename[lat_index]

    lon_value = float(filename[:lon_index].replace('_', '.'))
    lat_value = float(filename[lon_index + 1:lat_index].replace('_', '.'))

    lon = lon_value if lon_char == 'E' else 360 - lon_value
    lat = lat_value if lat_char == 'N' else -lat_value

    return lon, lat


def create_square(center, side_length):
    """
    Create a square polygon centered at the given point.

    Parameters:
        center (tuple): (longitude, latitude).
        side_length (float): Length of one side in meters.

    Returns:
        Polygon: Square polygon geometry.
    """
    center_point = Point(center[0], center[1])
    half_side = side_length / 2.0

    # cap_style=3 ensures a square-shaped buffer
    buffered = center_point.buffer(half_side, cap_style=3)
    coords = list(buffered.exterior.coords)[:4]  # four corners
    square = Polygon(coords)
    return square


def create_shapefile(output_path, center, side_length):
    """
    Create a shapefile with Azimuthal Equidistant projection for a square.

    Parameters:
        output_path (str): Path to save the shapefile.
        center (tuple): (longitude, latitude) of the center.
        side_length (float): Length of one side in meters.
    """
    polygon = create_square(center, side_length)

    # Define projection string
    projection = (
        'PROJCS["Moon_2000_Azimuthal_Equidistant",'
        'GEOGCS["GCS_Moon_2000",DATUM["D_Moon_2000",'
        'SPHEROID["Moon_2000_IAU_IAG",1737400,0]],'
        'PRIMEM["Reference_Meridian",0],UNIT["Degree",0.0174532925199433]],'
        'PROJECTION["Azimuthal_Equidistant"],'
        f'PARAMETER["latitude_of_origin",{center[1]}],'
        f'PARAMETER["central_meridian",{center[0]}],'
        'PARAMETER["false_easting",0],PARAMETER["false_northing",0],'
        'UNIT["metre",1]]'
    )

    gdf = gpd.GeoDataFrame(geometry=[polygon], crs=projection)
    gdf.to_file(output_path)


def main():
    """
    Main function to process crater data and generate shapefiles.
    """
    input_csv = 'data/crater_read.csv'
    output_base = 'data/clip/'
    df = pd.read_csv(input_csv)
    filenames = df.iloc[:, 0]
    diameters_km = df.iloc[:, 1]

    for i in tqdm(range(len(filenames))):
        try:
            center = extract_coordinate(filenames[i])
            diameter_m = diameters_km[i] * 1000
            buffer_length = diameter_m * 2

            crater_folder = os.path.join(output_base, str(i+1), 'shp')
            os.makedirs(crater_folder, exist_ok=True)

            output_file = os.path.join(crater_folder, f"{filenames[i]}.shp")
            create_shapefile(output_file, center, buffer_length)
        except Exception as e:
            print(f"Error processing {filenames[i]}: {e}")

    print("Processing complete.")


if __name__ == "__main__":
    main()
