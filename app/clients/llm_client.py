# app/clients/llm_client.py
import os
import logging
from typing import List, Dict, Any
import openai
from openai.error import RateLimitError, OpenAIError

logger = logging.getLogger(__name__)

class LLMClient:
    def __init__(self, api_key: str = None, model_name: str = "gpt-3.5-turbo") -> None:
        key = api_key or os.getenv("OPENAI_API_KEY")
        if not key:
            raise ValueError("Не задан OPENAI_API_KEY.")
        openai.api_key = key
        self.model_name = model_name

    def get_response(self, prompt: str, context: List[Dict[str, str]] = None,
                     temperature: float = 0.7, max_tokens: int = 150) -> str:
        messages = []
        if context:
            messages = [{"role": "user", "content": c[0]} for c in context]
        messages.append({"role": "user", "content": prompt})
        try:
            resp = openai.ChatCompletion.create(
                model=self.model_name,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            return resp.choices[0].message.content.strip()
        except RateLimitError as e:
            logger.warning("Rate limit exceeded: %s", e)
            raise
        except OpenAIError as e:
            logger.error("OpenAI error: %s", e)
            raise