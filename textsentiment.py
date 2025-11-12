# textsentiment.py
# Developed by Yash Tagunde for Edge Data Analytics submission
# Uses Azure Cognitive Services Text Analytics API to analyze sentiment of text files

import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def authenticate_client():
    key = os.getenv("AZURE_LANGUAGE_KEY")
    endpoint = os.getenv("AZURE_LANGUAGE_ENDPOINT")

    if not key or not endpoint:
        raise RuntimeError("Please set AZURE_LANGUAGE_KEY and AZURE_LANGUAGE_ENDPOINT environment variables.")
    
    return TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

def analyze_sentiment(file_path: str, output_file: str | None = None):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Text file not found: {file_path}")

    client = authenticate_client()

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    response = client.analyze_sentiment(documents=[text])[0]

    result = (
        f"Overall sentiment: {response.sentiment}\n"
        f"Positive: {response.confidence_scores.positive:.2f}\n"
        f"Neutral: {response.confidence_scores.neutral:.2f}\n"
        f"Negative: {response.confidence_scores.negative:.2f}\n"
    )

    print(result)

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"Results saved → {output_file}")

def main():
    import argparse
    p = argparse.ArgumentParser(description="Analyze sentiment of a text file using Azure Text Analytics.")
    p.add_argument("file", help="Path to input text file")
    p.add_argument("--out", default=None, help="Path to output text file")
    args = p.parse_args()

    analyze_sentiment(args.file, args.out)

if __name__ == "__main__":
    main()
