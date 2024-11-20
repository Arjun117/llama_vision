import ollama

#img = 'C:/tensorflow1/models/research/object_detection/ocr_api/images/Fashion.png'
img = 'C:/images_new_invoice/inv.jpg'

response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': 'What is in this image?',
        'images': [img]
    }]
)

print(response["message"]["content"])     