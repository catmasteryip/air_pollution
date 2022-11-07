import geopandas as gpd
import shapely
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

district_dcca = pd.read_excel("../raw_data/SDI_2006_spatial map.xlsx",
                             engine = "openpyxl")