import requests
import json

class LangDrive:
    def __init__(self) -> None:
        pass

    def completion(self, prompt: str, model: str, max_tokens: int) -> str:
        """
        Make a Post request to call: 
        POST https://api.langdrive.ai/v1/chat/completions.
        
        Returns generated text in response.
        """     
        url = "https://api.langdrive.ai/v1/chat/completions"
        
        headers = {
            'Content-Type': 'application/json'
        }
        
        # Prepare the data
        data = {
            "prompt": prompt,
            "model": model,
            # "max_tokens": max_tokens
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        
        if response.status_code == 200:
            # Parse the response & return generated_text
            # If it was successful or not
            response_data = json.loads(response.text)
            
            if response_data.get('success'):
                return response_data.get('generated_text', '')
            else:
                return "Request unsuccessful."
                
        else:
            return f"HTTP request failed with status code {response.status_code}."
