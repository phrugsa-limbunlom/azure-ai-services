#
# Copyright (c) Microsoft. All rights reserved.
# To learn more, please visit the documentation - Quickstart: Azure Content Safety: https://aka.ms/acsstudiodoc
#
import requests
import os
import load_dotenv, find_dotenv


def shield_prompt_body(
    user_prompt: str,
    documents: list
) -> dict:
    """
    Builds the request body for the Content Safety API request.

    Args:
    - user_prompt (str): The user prompt to analyze.
    - documents (list): The documents to analyze.

    Returns:
    - dict: The request body for the Content Safety API request.
    """
    body = {
        "userPrompt": user_prompt,
        "documents": documents
    }
    return body


def detect_groundness_result(
    data: dict,
    url: str,
    subscription_key: str
):
    """
    Retrieve the Content Safety API request result.

    Args:
    - data (dict): The body data sent in the request.
    - url (str): The URL address of the request being sent.
    - subscription_key (str): The subscription key value corresponding to the request being sent.

    Returns:
    - response: The request result of the Content Safety API.
    """
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": subscription_key
    }

    # Send the API request
    response = requests.post(url, headers=headers, json=data)
    return response


if __name__ == "__main__":

    load_dotenv(find_dotenv())
    
    # Configure the Content Safety API request
    subscription_key =  os.getenv("CONTENT_SAFE_SUBSCRIPTION_KEY")
    endpoint = os.getenv("CONTENT_SAFE_ENDPOINT")

    api_version = "2024-09-01"

    # Set according to the actual task category.
    user_prompt = "<test_user_prompt>"
    documents = [
        "<this_is_a_documents>",
        "<this_is_another_documents>"
    ]

    # Build the request body
    data = shield_prompt_body(user_prompt=user_prompt, documents=documents)
    # Set up the API request
    url = f"{endpoint}/contentsafety/text:shieldPrompt?api-version={api_version}"

    # Send the API request
    response = detect_groundness_result(data=data, url=url, subscription_key=subscription_key)

    # Handle the API response
    if response.status_code == 200:
        result = response.json()
        print("shieldPrompt result:", result)
    else:
        print("Error:", response.status_code, response.text)