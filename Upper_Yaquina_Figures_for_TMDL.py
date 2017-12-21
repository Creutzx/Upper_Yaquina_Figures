import arcpy

#input info in same way as Mid-Coast map outline
#created new .lyr and .mxd files specific to upper yaquina watershed

chr_dir_work = r'\\DEQHQ1\TMDL_WR\MidCoast\GIS\Figures\python\makelocinstate'
chr_map_doc_base = r'\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\Upper_Yaquina_TMDL_BC_Automated_V2.mxd'
chr_map_doc_new = r'\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\python\makelocinstate\Upper_Yaquina.mxd'
chr_png_map_new = r'\\DEQHQ1\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\Up_Yaq.png'
chr_lyr_name_sel = r'HUC 10'
chr_lyr_sym_wtsd = r'\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Layer\upper_yaquina_official_huc_10.lyr'
chr_lyr_sym_state = r'\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\or_state_boundary_for_inset.lyr'

# get the base map document

mxd_base = arcpy.mapping.MapDocument(chr_map_doc_base)
# make a copy that will be changed

mxd_base.saveACopy(chr_map_doc_new)
del mxd_base
# get new map doc to edit
mxd_new = arcpy.mapping.MapDocument(chr_map_doc_new)
layers = arcpy.mapping.ListLayers(mxd_new)
print '\n' + r'Data sources of layers'
for layer in layers:
    if layer.supports("dataSource"):
        print layer.dataSource
# some layers might not support the property "dataSource"
print '\n' + r'Names of layers'
for layer in layers:
    desc = arcpy.Describe(layer)
    print desc.nameString








#mxd_base = arcpy.mapping.MapDocument(r'\\U:\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\Upper_Yaquina_TMDL_BC_Automated_V2.mxd')



