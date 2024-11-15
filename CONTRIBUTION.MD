

# Project Contributor - Swati Ghadge 

# Project consumers -Users who wants to use the tool to generate JSON SCHEMAS Using Open ai

# Useful Info
This is python and open ai based tool . It is a python based scheduler which reads typescript context file and use it to generat json schema for only updated types . We maintain a json look up file which can be used to inform the tool which new json schemas to be created . This information is send to open ai model to generate jsonschema . The geneared json schema is then saved back to jsonschema output location.

## Assumption FDC3 repository source files are accessible for python utility

# Process Cycle
- Step1 : User creates a new type in ContextTypes.ts file
- Step2 : User needs to update updatedTypeScriptTypes.json.json file with newly added type name only in typescript application repository 
- Step3 : Python job reads updatedTypeScriptTypes.json.json and gets list of updated type names
- Step4 : Python also reads ContextTypes.ts file and sends info to open ai model to generate jsonSchema
- Step5: Open ai process information and generates jsonSchema and saves at specificed location
- Note : sample files for updatedTypeScriptTypes.json and  ContextTypes.ts are provided for ref in resource folder

# Contributing to JsonSchema Generator tool

Thank you for considering contributing to [Project Name]! We welcome all types of contributions, including bug reports, feature requests, documentation improvements, and code enhancements.

## How to Contribute

1. **Fork the Repository**
   - Fork the repository to your own GitHub account.
   - Clone the forked repository to your local machine.
   - Add the upstream repository:
     ```sh
     git remote add upstream https://github.com/[ORIGINAL_OWNER]/[REPOSITORY_NAME].git
     ```

2. **Create a Branch**
   - Create a new branch for your work:
     ```sh
     git checkout -b my-feature-branch
     ```

3. **Make Changes**
   - Make your changes to the codebase.
   - Ensure your code follows the project's coding standards and conventions.
   - Test your changes thoroughly.

4. **Commit Changes**
   - Commit your changes with a descriptive commit message:
     ```sh
     git add .
     git commit -m "Description of the changes"
     ```

5. **Push Changes**
   - Push your changes to your forked repository:
     ```sh
     git push origin my-feature-branch
     ```

6. **Create a Pull Request**
   - Go to the original repository and create a pull request from your forked repository's branch.
   - Provide a clear and descriptive title and description for your pull request.
   - Reference any relevant issues or discussions.

## Code of Conduct

We strive to provide a welcoming and inclusive environment for all contributors. Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a positive experience for everyone.

## Reporting Issues

If you encounter any bugs or have suggestions for improvements, please check if the issue is already reported. If not, create a new issue with a detailed description.

## Feature Requests

We welcome new feature ideas! Feel free to create an issue with your proposal, and let's discuss it.

## Acknowledgements

Thank you to all the contributors who make this project better!

---

We appreciate your efforts to contribute to This tool . Together, we can make this project amazing!

