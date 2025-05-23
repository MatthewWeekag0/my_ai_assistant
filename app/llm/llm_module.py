# app/llm_module.py

import asyncio
from openai import AsyncOpenAI
import httpx

class LLMModule:
    def __init__(self, openai_key):
        self.client = AsyncOpenAI(api_key=openai_key)

    async def _query_chatgpt(self, text):
        try:
            response = await self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": text}],
                timeout=10  # Таймаут в секундах
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Ошибка при запросе к ChatGPT: {e}"

    async def _query_gemini(self, text):
        try:
            # Псевдокод для Gemini API с использованием httpx
            async with httpx.AsyncClient(timeout=10) as client:
                response = await client.post(
                    "https://api.gemini.com/v1/chat/completions",
                    json={"messages": [{"role": "user", "content": text}]},
                    headers={"Authorization": "Bearer YOUR_GEMINI_API_KEY"}
                )
                response.raise_for_status()
                data = response.json()
                return data["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Ошибка при запросе к Gemini: {e}"

    async def query_llm(self, text):
        chatgpt_task = self._query_chatgpt(text)
        gemini_task = self._query_gemini(text)
        chatgpt_ans, gemini_ans = await asyncio.gather(chatgpt_task, gemini_task)
        # Выбор ответа с большей длиной
        return chatgpt_ans if len(chatgpt_ans) >= len(gemini_ans) else gemini_ans
