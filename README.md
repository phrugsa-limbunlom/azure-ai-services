# Azure AI Services

A collection of AI applications utilizing Azure AI services, including OpenAI, Search, Language, Speech, and Vision.

## Features

This repository contains various AI-powered functionalities:

- 📄 **RAG with OpenAI** - Implement Retrieval-Augmented Generation (RAG) with document indexing.
- 🖼️ **Image Analysis** - Analyze images for insights and detect objects.
- 🏷️ **Image Classification** - Train and test custom image classification models.
- 🛡️ **Prompt Shield** - Protect content using prompt shielding.
- 🎙️ **Speech-to-Text** - Convert speech into text.
- 🌍 **Speech Translation** - Translate spoken language.
- 📝 **Text Analysis** - Perform sentiment analysis, entity recognition, and text processing.

## Provision Azure Resources

To set up the required Azure services, follow these steps:

- 🔍 **Azure AI Search (Indexing)**  : *Create a resource → AI Search*
- 📦 **Azure Storage**  : *Create a resource → Storage Account*
- 🤖 **Azure OpenAI**  : *Create a resource → Azure OpenAI*
- 🗣️ **Azure Language Services**  : *Create a resource → Azure AI Services*
- 🖼️ **Azure Vision Services**  : *Create a resource → Azure AI ServicesCustom vision*
- 🏷️ **Azure Custom Vision**  : *Create a resource → Azure Custom vision*
- 🎤 **Azure Speech Services**  : *Create a resource → Speech Services*

## Configuration

### Install Required Libraries
```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file and add the following keys:

```ini
# Language Service
AI_SERVICE_ENDPOINT=<AI_SERVICE_ENDPOINT>
AI_SERVICE_KEY=<AI_SERVICE_KEY>

# Speech Service
SPEECH_KEY=<SPEECH_KEY>
SPEECH_REGION=<SPEECH_REGION>

# Vision Service
AI_VISION_SERVICE_ENDPOINT=<AI_VISION_SERVICE_ENDPOINT>
AI_VISION_SERVICE_KEY=<AI_VISION_SERVICE_KEY>

# Training Image Classification
TrainingEndpoint=<TrainingEndpoint>
TrainingKey=<TrainingKey>
ProjectID=<ProjectID>

# Testing Image Classification
PredictionEndpoint=<PredictionEndpoint>
PredictionKey=<PredictionKey>
ProjectID=<ProjectID>
ModelName=<ModelName>

# OpenAI and AI Search Services
AZURE_OAI_ENDPOINT=<AZURE_OAI_ENDPOINT>
AZURE_OAI_KEY=<AZURE_OAI_KEY>
AZURE_OAI_DEPLOYMENT=<AZURE_OAI_DEPLOYMENT>
AZURE_SEARCH_ENDPOINT=<AZURE_SEARCH_ENDPOINT>
AZURE_SEARCH_KEY=<AZURE_SEARCH_KEY>
AZURE_SEARCH_INDEX=<AZURE_SEARCH_INDEX>
```

## Run Services

Navigate to the respective directory and run the Python script:

```bash
cd {path_to_file}
python {file}
```

### Example
```bash
cd image-analysis
python image-analysis.py
```

## Resources
https://learn.microsoft.com/en-us/training/courses/ai-102t00#course-syllabus
