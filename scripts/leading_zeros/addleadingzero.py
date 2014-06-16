lenCalc(str(!FIPS!))



def lenCalc(fips):
  if len(fips) == 4:
    return '0' + fips
  else:
    return fips

