# NITF_Files
Creation of NITF files 

(1) Blank NITF files 
- reference to Gdal's official tutorial 
- https://gdal.org/tutorials/raster_api_tut.html#opening-the-file
- using the provided Create() function 

(2) Checkerboard NITF files 
- create a raster from array 
- https://pcjericks.github.io/py-gdalogr-cookbook/raster_layers.html

(3) Diagnosis.py 
- Open any image file by changing parameter in Open() 
- Return:
- Driver (File type)
- Size 
- Projection
- Origin 
- Pixel Size 
 
set driver = NITF 
Source code: https://gdal.org/python/index.html



