import arcpy, time, datetime, csv, sys, traceback
from arcpy import env
env.overwriteOutput = True

#work directory
wd = 'V:/GIS/projects/transit/tasks/201405_transit/data/'

#input table or GIS file
table   = wd+"processing/zonal_stats.gdb/station"+i+'_pts_'+j+"_kd_c_"+c+"_b_"+s+"_zon"
#output csv file
outfile = wd+'tables/zonal_stats/station'+i+'_'+j+'_kd_c_'+c+"_b_"+s+'_zon_raw.csv'

#--first lets make a list of all of the fields in the table
fields = arcpy.ListFields(table)
field_names = [field.name for field in fields]

with open(outfile,'wb') as f:
    w = csv.writer(f)
    #--write all field names to the output file
    w.writerow(field_names)

    #--now we make the search cursor that will iterate through the rows of the table
    for row in arcpy.SearchCursor(table):
        field_vals = [row.getValue(field.name) for field in fields]
        w.writerow(field_vals)
    del row
print "export zonal stats export is complete"