# WaterScarcity
Supporting materials for the paper 'Integrating aquatic life requirements into water scarcity assessment for coastal watersheds'

The algorithm and software versions used in this study are Python 3.9.13, Excel Version 2508, ArcGIS Pro 3.1.3. Geoprocessing processes conducted in ArcGIS Pro are recorded as Python scripts.

Section 1: Flow analysis:
IFR, A, Q, D calculation: Water flow analysis.py
Tributary flow allocation – construct a method allowing tributaries flow allocation at water quality sampling sites for better capture the pollution source areas: Tributary water allocation calculation_Geoprocessing.py

Section 2: Water quality data
Analyze water quality data monthly and aligning with PFRs: Water quality data treatment.py

Section 3: Water scarcity calculation:
According to spatial variation of aquatic life water quality requirements at stream reach level, the calculation of (C/Cmax-1) is conducted in Arcgis Pro for clear visulization: C_calculation_Geoprocessing.py
WSq calculations for: D4: industrial, D5: domestic, D16: agriculture: WSq_calculation_drainage.xlsx
WSp calculations  at drainage and management area level: WSp_calculation_drainage and managementarea.xlsx
WSp calculations at stream reach level: WSp_calculation_DO_reachcode.xlsx, WSp_calculation_T_reachcode.xlsx, WSp_calculation_Hg_reachcode.xlsx, WSp_calculation_NH3N_reachcode.xlsx
