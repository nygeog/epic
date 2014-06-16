#code 1 make feature layer:

datalayer = "C:/GIS/class/data/gist1_instructor_edition/Data/UnitedStates.gdb/NYTracts"

arcpy.MakeFeatureLayer_management(datalayer, 'NY Tracts')