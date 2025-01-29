import requests
import json

url = "http://127.0.0.1:8080/v1/chat/completions"
headers = {
    "Content-Type": "application/json"
}
data = {
    "model": "deepseek-r1-distill-llama-8b",
    "messages": [
        { "role": "system", "content": "Responde en Español" },
        {
            "role": "user",
            "content": "Resuelve el siguiente sistema de ecuaciones no lineales utilizando el método de sustitución o igualación: \n\nx^2 + y^2 = 25 \n2x - y = 4"
        }
    ],
    "temperature": 0.7,
    "max_tokens": -1,
    "stream": True
}
response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)
response_text = ""
for chunk in response.iter_lines():
    if chunk:
        cleaned_chunk = chunk.decode('utf-8').replace('data: ', '')
        try:
            chunk_data = json.loads(cleaned_chunk)
            if "choices" in chunk_data:
                for choice in chunk_data["choices"]:
                    if "delta" in choice and "content" in choice["delta"]:
                        content = choice["delta"]["content"]
                        response_text += content 
        except json.JSONDecodeError:
            print("Error al decodificar el fragmento:", cleaned_chunk)
        if "data" in cleaned_chunk and '"DONE"' in cleaned_chunk:
            break 
print(response_text)
