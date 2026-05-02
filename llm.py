import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def call_llm(prompt, model="phi3"):
    # Sends a prompt to the Ollama model and returns the response text.
    
    try: 
        response = requests.post(
            OLLAMA_URL,
            json={
                "model":model,
                "prompt":prompt,
                "stream":False,
                "options":{
                    "temperature":0.1
                }
            },
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data.get("response", "").strip()
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama. Is it running?"

    except requests.exceptions.Timeout:
        return "Error: Request timed out."

    except Exception as e:
        return f"Error: {str(e)}"
    


