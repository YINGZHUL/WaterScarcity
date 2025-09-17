# WaterScarcity
This repository includes supporting scripts for the paper 'Integrating aquatic life requirements into water scarcity assessment for coastal watersheds'.

The algorithm and software versions used in this study are Python 3.9.13, Excel Version 2508, ArcGIS Pro 3.1.3. Geoprocessing processes conducted in ArcGIS Pro are recorded as Python scripts.

**Section 1: Flow analysis:**
IFR, A, Q, D calculation
Tributary flow allocation – construct a method allowing tributaries flow allocation at water quality sampling sites for better capture the pollution source areas

**Section 2: Water quality data:**
Analyze water quality data monthly and aligning with PFRs

**Section 3: Water scarcity calculation:**
According to spatial variation of aquatic life water quality requirements at stream reach level, the calculation of (C/Cmax-1) is conducted in Arcgis Pro for clear visulization
WSq calculations for: D4: industrial, D5: domestic, D16
WSp calculations  at drainage and management area level
WSp calculations at stream reach level

Input data used in Flow analysis section are available at: http://www.hydroshare.org/resource/d15b9934f34e4c57913b3cb53966d5c7
Input water quality data are derived from: https://ecology.wa.gov/research-data/data-resources/environmental-information-management-database
