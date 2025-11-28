# Data-Processing-Tool
A Python-based data processing pipeline designed as a demonstration for MDA. Features modular data ingestion and an LLM-driven processing workflow. 

<img width="1015" height="404" alt="Screenshot 2025-11-28 at 1 49 03 PM" src="https://github.com/user-attachments/assets/e7121c70-007d-4bc2-abd8-3be249440433" />



**Repository Structure**
- pipeline.py: The core logic engine that orchestrates the flow of data from input to final output.
- ingest.py: Handles data loading and preprocessing, preparing raw information for the pipeline.
- system_prompt.md: Contains the system-level instructions for the LLM.
- requirements.txt: Lists necessary Python dependencies for reproduction.

**Workflow**
- Upon running the program, .eml file is manually placed in folder on desktop labed CY 25
- Folder is scanned every 5 seconds
- An exel file is automatically created and filled out with information in the .eml file according to the structure laid out in requirements documentation
- If information cannot be parsed, it will be sent to a rejects folder that is created on the desktop. 
