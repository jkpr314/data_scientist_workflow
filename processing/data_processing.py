import pandas as pd

df = pd.read_excel('../data/API_NY.GDP.MKTP.CD_DS2_en_excel_v2_4251142.xls')

df.columns = df.loc[2]
df = df[3:].reset_index(drop=True)

temp = df[df.columns[4:]].transpose()
temp.columns = df['Country Code']

temp.index.name = 'year'
temp.to_parquet('../data/country_year_gdp.parquet')