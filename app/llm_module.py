# app/llm_module.py

import openai
import asyncio

class LLMModule:
    def __init__(self, openai_key):
        openai.api_key = openai_key

    async def _query_chatgpt(self, text):
        response = await openai.ChatCompletion.acreate(
            model="gpt-4",
            messages=[{"role": "user", "content": text}]
        )
        return response.choices[0].message.content

    async def _query_gemini(self, text):
        # Псевдокод для Gemini API
        return "Ответ Gemini"

    def query_llm(self, text):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        tasks = [self._query_chatgpt(text), self._query_gemini(text)]
        chatgpt_ans, gemini_ans = loop.run_until_complete(asyncio.gather(*tasks))
        return chatgpt_ans if len(chatgpt_ans) >= len(gemini_ans) else gemini_ans
