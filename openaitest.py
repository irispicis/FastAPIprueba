import openai
from pydantic import BaseModel

openai.organization = 'org-2cWY9wXKn7PCXIWc7y0eMl7e'
openai.api_key = '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'
class Document(BaseModel):
    prompt: str = ''
def inference(prompt: str) -> list:
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "system", "content": """Eres un calculador factorial, calculas el factorial de cada número que sea ingresado,
          -Si el número es ingresado en forma de texto regresaras syntax error""",
           },
          {"role": "user", "content": prompt}
        ]
    )
    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens
    print("Se han utilizado los siguientes tokens: " + total_tokens)
    print('[SE TERMINÓ DE PROCESAR]'.center(40, '-'))
    return [content, total_tokens]
