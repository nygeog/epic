import pandas as pd

xlsFile = '/Users/danielmsheehan/Dropbox/Public/epic/data/student_example_data/vietnam/HCMCFacility_Listing_By_UniqueID_Address_ImplementingMechanism\ \(18June_2014\).xlsx'

pd.io.excel.read_excel(xlsFile, 'BY ID and ADDRESS ONLY')