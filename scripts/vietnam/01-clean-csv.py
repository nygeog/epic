import pandas as pd

inCSV = '/Users/danielmsheehan/Dropbox/Public/epic/data/student_example_data/vietnam/addresses_out.csv'
outCSV = '/Users/danielmsheehan/Dropbox/Public/epic/data/student_example_data/vietnam/addresses_out_pandas.csv'

df = pd.read_csv(inCSV)

df = df[['latitude','longitude']]

df.index.name = 'uid'

df['duid'] = df.index + 1

df.to_csv(outCSV)