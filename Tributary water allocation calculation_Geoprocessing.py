import arcpy
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
out_accumulation_raster = arcpy.sa.FlowAccumulation(
    in_flow_direction_raster="FlowDir_Fill6",
    in_weight_raster=None,
    data_type="FLOAT",
    flow_direction_type="D8"
)
out_accumulation_raster.save("FlowAcc_Flow6")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
out_surface_raster = arcpy.sa.Fill(
    in_surface_raster="dem_mstrburn6",
    z_limit=None
)
out_surface_raster.save("Fill_dem_mst6")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
out_flow_direction_raster = arcpy.sa.FlowDirection(
    in_surface_raster="Fill_dem_mst6",
    force_flow="FORCE",
    out_drop_raster=None,
    flow_direction_type="D8"
)
out_flow_direction_raster.save("FlowDir_Fill6")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
output_raster = arcpy.sa.RasterCalculator(
    expression='Con(IsNull( "modelstr_raster"), "dem_tribburn5", "dem_tribburn5"-1000)'
)
output_raster.save("dem_mstrburn6")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
out_surface_raster = arcpy.sa.Fill(
    in_surface_raster="doubleburn_calculated1",
    z_limit=None
)
out_surface_raster.save("Fill_doubleburn5")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
output_raster = arcpy.sa.RasterCalculator(
    expression='Con(IsNull( "Modeled_Streamflow_edited"), "tributary_edited_calculated1", "tributary_edited_calculated1"-1000)'
)
output_raster.save("doubleburn_calculated1")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
output_raster = arcpy.sa.RasterCalculator(
    expression='Con(IsNull( "WQSt_raster2"), "Wall_calcualted", "Wall_calcualted"-500)'
)
output_raster.save("tributary_edited_calculated1")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
output_raster = arcpy.sa.RasterCalculator(
    expression='Con(IsNull( "WallRaster_WRIA1"), "FlowDirection_Fill1", "FlowDirection_Fill1"+500)'
)
output_raster.save("Wall_calcualted")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
out_raster = arcpy.sa.Watershed(
    in_flow_direction_raster="FlowDir_Fill6",
    in_pour_point_data="SnapPou_nodes10",
    pour_point_field="Value"
)
out_raster.save("Watersh_Flow10")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
out_raster = arcpy.sa.SnapPourPoint(
    in_pour_point_data="wria1_337_moved_20250221",
    in_accumulation_raster="FlowAcc_Flow6",
    snap_distance=30,
    pour_point_field="OBJECTID"
)
out_raster.save("SnapPou_nodes10")
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.XYTableToPoint(
    in_table="Location_ID_dictionary.csv",
    out_feature_class="Location_ID_dictionary_XYTableToPoint",
    x_field="Calculated_Longitude_Decimal_Degrees_NAD83HARN",
    y_field="Calculated_Latitude_Decimal_Degrees_NAD83HARN",
    z_field=None,
    coordinate_system='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision'
)
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
out_raster = arcpy.sa.SnapPourPoint(
    in_pour_point_data="Location_ID_dictionary_XYTableToPoint",
    in_accumulation_raster="FlowAcc_Flow6",
    snap_distance=30,
    pour_point_field="Location_ID_Num"
)
out_raster.save("SnapPou_AllLocationID_noMoves")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
out_raster = arcpy.sa.Watershed(
    in_flow_direction_raster="FlowDir_Fill6",
    in_pour_point_data="SnapPou_AllLocationID_noMoves",
    pour_point_field="Value"
)
out_raster.save("Watersh_LocationID_noMoves")
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.ExportFeatures(
    in_features="Location_ID_dictionary_XYTableToPoint",
    out_features="Location_ID_dictionary_edit",
    where_clause="",
    use_field_alias_as_name="NOT_USE_ALIAS",
    field_mapping='Location_ID_Num "Location_ID_Num" true true false 4 Long 0 0,First,#,Location_ID_dictionary_XYTableToPoint,Location_ID_Num,-1,-1;Location_ID "Location_ID" true true false 8000 Text 0 0,First,#,Location_ID_dictionary_XYTableToPoint,Location_ID,0,8000;Calculated_Latitude_Decimal_Degrees_NAD83HARN "Calculated_Latitude_Decimal_Degrees_NAD83HARN" true true false 8 Double 0 0,First,#,Location_ID_dictionary_XYTableToPoint,Calculated_Latitude_Decimal_Degrees_NAD83HARN,-1,-1;Calculated_Longitude_Decimal_Degrees_NAD83HARN "Calculated_Longitude_Decimal_Degrees_NAD83HARN" true true false 8 Double 0 0,First,#,Location_ID_dictionary_XYTableToPoint,Calculated_Longitude_Decimal_Degrees_NAD83HARN,-1,-1',
    sort_field=None
)
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
out_raster = arcpy.sa.Watershed(
    in_flow_direction_raster="FlowDir_Fill6",
    in_pour_point_data="SnapPou_LocationID_dictionary_edit",
    pour_point_field="Value"
)
out_raster.save("Watersh_LocationID_dictionary_edit")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
out_raster = arcpy.sa.SnapPourPoint(
    in_pour_point_data="Location_ID_dictionary_edit",
    in_accumulation_raster="FlowAcc_Flow6",
    snap_distance=30,
    pour_point_field="Location_ID_Num"
)
out_raster.save("SnapPou_LocationID_dictionary_edit")
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.AddJoin(
    in_layer_or_view="Location_ID_dictionary_edit",
    in_field="Location_ID_Num",
    join_table="Watersh_LocationID_dictionary_edit",
    join_field="Value",
    join_type="KEEP_ALL",
    index_join_fields="NO_INDEX_JOIN_FIELDS"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="Location_ID_dictionary_edit",
    selection_type="NEW_SELECTION",
    where_clause="VAT_Watersh_LocationID_dictionary_edit.Value IS NULL",
    invert_where_clause=None
)
# different Location_ID labeled sampling points may be close enough that share a same snap point (30 * 30). Only one point can be captured by Snap Pour Point at a time.
# The following process checks and makes sure all sampling points are captured.

arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.ExportFeatures(
    in_features="Location_ID_dictionary_edit",
    out_features="Location_ID_dictionary_missing1",
    where_clause="",
    use_field_alias_as_name="NOT_USE_ALIAS",
    field_mapping='Location_ID_Num "Location_ID_Num" true true false 4 Long 0 0,First,#,Location_ID_dictionary_edit,Location_ID_dictionary_edit.Location_ID_Num,-1,-1;Location_ID "Location_ID" true true false 8000 Text 0 0,First,#,Location_ID_dictionary_edit,Location_ID_dictionary_edit.Location_ID,0,8000;Calculated_Latitude_Decimal_Degrees_NAD83HARN "Calculated_Latitude_Decimal_Degrees_NAD83HARN" true true false 8 Double 0 0,First,#,Location_ID_dictionary_edit,Location_ID_dictionary_edit.Calculated_Latitude_Decimal_Degrees_NAD83HARN,-1,-1;Calculated_Longitude_Decimal_Degrees_NAD83HARN "Calculated_Longitude_Decimal_Degrees_NAD83HARN" true true false 8 Double 0 0,First,#,Location_ID_dictionary_edit,Location_ID_dictionary_edit.Calculated_Longitude_Decimal_Degrees_NAD83HARN,-1,-1;revise "revise" true true false 8 Double 0 0,First,#,Location_ID_dictionary_edit,Location_ID_dictionary_edit.revise,-1,-1;checked "checked" true true false 8 Double 0 0,First,#,Location_ID_dictionary_edit,Location_ID_dictionary_edit.checked,-1,-1;OBJECTID "OBJECTID" false true false 4 Long 0 9,First,#,Location_ID_dictionary_edit,VAT_Watersh_LocationID_dictionary_edit.OBJECTID,-1,-1;Value "Value" false true false 4 Long 0 0,First,#,Location_ID_dictionary_edit,VAT_Watersh_LocationID_dictionary_edit.Value,-1,-1;Count "Count" false true false 8 Double 0 0,First,#,Location_ID_dictionary_edit,VAT_Watersh_LocationID_dictionary_edit.Count,-1,-1',
    sort_field=None
)
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
out_raster = arcpy.sa.SnapPourPoint(
    in_pour_point_data="Location_ID_dictionary_missing1",
    in_accumulation_raster="FlowAcc_Flow6",
    snap_distance=30,
    pour_point_field="Location_ID_Num"
)
out_raster.save("SnapPou_LocationID_dictionary_missing1")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
out_raster = arcpy.sa.Watershed(
    in_flow_direction_raster="FlowDir_Fill6",
    in_pour_point_data="SnapPou_LocationID_dictionary_missing1",
    pour_point_field="Value"
)
out_raster.save("Watersh_LocationID_dictionary_missing1")
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.AddJoin(
    in_layer_or_view="Location_ID_dictionary_missing1",
    in_field="Location_ID_Num",
    join_table="Watersh_LocationID_dictionary_missing1",
    join_field="Value",
    join_type="KEEP_COMMON",
    index_join_fields="NO_INDEX_JOIN_FIELDS"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="Location_ID_dictionary_edit",
    selection_type="NEW_SELECTION",
    where_clause="VAT_Watersh_LocationID_dictionary_edit.Value IS NULL",
    invert_where_clause=None
)
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.ExportFeatures(
    in_features="Location_ID_dictionary_missing1",
    out_features="Location_ID_dictionary_missing2",
    where_clause="",
    use_field_alias_as_name="NOT_USE_ALIAS",
    field_mapping='Location_ID_Num "Location_ID_Num" true true false 4 Long 0 0,First,#,Location_ID_dictionary_missing1,Location_ID_dictionary_missing1.Location_ID_Num,-1,-1;Location_ID "Location_ID" true true false 8000 Text 0 0,First,#,Location_ID_dictionary_missing1,Location_ID_dictionary_missing1.Location_ID,0,8000;Calculated_Latitude_Decimal_Degrees_NAD83HARN "Calculated_Latitude_Decimal_Degrees_NAD83HARN" true true false 8 Double 0 0,First,#,Location_ID_dictionary_missing1,Location_ID_dictionary_missing1.Calculated_Latitude_Decimal_Degrees_NAD83HARN,-1,-1;Calculated_Longitude_Decimal_Degrees_NAD83HARN "Calculated_Longitude_Decimal_Degrees_NAD83HARN" true true false 8 Double 0 0,First,#,Location_ID_dictionary_missing1,Location_ID_dictionary_missing1.Calculated_Longitude_Decimal_Degrees_NAD83HARN,-1,-1;revise "revise" true true false 8 Double 0 0,First,#,Location_ID_dictionary_missing1,Location_ID_dictionary_missing1.revise,-1,-1;checked "checked" true true false 8 Double 0 0,First,#,Location_ID_dictionary_missing1,Location_ID_dictionary_missing1.checked,-1,-1;OBJECTID "OBJECTID" false true false 4 Long 0 9,First,#,Location_ID_dictionary_missing1,VAT_Watersh_LocationID_dictionary_missing1.OBJECTID,-1,-1;Value "Value" false true false 4 Long 0 0,First,#,Location_ID_dictionary_missing1,VAT_Watersh_LocationID_dictionary_missing1.Value,-1,-1;Count "Count" false true false 8 Double 0 0,First,#,Location_ID_dictionary_missing1,VAT_Watersh_LocationID_dictionary_missing1.Count,-1,-1',
    sort_field=None
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="Location_ID_dictionary_missing1",
    selection_type="NEW_SELECTION",
    where_clause="VAT_Watersh_LocationID_dictionary_missing1.Value IS NULL",
    invert_where_clause=None
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.AddJoin(
    in_layer_or_view="Location_ID_dictionary_missing1",
    in_field="Location_ID_Num",
    join_table="Watersh_LocationID_dictionary_missing1",
    join_field="Value",
    join_type="KEEP_ALL",
    index_join_fields="NO_INDEX_JOIN_FIELDS"
)
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.ExportFeatures(
    in_features="Location_ID_dictionary_edit",
    out_features="Location_ID_dictionary_missing1",
    where_clause="",
    use_field_alias_as_name="NOT_USE_ALIAS",
    field_mapping='Location_ID_Num "Location_ID_Num" true true false 4 Long 0 0,First,#,Location_ID_dictionary_edit,Location_ID_dictionary_edit.Location_ID_Num,-1,-1;Location_ID "Location_ID" true true false 8000 Text 0 0,First,#,Location_ID_dictionary_edit,Location_ID_dictionary_edit.Location_ID,0,8000;Calculated_Latitude_Decimal_Degrees_NAD83HARN "Calculated_Latitude_Decimal_Degrees_NAD83HARN" true true false 8 Double 0 0,First,#,Location_ID_dictionary_edit,Location_ID_dictionary_edit.Calculated_Latitude_Decimal_Degrees_NAD83HARN,-1,-1;Calculated_Longitude_Decimal_Degrees_NAD83HARN "Calculated_Longitude_Decimal_Degrees_NAD83HARN" true true false 8 Double 0 0,First,#,Location_ID_dictionary_edit,Location_ID_dictionary_edit.Calculated_Longitude_Decimal_Degrees_NAD83HARN,-1,-1;revise "revise" true true false 8 Double 0 0,First,#,Location_ID_dictionary_edit,Location_ID_dictionary_edit.revise,-1,-1;checked "checked" true true false 8 Double 0 0,First,#,Location_ID_dictionary_edit,Location_ID_dictionary_edit.checked,-1,-1;OBJECTID "OBJECTID" false true false 4 Long 0 9,First,#,Location_ID_dictionary_edit,VAT_Watersh_LocationID_dictionary_edit.OBJECTID,-1,-1;Value "Value" false true false 4 Long 0 0,First,#,Location_ID_dictionary_edit,VAT_Watersh_LocationID_dictionary_edit.Value,-1,-1;Count "Count" false true false 8 Double 0 0,First,#,Location_ID_dictionary_edit,VAT_Watersh_LocationID_dictionary_edit.Count,-1,-1',
    sort_field=None
)
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
out_raster = arcpy.sa.SnapPourPoint(
    in_pour_point_data="Location_ID_dictionary_missing2",
    in_accumulation_raster="FlowAcc_Flow6",
    snap_distance=30,
    pour_point_field="Location_ID_Num"
)
out_raster.save("SnapPou_LocaionID_dictionary_missing2")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
out_raster = arcpy.sa.Watershed(
    in_flow_direction_raster="FlowDir_Fill6",
    in_pour_point_data="SnapPou_LocaionID_dictionary_missing2",
    pour_point_field="Value"
)
out_raster.save("Watersh_LocationID_dictionary_missing2")
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.AddJoin(
    in_layer_or_view="Location_ID_dictionary_missing2",
    in_field="Location_ID_Num",
    join_table="Watersh_LocationID_dictionary_missing2",
    join_field="Value",
    join_type="KEEP_ALL",
    index_join_fields="NO_INDEX_JOIN_FIELDS"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="Location_ID_dictionary_missing2",
    selection_type="NEW_SELECTION",
    where_clause="VAT_Watersh_LocationID_dictionary_missing2.Value IS NULL",
    invert_where_clause=None
)
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.ExportFeatures(
    in_features="Location_ID_dictionary_missing2",
    out_features="Location_ID_dictionary_missing3",
    where_clause="",
    use_field_alias_as_name="NOT_USE_ALIAS",
    field_mapping='Location_ID_Num "Location_ID_Num" true true false 4 Long 0 0,First,#,Location_ID_dictionary_missing2,Location_ID_dictionary_missing2.Location_ID_Num,-1,-1;Location_ID "Location_ID" true true false 8000 Text 0 0,First,#,Location_ID_dictionary_missing2,Location_ID_dictionary_missing2.Location_ID,0,8000;Calculated_Latitude_Decimal_Degrees_NAD83HARN "Calculated_Latitude_Decimal_Degrees_NAD83HARN" true true false 8 Double 0 0,First,#,Location_ID_dictionary_missing2,Location_ID_dictionary_missing2.Calculated_Latitude_Decimal_Degrees_NAD83HARN,-1,-1;Calculated_Longitude_Decimal_Degrees_NAD83HARN "Calculated_Longitude_Decimal_Degrees_NAD83HARN" true true false 8 Double 0 0,First,#,Location_ID_dictionary_missing2,Location_ID_dictionary_missing2.Calculated_Longitude_Decimal_Degrees_NAD83HARN,-1,-1;revise "revise" true true false 8 Double 0 0,First,#,Location_ID_dictionary_missing2,Location_ID_dictionary_missing2.revise,-1,-1;checked "checked" true true false 8 Double 0 0,First,#,Location_ID_dictionary_missing2,Location_ID_dictionary_missing2.checked,-1,-1;OBJECTID "OBJECTID" false true false 4 Long 0 9,First,#,Location_ID_dictionary_missing2,VAT_Watersh_LocationID_dictionary_missing2.OBJECTID,-1,-1;Value "Value" false true false 4 Long 0 0,First,#,Location_ID_dictionary_missing2,VAT_Watersh_LocationID_dictionary_missing2.Value,-1,-1;Count "Count" false true false 8 Double 0 0,First,#,Location_ID_dictionary_missing2,VAT_Watersh_LocationID_dictionary_missing2.Count,-1,-1',
    sort_field=None
)
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
out_raster = arcpy.sa.SnapPourPoint(
    in_pour_point_data="Location_ID_dictionary_missing3",
    in_accumulation_raster="FlowAcc_Flow6",
    snap_distance=30,
    pour_point_field="Location_ID_Num"
)
out_raster.save("SnapPou_LocationID_dictionary_missing3")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
out_raster = arcpy.sa.Watershed(
    in_flow_direction_raster="FlowDir_Fill6",
    in_pour_point_data="SnapPou_LocationID_dictionary_missing3",
    pour_point_field="Value"
)
out_raster.save("Watersh_LocationID_dictionary_missing3")
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.AddJoin(
    in_layer_or_view="Location_ID_dictionary_missing3",
    in_field="Location_ID_Num",
    join_table="Watersh_LocationID_dictionary_missing3",
    join_field="Value",
    join_type="KEEP_ALL",
    index_join_fields="NO_INDEX_JOIN_FIELDS"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="Location_ID_dictionary_missing3",
    selection_type="NEW_SELECTION",
    where_clause="VAT_Watersh_LocationID_dictionary_missing3.Value IS NULL",
    invert_where_clause=None
)
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.ExportFeatures(
    in_features="Location_ID_dictionary_missing3",
    out_features="Location_ID_dictionary_missing4",
    where_clause="",
    use_field_alias_as_name="NOT_USE_ALIAS",
    field_mapping='Location_ID_Num "Location_ID_Num" true true false 4 Long 0 0,First,#,Location_ID_dictionary_missing3,Location_ID_dictionary_missing3.Location_ID_Num,-1,-1;Location_ID "Location_ID" true true false 8000 Text 0 0,First,#,Location_ID_dictionary_missing3,Location_ID_dictionary_missing3.Location_ID,0,8000;Calculated_Latitude_Decimal_Degrees_NAD83HARN "Calculated_Latitude_Decimal_Degrees_NAD83HARN" true true false 8 Double 0 0,First,#,Location_ID_dictionary_missing3,Location_ID_dictionary_missing3.Calculated_Latitude_Decimal_Degrees_NAD83HARN,-1,-1;Calculated_Longitude_Decimal_Degrees_NAD83HARN "Calculated_Longitude_Decimal_Degrees_NAD83HARN" true true false 8 Double 0 0,First,#,Location_ID_dictionary_missing3,Location_ID_dictionary_missing3.Calculated_Longitude_Decimal_Degrees_NAD83HARN,-1,-1;revise "revise" true true false 8 Double 0 0,First,#,Location_ID_dictionary_missing3,Location_ID_dictionary_missing3.revise,-1,-1;checked "checked" true true false 8 Double 0 0,First,#,Location_ID_dictionary_missing3,Location_ID_dictionary_missing3.checked,-1,-1;OBJECTID "OBJECTID" false true false 4 Long 0 9,First,#,Location_ID_dictionary_missing3,VAT_Watersh_LocationID_dictionary_missing3.OBJECTID,-1,-1;Value "Value" false true false 4 Long 0 0,First,#,Location_ID_dictionary_missing3,VAT_Watersh_LocationID_dictionary_missing3.Value,-1,-1;Count "Count" false true false 8 Double 0 0,First,#,Location_ID_dictionary_missing3,VAT_Watersh_LocationID_dictionary_missing3.Count,-1,-1',
    sort_field=None
)
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
out_raster = arcpy.sa.SnapPourPoint(
    in_pour_point_data="Location_ID_dictionary_missing4",
    in_accumulation_raster="FlowAcc_Flow6",
    snap_distance=30,
    pour_point_field="Location_ID_Num"
)
out_raster.save("SnapPou_LocationID_dictionary_missing4")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
out_raster = arcpy.sa.Watershed(
    in_flow_direction_raster="FlowDir_Fill6",
    in_pour_point_data="SnapPou_LocationID_dictionary_missing4",
    pour_point_field="Value"
)
out_raster.save("Watersh_LocationID_dictionary_missing4")
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.ExportFeatures(
    in_features="Location_ID_dictionary_missing4",
    out_features="Location_ID_dictionary_missing5",
    where_clause="",
    use_field_alias_as_name="NOT_USE_ALIAS",
    field_mapping='Location_ID_Num "Location_ID_Num" true true false 4 Long 0 0,First,#,Location_ID_dictionary_missing4,Location_ID_Num,-1,-1;Location_ID "Location_ID" true true false 8000 Text 0 0,First,#,Location_ID_dictionary_missing4,Location_ID,0,8000;Calculated_Latitude_Decimal_Degrees_NAD83HARN "Calculated_Latitude_Decimal_Degrees_NAD83HARN" true true false 8 Double 0 0,First,#,Location_ID_dictionary_missing4,Calculated_Latitude_Decimal_Degrees_NAD83HARN,-1,-1;Calculated_Longitude_Decimal_Degrees_NAD83HARN "Calculated_Longitude_Decimal_Degrees_NAD83HARN" true true false 8 Double 0 0,First,#,Location_ID_dictionary_missing4,Calculated_Longitude_Decimal_Degrees_NAD83HARN,-1,-1;revise "revise" true true false 8 Double 0 0,First,#,Location_ID_dictionary_missing4,revise,-1,-1;checked "checked" true true false 8 Double 0 0,First,#,Location_ID_dictionary_missing4,checked,-1,-1',
    sort_field=None
)
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
out_raster = arcpy.sa.SnapPourPoint(
    in_pour_point_data="Location_ID_dictionary_missing5",
    in_accumulation_raster="FlowAcc_Flow6",
    snap_distance=30,
    pour_point_field="Location_ID_Num"
)
out_raster.save("SnapPou_LocationID_dictionary_missing5")
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
with arcpy.EnvManager(outputZFlag="Disabled", outputMFlag="Disabled"):
    arcpy.conversion.RasterToPoint(
        in_raster="SnapPou_LocationID_dictionary_edit",
        out_point_features="RasterToPoint_dictionary_edit",
        raster_field="Value"
    )
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
with arcpy.EnvManager(outputZFlag="Disabled", outputMFlag="Disabled"):
    arcpy.conversion.RasterToPoint(
        in_raster="SnapPou_LocationID_dictionary_missing1",
        out_point_features="RasterToPoint_dictionary_missing1",
        raster_field="Value"
    )
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
with arcpy.EnvManager(outputZFlag="Disabled", outputMFlag="Disabled"):
    arcpy.conversion.RasterToPoint(
        in_raster="SnapPou_LocaionID_dictionary_missing2",
        out_point_features="RasterToPoint_dictionary_missing2",
        raster_field="Value"
    )
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
with arcpy.EnvManager(outputZFlag="Disabled", outputMFlag="Disabled"):
    arcpy.conversion.RasterToPoint(
        in_raster="SnapPou_LocationID_dictionary_missing4",
        out_point_features="RasterToPoint_dictionary_missing4",
        raster_field="Value"
    )
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
with arcpy.EnvManager(outputZFlag="Disabled", outputMFlag="Disabled"):
    arcpy.conversion.RasterToPoint(
        in_raster="SnapPou_LocationID_dictionary_missing3",
        out_point_features="RasterToPoint_dictionary_missing3",
        raster_field="Value"
    )
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
with arcpy.EnvManager(outputZFlag="Disabled", outputMFlag="Disabled"):
    arcpy.conversion.RasterToPoint(
        in_raster="SnapPou_LocationID_dictionary_missing5",
        out_point_features="RasterToPoint_dictionary_missing5",
        raster_field="Value"
    )
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.Merge(
    inputs="RasterToPoint_dictionary_edit;RasterToPoint_dictionary_missing1;RasterToPoint_dictionary_missing2;RasterToPoint_dictionary_missing3;RasterToPoint_dictionary_missing4;RasterToPoint_dictionary_missing5",
    output="RasterToPoint_dictionary_Merge",
    field_mappings='pointid "pointid" true true false 4 Long 0 0,First,#,RasterToPoint_dictionary_edit,pointid,-1,-1,RasterToPoint_dictionary_missing1,pointid,-1,-1,RasterToPoint_dictionary_missing2,pointid,-1,-1,RasterToPoint_dictionary_missing3,pointid,-1,-1,RasterToPoint_dictionary_missing4,pointid,-1,-1,RasterToPoint_dictionary_missing5,pointid,-1,-1;grid_code "grid_code" true true false 4 Long 0 0,First,#,RasterToPoint_dictionary_edit,grid_code,-1,-1,RasterToPoint_dictionary_missing1,grid_code,-1,-1,RasterToPoint_dictionary_missing2,grid_code,-1,-1,RasterToPoint_dictionary_missing3,grid_code,-1,-1,RasterToPoint_dictionary_missing4,grid_code,-1,-1,RasterToPoint_dictionary_missing5,grid_code,-1,-1',
    add_source="NO_SOURCE_INFO"
)
# /
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
arcpy.sa.ExtractValuesToPoints(
    in_point_features="RasterToPoint_dictionary_Merge",
    in_raster="FlowAcc_Flow6",
    out_point_features="ExtractValues_FlowAccu_points",
    interpolate_values="NONE",
    add_attributes="VALUE_ONLY"
)
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
arcpy.sa.ExtractValuesToPoints(
    in_point_features="ExtractValues_FlowAccu_points",
    in_raster="Watersh_Flow10",
    out_point_features="ExtractValues_FlowAccu_points1",
    interpolate_values="NONE",
    add_attributes="VALUE_ONLY"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="ExtractValues_FlowAccu_points1",
    selection_type="NEW_SELECTION",
    where_clause="UpstreamNode IS NULL",
    invert_where_clause=None
)
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
arcpy.sa.ExtractValuesToPoints(
    in_point_features="wria1_337_moved_20250221",
    in_raster="FlowAcc_Flow6",
    out_point_features="ExtractValues_FlowAccu_337nodes",
    interpolate_values="NONE",
    add_attributes="VALUE_ONLY"
)
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
with arcpy.EnvManager(outputZFlag="Disabled", outputMFlag="Disabled"):
    arcpy.conversion.RasterToPoint(
        in_raster="SnapPou_nodes10",
        out_point_features="RasterToPoint_SnapPou_337nodes",
        raster_field="Value"
    )
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
arcpy.sa.ExtractValuesToPoints(
    in_point_features="RasterToPoint_SnapPou_337nodes",
    in_raster="FlowAcc_Flow6",
    out_point_features="ExtractValues_FlowAccu_337nodes",
    interpolate_values="NONE",
    add_attributes="VALUE_ONLY"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.AddJoin(
    in_layer_or_view="ExtractValues_FlowAccu_points1",
    in_field="UpstreamNode",
    join_table="ExtractValues_FlowAccu_337nodes",
    join_field="OBJECTID_Nodes",
    join_type="KEEP_ALL",
    index_join_fields="NO_INDEX_JOIN_FIELDS"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="ExtractValues_FlowAccu_points1",
    selection_type="NEW_SELECTION",
    where_clause="UpstreamNode IS NULL",
    invert_where_clause=None
)
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.ExportFeatures(
    in_features="ExtractValues_FlowAccu_points1",
    out_features="ExtractValues_LocationID_Nodes_join",
    where_clause="",
    use_field_alias_as_name="NOT_USE_ALIAS",
    field_mapping='pointid "pointid" true true false 4 Long 0 0,First,#,ExtractValues_FlowAccu_points1,ExtractValues_FlowAccu_points1.pointid,-1,-1;grid_code "grid_code" true true false 4 Long 0 0,First,#,ExtractValues_FlowAccu_points1,ExtractValues_FlowAccu_points1.grid_code,-1,-1;FlowAccuArea "RASTERVALU" true true false 4 Float 0 0,First,#,ExtractValues_FlowAccu_points1,ExtractValues_FlowAccu_points1.FlowAccuArea,-1,-1;UpstreamNode "RASTERVALU" true true false 4 Long 0 0,First,#,ExtractValues_FlowAccu_points1,ExtractValues_FlowAccu_points1.UpstreamNode,-1,-1;OBJECTID "OBJECTID" false true false 4 Long 0 9,First,#,ExtractValues_FlowAccu_points1,ExtractValues_FlowAccu_337nodes.OBJECTID,-1,-1;pointid "pointid" true true false 4 Long 0 0,First,#,ExtractValues_FlowAccu_points1,ExtractValues_FlowAccu_337nodes.pointid,-1,-1;OBJECTID_Nodes "grid_code" true true false 4 Long 0 0,First,#,ExtractValues_FlowAccu_points1,ExtractValues_FlowAccu_337nodes.OBJECTID_Nodes,-1,-1;FlowAccuArea_Nodes "RASTERVALU" true true false 4 Float 0 0,First,#,ExtractValues_FlowAccu_points1,ExtractValues_FlowAccu_337nodes.FlowAccuArea_Nodes,-1,-1',
    sort_field=None
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.CalculateField(
    in_table="ExtractValues_LocationID_Nodes_join",
    field="FlowRatio",
    expression="!FlowAccuArea! / !FlowAccuArea_Nodes!",
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.AddJoin(
    in_layer_or_view="ExtractValues_LocationID_Nodes_join",
    in_field="grid_code",
    join_table="Location_ID_dictionary_edit",
    join_field="Location_ID_dictionary_edit.Location_ID_Num",
    join_type="KEEP_ALL",
    index_join_fields="NO_INDEX_JOIN_FIELDS"
)
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.ExportFeatures(
    in_features="ExtractValues_LocationID_Nodes_join",
    out_features="ExtractValues_LocationID_Nodes_join1",
    where_clause="",
    use_field_alias_as_name="NOT_USE_ALIAS",
    field_mapping='pointid "pointid" true true false 4 Long 0 0,First,#,ExtractValues_LocationID_Nodes_join,ExtractValues_LocationID_Nodes_join.pointid,-1,-1;grid_code "grid_code" true true false 4 Long 0 0,First,#,ExtractValues_LocationID_Nodes_join,ExtractValues_LocationID_Nodes_join.grid_code,-1,-1;FlowAccuArea "RASTERVALU" true true false 4 Float 0 0,First,#,ExtractValues_LocationID_Nodes_join,ExtractValues_LocationID_Nodes_join.FlowAccuArea,-1,-1;UpstreamNode "RASTERVALU" true true false 4 Long 0 0,First,#,ExtractValues_LocationID_Nodes_join,ExtractValues_LocationID_Nodes_join.UpstreamNode,-1,-1;OBJECTID "OBJECTID" true true false 4 Long 0 0,First,#,ExtractValues_LocationID_Nodes_join,ExtractValues_LocationID_Nodes_join.OBJECTID,-1,-1;pointid_1 "pointid" true true false 4 Long 0 0,First,#,ExtractValues_LocationID_Nodes_join,ExtractValues_LocationID_Nodes_join.pointid_1,-1,-1;OBJECTID_Nodes "grid_code" true true false 4 Long 0 0,First,#,ExtractValues_LocationID_Nodes_join,ExtractValues_LocationID_Nodes_join.OBJECTID_Nodes,-1,-1;FlowAccuArea_Nodes "RASTERVALU" true true false 4 Float 0 0,First,#,ExtractValues_LocationID_Nodes_join,ExtractValues_LocationID_Nodes_join.FlowAccuArea_Nodes,-1,-1;FlowRatio "FlowRatio" true true false 4 Float 0 0,First,#,ExtractValues_LocationID_Nodes_join,ExtractValues_LocationID_Nodes_join.FlowRatio,-1,-1;OBJECTID "OBJECTID" false true false 4 Long 0 9,First,#,ExtractValues_LocationID_Nodes_join,Location_ID_dictionary_edit.OBJECTID,-1,-1;Location_ID_Num "Location_ID_Num" true true false 4 Long 0 0,First,#,ExtractValues_LocationID_Nodes_join,Location_ID_dictionary_edit.Location_ID_Num,-1,-1;Location_ID "Location_ID" true true false 8000 Text 0 0,First,#,ExtractValues_LocationID_Nodes_join,Location_ID_dictionary_edit.Location_ID,0,8000;Calculated_Latitude_Decimal_Degrees_NAD83HARN "Calculated_Latitude_Decimal_Degrees_NAD83HARN" true true false 8 Double 0 0,First,#,ExtractValues_LocationID_Nodes_join,Location_ID_dictionary_edit.Calculated_Latitude_Decimal_Degrees_NAD83HARN,-1,-1;Calculated_Longitude_Decimal_Degrees_NAD83HARN "Calculated_Longitude_Decimal_Degrees_NAD83HARN" true true false 8 Double 0 0,First,#,ExtractValues_LocationID_Nodes_join,Location_ID_dictionary_edit.Calculated_Longitude_Decimal_Degrees_NAD83HARN,-1,-1;revise "revise" true true false 8 Double 0 0,First,#,ExtractValues_LocationID_Nodes_join,Location_ID_dictionary_edit.revise,-1,-1;checked "checked" true true false 8 Double 0 0,First,#,ExtractValues_LocationID_Nodes_join,Location_ID_dictionary_edit.checked,-1,-1;OBJECTID "OBJECTID" false true false 4 Long 0 9,First,#,ExtractValues_LocationID_Nodes_join,VAT_Watersh_LocationID_dictionary_edit.OBJECTID,-1,-1;Value "Value" true true false 4 Long 0 0,First,#,ExtractValues_LocationID_Nodes_join,VAT_Watersh_LocationID_dictionary_edit.Value,-1,-1;Count "Count" true true false 8 Double 0 0,First,#,ExtractValues_LocationID_Nodes_join,VAT_Watersh_LocationID_dictionary_edit.Count,-1,-1',
    sort_field=None
)
arcpy.ImportToolbox(r"@\Analysis Tools.tbx")
arcpy.analysis.SpatialJoin(
    target_features="ExtractValues_LocationID_Nodes_join1",
    join_features="WRIA_1_Drainages",
    out_feature_class="ExtractValues_LocationID_Nodes_join2",
    join_operation="JOIN_ONE_TO_ONE",
    join_type="KEEP_ALL",
    field_mapping='pointid "pointid" true true false 4 Long 0 0,First,#,ExtractValues_LocationID_Nodes_join1,pointid,-1,-1;grid_code "grid_code" true true false 4 Long 0 0,First,#,ExtractValues_LocationID_Nodes_join1,grid_code,-1,-1;FlowAccuArea "RASTERVALU" true true false 4 Float 0 0,First,#,ExtractValues_LocationID_Nodes_join1,FlowAccuArea,-1,-1;UpstreamNode "RASTERVALU" true true false 4 Long 0 0,First,#,ExtractValues_LocationID_Nodes_join1,UpstreamNode,-1,-1;OBJECTID "OBJECTID" true true false 4 Long 0 0,First,#,ExtractValues_LocationID_Nodes_join1,OBJECTID,-1,-1;pointid_1 "pointid" true true false 4 Long 0 0,First,#,ExtractValues_LocationID_Nodes_join1,pointid_1,-1,-1;OBJECTID_Nodes "grid_code" true true false 4 Long 0 0,First,#,ExtractValues_LocationID_Nodes_join1,OBJECTID_Nodes,-1,-1;FlowAccuArea_Nodes "RASTERVALU" true true false 4 Float 0 0,First,#,ExtractValues_LocationID_Nodes_join1,FlowAccuArea_Nodes,-1,-1;FlowRatio "FlowRatio" true true false 4 Float 0 0,First,#,ExtractValues_LocationID_Nodes_join1,FlowRatio,-1,-1;OBJECTID_1 "OBJECTID" true true false 4 Long 0 0,First,#,ExtractValues_LocationID_Nodes_join1,OBJECTID_1,-1,-1;Location_ID_Num "Location_ID_Num" true true false 4 Long 0 0,First,#,ExtractValues_LocationID_Nodes_join1,Location_ID_Num,-1,-1;Location_ID "Location_ID" true true false 8000 Text 0 0,First,#,ExtractValues_LocationID_Nodes_join1,Location_ID,0,8000;Calculated_Latitude_Decimal_Degrees_NAD83HARN "Calculated_Latitude_Decimal_Degrees_NAD83HARN" true true false 8 Double 0 0,First,#,ExtractValues_LocationID_Nodes_join1,Calculated_Latitude_Decimal_Degrees_NAD83HARN,-1,-1;Calculated_Longitude_Decimal_Degrees_NAD83HARN "Calculated_Longitude_Decimal_Degrees_NAD83HARN" true true false 8 Double 0 0,First,#,ExtractValues_LocationID_Nodes_join1,Calculated_Longitude_Decimal_Degrees_NAD83HARN,-1,-1;revise "revise" true true false 8 Double 0 0,First,#,ExtractValues_LocationID_Nodes_join1,revise,-1,-1;checked "checked" true true false 8 Double 0 0,First,#,ExtractValues_LocationID_Nodes_join1,checked,-1,-1;OBJECTID_12 "OBJECTID" true true false 4 Long 0 0,First,#,ExtractValues_LocationID_Nodes_join1,OBJECTID_12,-1,-1;Value "Value" true true false 4 Long 0 0,First,#,ExtractValues_LocationID_Nodes_join1,Value,-1,-1;Count "Count" true true false 8 Double 0 0,First,#,ExtractValues_LocationID_Nodes_join1,Count,-1,-1;BSNWRIA1A "BSNWRIA1A" true true false 8 Double 0 0,First,#,WRIA_1_Drainages,BSNWRIA1A,-1,-1;FIRST_ORDE "FIRST_ORDE" true true false 25 Text 0 0,First,#,WRIA_1_Drainages,FIRST_ORDE,0,25;SECOND_ORD "SECOND_ORD" true true false 30 Text 0 0,First,#,WRIA_1_Drainages,SECOND_ORD,0,30;DRAIN_NAME "DRAIN_NAME" true true false 60 Text 0 0,First,#,WRIA_1_Drainages,DRAIN_NAME,0,60;SQ_MILE "SQ_MILE" true true false 8 Double 0 0,First,#,WRIA_1_Drainages,SQ_MILE,-1,-1;MODEL_TYPE "MODEL_TYPE" true true false 16 Text 0 0,First,#,WRIA_1_Drainages,MODEL_TYPE,0,16;Centroid "Centroid" true true false 4 Float 0 0,First,#,WRIA_1_Drainages,Centroid,-1,-1;CentroidY "CentroidY" true true false 4 Float 0 0,First,#,WRIA_1_Drainages,CentroidY,-1,-1;Shape_Length "Shape_Length" false true true 8 Double 0 0,First,#,WRIA_1_Drainages,Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0,First,#,WRIA_1_Drainages,Shape_Area,-1,-1',
    match_option="WITHIN",
    search_radius=None,
    distance_field_name=""
)
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.TableToExcel(
    Input_Table="ExtractValues_LocationID_Nodes_join2",
    Output_Excel_File=r"FlowRatio_library.xls",
    Use_field_alias_as_column_header="NAME",
    Use_domain_and_subtype_description="CODE"
)
