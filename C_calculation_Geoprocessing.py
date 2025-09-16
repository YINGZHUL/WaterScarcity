import arcpy
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="T_processing9672_ExportFeature_TWO",
    selection_type="NEW_SELECTION",
    where_clause="T_requirement = 12",
    invert_where_clause=None
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.CalculateField(
    in_table="T_processing9672_ExportFeature_TWO",
    field="Ccalcualtion",
    expression="(!Result_Value! - !T_requirement!) / !T_requirement!",
    expression_type="PYTHON3",
    code_block="",
    field_type="FLOAT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="T_processing9672_ExportFeature_TWO",
    selection_type="NEW_SELECTION",
    where_clause="T_requirement = 12 And Result_Value < 12",
    invert_where_clause=None
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.CalculateField(
    in_table="T_processing9672_ExportFeature_TWO",
    field="Ccalcualtion",
    expression="0",
    expression_type="PYTHON3",
    code_block="",
    field_type="FLOAT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="T_processing9672_ExportFeature_TWO",
    selection_type="NEW_SELECTION",
    where_clause="TEMPERATURE = '13 º C' And Ccalcualtion IS NULL",
    invert_where_clause=None
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="T_processing9672_ExportFeature_TWO",
    selection_type="NEW_SELECTION",
    where_clause="TEMPERATURE = '13 º C'",
    invert_where_clause=None
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.CalculateField(
    in_table="T_processing9672_ExportFeature_TWO",
    field="T13",
    expression="13",
    expression_type="PYTHON3",
    code_block="",
    field_type="FLOAT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="T_processing9672_ExportFeature_TWO",
    selection_type="NEW_SELECTION",
    where_clause="TEMPERATURE = '13 º C' And Ccalcualtion IS NULL",
    invert_where_clause=None
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.CalculateField(
    in_table="T_processing9672_ExportFeature_TWO",
    field="Ccalcualtion",
    expression="(!Result_Value! - !T13!) / !T13!",
    expression_type="PYTHON3",
    code_block="",
    field_type="FLOAT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="T_processing9672_ExportFeature_TWO",
    selection_type="NEW_SELECTION",
    where_clause="Ccalcualtion < 0",
    invert_where_clause=None
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.CalculateField(
    in_table="T_processing9672_ExportFeature_TWO",
    field="Ccalcualtion",
    expression="0",
    expression_type="PYTHON3",
    code_block="",
    field_type="FLOAT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="T_processing9672_ExportFeature_TWO",
    selection_type="NEW_SELECTION",
    where_clause="T_requirement = 16 And Ccalcualtion IS NULL",
    invert_where_clause=None
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="T_processing9672_ExportFeature_TWO",
    selection_type="NEW_SELECTION",
    where_clause="T13 = 13",
    invert_where_clause=None
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="T_processing9672_ExportFeature_TWO",
    selection_type="NEW_SELECTION",
    where_clause="T_requirement = 16 And Ccalcualtion IS NULL",
    invert_where_clause=None
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.CalculateField(
    in_table="T_processing9672_ExportFeature_TWO",
    field="Ccalcualtion",
    expression="(!Result_Value! - !T_requirement!) / !T_requirement!",
    expression_type="PYTHON3",
    code_block="",
    field_type="FLOAT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="T_processing9672_ExportFeature_TWO",
    selection_type="NEW_SELECTION",
    where_clause="Ccalcualtion < 0",
    invert_where_clause=None
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.CalculateField(
    in_table="T_processing9672_ExportFeature_TWO",
    field="Ccalcualtion",
    expression="0",
    expression_type="PYTHON3",
    code_block="",
    field_type="FLOAT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="T_processing9672_ExportFeature_TWO",
    selection_type="NEW_SELECTION",
    where_clause="T_requirement = 17.5 And Ccalcualtion IS NULL",
    invert_where_clause=None
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.CalculateField(
    in_table="T_processing9672_ExportFeature_TWO",
    field="Ccalcualtion",
    expression="(!Result_Value! - !T_requirement!) / !T_requirement!",
    expression_type="PYTHON3",
    code_block="",
    field_type="FLOAT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="T_processing9672_ExportFeature_TWO",
    selection_type="NEW_SELECTION",
    where_clause="Ccalcualtion < 0",
    invert_where_clause=None
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.CalculateField(
    in_table="T_processing9672_ExportFeature_TWO",
    field="Ccalcualtion",
    expression="0",
    expression_type="PYTHON3",
    code_block="",
    field_type="FLOAT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.TableToExcel(
    Input_Table="T_processing9672_ExportFeature_TWO",
    Output_Excel_File=r"H:\2023_UW\Nippon GeoHealth Project\useful data file\water_scarcity_assessment\T_processing9672_ExportFeature_TWO_TableToExcel.xls",
    Use_field_alias_as_column_header="NAME",
    Use_domain_and_subtype_description="CODE"
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.AddSpatialJoin(
    target_features="T_processing9672_ExportFeature",
    join_features="WQStandards_BeneficialU_ExportFeature",
    join_operation="JOIN_ONE_TO_ONE",
    join_type="KEEP_ALL",
    field_mapping=r'USE_CODE_NR "USE_CODE_NR" true true false 4 Long 0 0,First,#,WQStandards_BeneficialU_ExportFeature,USE_CODE_NR,-1,-1;SUB1_CODE "SUB1_CODE" true true false 4 Long 0 0,First,#,WQStandards_BeneficialU_ExportFeature,SUB1_CODE,-1,-1;SUB2_CODE "SUB2_CODE" true true false 4 Long 0 0,First,#,WQStandards_BeneficialU_ExportFeature,SUB2_CODE,-1,-1;USE_REA "USE_REA" true true false 2 Short 0 0,First,#,WQStandards_BeneficialU_ExportFeature,USE_REA,-1,-1;WC_GNIS_NM "WC_GNIS_NM" true true false 50 Text 0 0,First,#,WQStandards_BeneficialU_ExportFeature,WC_GNIS_NM,0,50;ReachCode "ReachCode" true true false 14 Text 0 0,First,#,WQStandards_BeneficialU_ExportFeature,ReachCode,0,14;FMeasure "FMeasure" true true false 8 Double 0 0,First,#,WQStandards_BeneficialU_ExportFeature,FMeasure,-1,-1;TMeasure "TMeasure" true true false 8 Double 0 0,First,#,WQStandards_BeneficialU_ExportFeature,TMeasure,-1,-1;EventDate "EventDate" true true false 8 Date 0 0,First,#,WQStandards_BeneficialU_ExportFeature,EventDate,-1,-1;AQUATIC "AQUATIC" true true false 50 Text 0 0,First,#,WQStandards_BeneficialU_ExportFeature,AQUATIC,0,50;RECREATION "RECREATION" true true false 50 Text 0 0,First,#,WQStandards_BeneficialU_ExportFeature,RECREATION,0,50;DOMESTIC_WATER "DOMESTIC_WATER" true true false 1 Text 0 0,First,#,WQStandards_BeneficialU_ExportFeature,DOMESTIC_WATER,0,1;Shape_Length "Shape_Length" false true true 8 Double 0 0,First,#,WQStandards_BeneficialU_ExportFeature,Shape_Length,-1,-1;T_requirement "T_requirement" true true false 8 Double 0 0,First,#,WQStandards_BeneficialU_ExportFeature,T_requirement,-1,-1',
    match_option="CLOSEST",
    search_radius=None,
    distance_field_name=""
)
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.AddSpatialJoin(
    target_features="T_processing9672Seperated_Monthly_XYTableToPoint",
    join_features="WQStandards_SuppS_Clip",
    join_operation="JOIN_ONE_TO_ONE",
    join_type="KEEP_ALL",
    field_mapping='WQStandards_SuppS_Clip,USE_CODE_NR,-1,-1;SUB1_CODE "SUB1_CODE" true true false 4 Long 0 0,First,#,WQStandards_SuppS_Clip,SUB1_CODE,-1,-1;SUB2_CODE "SUB2_CODE" true true false 4 Long 0 0,First,#,WQStandards_SuppS_Clip,SUB2_CODE,-1,-1;USE_REA "USE_REA" true true false 2 Short 0 0,First,#,WQStandards_SuppS_Clip,USE_REA,-1,-1;WC_GNIS_NM "WC_GNIS_NM" true true false 50 Text 0 0,First,#,WQStandards_SuppS_Clip,WC_GNIS_NM,0,50;ReachCode "ReachCode" true false false 14 Text 0 0,First,#,WQStandards_SuppS_Clip,ReachCode,0,14;FMeasure "FMeasure" true false false 8 Double 0 0,First,#,WQStandards_SuppS_Clip,FMeasure,-1,-1;TMeasure "TMeasure" true false false 8 Double 0 0,First,#,WQStandards_SuppS_Clip,TMeasure,-1,-1;EventDate "EventDate" true true false 8 Date 0 0,First,#,WQStandards_SuppS_Clip,EventDate,-1,-1;DATES "DATES" true true false 25 Text 0 0,First,#,WQStandards_SuppS_Clip,DATES,0,25;TEMPERATURE "TEMPERATURE" true true false 10 Text 0 0,First,#,WQStandards_SuppS_Clip,TEMPERATURE,0,10;Shape_Length "Shape_Length" false true true 8 Double 0 0,First,#,WQStandards_SuppS_Clip,Shape_Length,-1,-1',
    match_option="WITHIN_A_DISTANCE",
    search_radius="100 Meters",
    distance_field_name=""
)
