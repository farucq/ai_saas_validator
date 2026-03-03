from groq import Groq
from config.settings import GROQ_API_KEY, MODEL_NAME
from utils.logger import logger

client = Groq(api_key=GROQ_API_KEY)


def ask_llm(prompt):
    logger.info("Sending request to LLM")

    try:
        chat = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=MODEL_NAME
        )

        response = chat.choices[0].message.content

        logger.info("LLM response received successfully")
        return response

    except Exception as e:
        logger.error(f"LLM request failed: {str(e)}")
        return "LLM request failed."