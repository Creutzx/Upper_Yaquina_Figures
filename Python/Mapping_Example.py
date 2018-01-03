import arcpy

mxd = arcpy.mapping.MapDocument(r'\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\Upper_Yaquina_TMDL_BC_Automated_V2.mxd')
arcpy.mapping.ExportToPDF(mxd, "C:\Student\MapScripting10_0\Watersheds.pdf")
