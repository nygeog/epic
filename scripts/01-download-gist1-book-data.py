import re, urllib, time, zipfile, os

stop_time = 3

download_location = 'E:/'
#EXAMPLE for Mac download_location = '/Volumes/Echo/GIS/data/census/2000/blocks/'

url = 'https://dl.dropboxusercontent.com/u/36281098/epic/data/gist1_instructor_edition.zip'
outzip = download_location + 'gist1_instructor_edition.zip'

print 'downloading... ' + url
urllib.urlretrieve(url, outzip)

print 'unzipping... ' + outzip
zipfile.ZipFile(outzip).extractall(download_location)

#os.remove(download_location+outzip)
#print "Deleting... " + stfi + "'s ZIP file"

#wait 3 seconds in case network connection is slow
time.sleep(stop_time)

print 'completed download and zip extraction'