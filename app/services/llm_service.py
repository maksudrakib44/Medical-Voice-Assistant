from groq import Groq
from app.core.config import settings

class LLMService:

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

        self.model = settings.MODEL_NAME

    def generate(self, messages):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )

        return response.choices[0].message.content

    def generate_stream(self, messages):

        stream = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=True
        )

        for chunk in stream:

            if chunk.choices[0].delta.content:

                yield chunk.choices[0].delta.content