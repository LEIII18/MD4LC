# -*- coding=UTF-8 -*-
# author:ldh
"""
Clip the Raster data from the shapefile
And keep the clip data's spacial reference is same as the shapefile.
"""

import arcpy
import os




def clip_other_data(other_rasterfile, frames_folderPath, result_clipRasterPath):
    prj = arcpy.Describe(other_rasterfile).spatialReference
    shp= frames_folderPath
    Output_Coordinate_System = arcpy.Describe(shp).spatialReference
    tempEnvironment0 = arcpy.env.outputCoordinateSystem
    arcpy.env.outputCoordinateSystem = Output_Coordinate_System

    frame_name = os.path.basename(shp)[:-4]
    out_raster = result_clipRasterPath + '\\' + frame_name + '.tif'

    arcpy.gp.ExtractByMask_sa(other_rasterfile, shp, out_raster)
    arcpy.env.outputCoordinateSystem = tempEnvironment0

def main():
    """
    Main function to clip the ratser
    """
    rasterfile = r"data/YourRasterFileName.tif" # write your target raster file here
    prj = arcpy.Describe(rasterfile).spatialReference
    shapefile = r"data/54_74E5_56N.shp"
    result_clipRasterPath = r"data/clipRaster"
    os.makedirs(result_clipRasterPath)
    clip_other_data(rasterfile, shapefile, result_clipRasterPath)
    print("*****OK!!!******")

if __name__=='__main__':
    main()