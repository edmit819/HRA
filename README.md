#  <p align="center">Welcome to HRA Repository</p>


HRA is a repository that defines TigerGraph Graph database schema for capturing a user Health Risk Assessments.

## Overview
The repository has a specific file structure to support TigerGraph development and deployment of a Graph database schema. If you are wondering what the number in the file name means, it represents which order that script should be loaded into TigerGraph (within that folder).

If you’re not familiar with TigerGraph, you need to load the database with a schema, then load the data for the vertex’s that are defined in the schema, and then load all of the queries.

The data to load into the database is defined in the GraphData directory. The src directory contains python programs to generate the data that gets loaded into TigerGraph database. The app_profile.py file is a Streamlit app that analysis the data generated by the other programs.

## Directory Structure
> DDLs/  
>> Data/  
>>> loadVertexData[1].gsql  

>> Queries/  
>>> calculateBodyMass[2].gsql  
		determineBloodPressure[7].gsql  
    determineCholesterol[6].gsql  
    determineDibetic[4].gsql  
    determineHRA[1].gsql  
    determineRisk[8].gsql  
    determineSmoker[3].gsql  
    determineVaccine[5].gsql  
    initializeGraph.gsql

>>Schema/
 >>>defineSchema.gsql  

>GraphData/
 >>>BodyMass-Index.csv  
 ClinicalProfiles.csv
 PersonProfiles.csv
 Vaccines.csv

>src/  
>>>CreateClinicalProfile.py  
>>>CreateUserProfile.py  
>>>app_profile.py  

## Scripts
>installPythonEnvironment.sh - Bash script to setup python environment  
requirements.txt - File that describes Python dependencies  
runClinicalProfiler.sh - Runs app_profile program to analysis generated data files  
runDataProfiler.sh - Runs the CreateClinicalprofile.py program that generates clinical profiles  
runUserProfiler.sh - Runs the CreateUserProfile.py program that generate a user profile, including first and last name, birthday, age, gender.  
