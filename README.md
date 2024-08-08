# bimser-staj-2024-2

```Use dev branch for development and create pull request to merge with main!```

```py
python version: 3.10
```

## Usage
```sh
# Create env
python3.10 -m venv env

# Activate env
...

# Install requirements
(env) pip install -r requirements.txt

# Test

pytest -s
pytest -s app/tests/test_main.py
pytest -s app/tests/test_main.py::test_read_main

# Run fastapi (auto reload)
fastapi dev

# Run fastapi
fastapi run
```

## Project Diagrams

### Class Diagram

![class_diagram](diagrams/class_diagram.png)

### Sequence Diagram

![sequence_diagram](diagrams/sequence_diagram.png)

### Deployment Diagram

![deployment_diagram](diagrams/deployment_diagram.png)

## Detailed Project Diagrams

### Class Diagram

![detailed_class_diagram](diagrams/detailed_class_diagram.png)

### Sequence Diagram

#### Insert Document Sequence

![insert_document_sequence_diagram](diagrams/insert_document_sequence_diagram.png)

#### Query Document Sequence

![query_documents_sequence_diagram](diagrams/query_documents_sequence_diagram.png)

#### Generate Response Sequence

![generate_response_sequence_diagram](diagrams/generate_response_sequence_diagram.png)

### Deployment Diagram

![detailed_deployment_diagram](diagrams/detailed_deployment_diagram.png)