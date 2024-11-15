# CITI HACKTHON USE CASE : Create a tool for defining FDC3 Context Schemas .



- ✨OPEN AI + FINOS  ✨

## STEPS TO EXECUTE

- Install packages from requirement.txt
- Create python virtual enviornment and activate the enviornment
- Update file path for updatedTypeScriptTypes.json , ContextTypes.ts and destination folder for jsonSchemas
- updatedTypeScriptTypes.json is json file maintains which types to be referred to generate jsonSchemas
- ContextTypes.ts is file which containts ContextTypes 
- destination folder where new jsonSchemas to be generated
- start main.py file using python main.py command

## - [Features]
- This is a JsonSchema generator tool using scheduled job to read updated types from typescipt file and convert into jsonSchema


## Tech



- [Python + openai] - Open AI based tool to read .ts file and generate json schema 


## Pre-requisite
- Python setup required
- Python packages needs to be installed
- Open AI account required as it call api which needs api key

## Notes
- Using AI to generate schemas can be a great starting point, offering speed and consistency.
- However, it should be complemented with human expertise to ensure accuracy and adaptability to specific needs.
