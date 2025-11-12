# Edge Data Analytics — Text Sentiment Analysis using Azure

This project demonstrates how to use **Azure Cognitive Services (Text Analytics)** to perform **Sentiment Analysis** on a given text file.  
It reads the input text, analyzes emotions (Positive, Neutral, Negative), and saves the results to a file.

## 🔧 Setup

1. Create an Azure **Text Analytics** resource (Free tier F0).
2. Set your environment variables:
   ```bash
   export AZURE_LANGUAGE_KEY="YOUR_KEY"
   export AZURE_LANGUAGE_ENDPOINT="YOUR_ENDPOINT"
