

import instructor
from openai import OpenAI
import json
import schedule
import time


# Define path of json file containting updated types 

#This function is to call open ai model to genrate required schema 
def generateJsonSchema():
  
  # Open and read the JSON file , 
  with open(r'C:\Users\Swati\typescript_project\src\updatedTypeScriptTypes.json', encoding="UTF-8") as file:
      jsonSchemaNameListStr = json.load(file)

  # Print the data
  print(jsonSchemaNameListStr['typenames'])

  updatedTypes = jsonSchemaNameListStr['typenames']
  for typeName in updatedTypes:
    client  = OpenAI(api_key='apikey')
    print(client)

    f = open(r"C:\Users\Swati\typescript_project\src\ContextTypes.ts",  encoding="utf-8")
    typedef = str(f.read())

    prompt_str = "Generate jsonschema for " + typeName  + " with id , title , description  for each property refering to typescript type "+ str(typedef) 
    print(prompt_str)
    response = client.chat.completions.create(
      model="gpt-4-1106-preview",
      messages=[
          {
            "role": "user",
            "content": prompt_str
          }
        ],
        temperature=0.7,
        max_tokens=800,
        top_p=1
    )
    print(response.choices[0].message.content)
    jsonschemaStr = response.choices[0].message.content.split("```json")

    jsonschema = jsonschemaStr[1].split("```")[0]
    print(jsonschema)
      
    
    path = "C:\\Users\\Swati\\typescript_project\\" + typeName + ".schema.json"
      # Writing to sample.json
    with open(path, "w") as outfile:
        outfile.write(jsonschema)
  return 



# Task scheduling

# Every day at 12am or 00:00 time bedtime() is called.
schedule.every().day.at("00:00").do(generateJsonSchema)
 
# Loop so that the scheduling task
# keeps on running all time.
while True:
 
    # Checks whether a scheduled task 
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
