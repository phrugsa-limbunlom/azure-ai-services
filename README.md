# Azure AI Services

A collection of AI applications utilizing Azure AI services, including OpenAI, Search, Language, Speech, and Vision.

## Features

This repository contains various AI-powered functionalities:

- 📄 **RAG with OpenAI** - Implement Retrieval-Augmented Generation (RAG) with document indexing.
- 🛡️ **Prompt Shield** - Protect content using prompt shielding.
- 🖼️ **Image Analysis** - Analyze images for insights and detect objects.
- 🏷️ **Image Classification** - Train and test custom image classification models.
- 🎙️ **Speech To Text** - Convert speech into text.
- 🌍 **Speech Translation** - Translate spoken language.
- 📝 **Text Analysis** - Perform sentiment analysis, entity recognition, and text processing.

## Provision Azure Resources

To set up the required Azure services, follow these steps:

- 🤖 **Azure OpenAI**  : *Create a resource → Azure OpenAI → Collect Key and Endpoint*
- 🔍 **Azure AI Search (Indexing)**  : *Create a resource → AI Search → Collect Key and Endpoint*
- 📦 **Azure Storage**  : *Create a resource → Storage Account*
- 🖼️ **Azure Vision Services**  : *Create a resource → Azure AI Services → Collect Key and Endpoint*
- 🏷️ **Azure Custom Vision**  : *Create a resource → Azure Custom vision*
- 🎤 **Azure Speech Services**  : *Create a resource → Speech Services → Collect Key and Endpoint*
- 🗣️ **Azure Language Services**  : *Create a resource → Azure Language Services → Collect Key and Endpoint*

## Model Deployment

### Custom Image Classification

**Model Training and Deployment**
1. Go to https://customvision.ai
2. Create a new project
3. Add images file
4. Tag a label
5. Repeat steps 3 and 4 until add all labels
6. Click the *Train* button
7. Review performance metrics
8. Click the *Performance* tab and the *Publish* button

**Model Testing**
1. Go to the Custom Vision portal home page
2. Under *Resource*, find prediction resource (ends with *-Prediction*)
3. Collect Key and Endpoint

### OpenAI Foundation Models

**Embedding model**
1. Go to the Azure OpenAI resource
2. Click the Azure AI Foundry portal
3. On the Deployment page, create a new base model deployment: *text-embedding-ada-002*

**Large language model**
1. Go to the Azure OpenAI resource
2. Click the Azure AI Foundry portal
3. On the Deployment page, create a new base model deployment: *gpt-35-turbo-16k*

## Indexing
1. Go to the storage account
2. Select *Blob containers*
3. Add a new container
4. Go to the Azure AI Search resource
5. Select *Import and vectorize data*
6. Select *Azure Blob Storage*
7. On the Vectorize your text page, set *Kind: Azure OpenAI* and *Model deployment: text-embedding-ada-002*
8. Set index name and then create the index

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
