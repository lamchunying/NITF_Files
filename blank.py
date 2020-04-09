from osgeo import gdal

fileformat = "NITF"
driver = gdal.GetDriverByName(fileformat)
metadata = driver.GetMetadata()
if metadata.get(gdal.DCAP_CREATE) == "YES":
    print("Driver {} supports Create() method.".format(fileformat))

if metadata.get(gdal.DCAP_CREATECOPY) == "YES":
    print("Driver {} supports CreateCopy() method.".format(fileformat))


dst_ds = driver.Create("blank.tif", xsize=2345, ysize=3844,
                    bands=8, eType=gdal.GDT_Byte)


dst_ds = None
