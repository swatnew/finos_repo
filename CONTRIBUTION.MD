

# Project owners & Contributor - Swati Ghadge 

# Project consumers -Users who wants to use the tool to generate JSON SCHEMAS Using Open ai

# Useful Info
This is python and open ai based tool . It is a python based scheduler which reads typescript context file and use it to generat json schema for only updated types . We maintain a json look up file which can be used to inform the tool which new json schemas to be created . This information is send to open ai model to generate jsonschema . The geneared json schema is then saved back to jsonschema output location.

# Assumption FDC3 repository source files are accessible for python utility
# Process Cycle
Step1 : User creates a new type in ContextTypes.ts file
Step2 : User needs to update UpdatedTypes.json file with newly added type name only in typescript application repository 
Step3 : Python job reads UpdatedTypes.json and gets list of updated type names
Step4 : Python also reads ContextTypes.ts file and sends info to open ai model to generate jsonSchema
Step5: Open ai process information and generates jsonSchema and saves at specificed location
