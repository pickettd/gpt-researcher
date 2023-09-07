"""Configuration class to store the state of bools for different scripts access."""
import os

import openai
#from langchain.chat_models import ChatOllama
#from langchain.chat_models import ChatLiteLLM
from colorama import Fore
from dotenv import load_dotenv

from config.singleton import Singleton

load_dotenv(verbose=True)

class Config(metaclass=Singleton):
    """
    Configuration class to store the state of bools for different scripts access.
    """

    def __init__(self) -> None:
        """Initialize the Config class"""
        self.debug_mode = True
        self.allow_downloads = False

        self.selenium_web_browser = os.getenv("USE_WEB_BROWSER", "chrome")
        self.llm_provider = os.getenv("LLM_PROVIDER", "ChatOpenAI")
        #self.llm_provider = "ChatLiteLLM"
        #self.llm_provider = "ChatOllama"
        # self.llm_provider = "AzureChatOpenAI"

        self.fast_llm_model = os.getenv("FAST_LLM_MODEL", "gpt-3.5-turbo-16k")
        self.smart_llm_model = os.getenv("SMART_LLM_MODEL", "gpt-4")
        self.fast_llm_deployment_id = os.getenv("FAST_LLM_DEPLOYMENT_ID")
        self.smart_llm_deployment_id = os.getenv("SMART_LLM_DEPLOYMENT_ID")
        # self.fast_llm_model = "wizard-vicuna:13b"
        # self.smart_llm_model = "wizard-vicuna:13b"
        #self.fast_llm_model = "vicuna:13b-v1.5-16k-q4_0"
        #self.smart_llm_model = "vicuna:13b-v1.5-16k-q4_0"
        self.use_deployment_id = True

        self.fast_token_limit = int(os.getenv("FAST_TOKEN_LIMIT", 4000))
        self.smart_token_limit = int(os.getenv("SMART_TOKEN_LIMIT", 8000))
        self.browse_chunk_max_length = int(os.getenv("BROWSE_CHUNK_MAX_LENGTH", 8192))

        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.temperature = float(os.getenv("TEMPERATURE", "1"))

        self.user_agent = os.getenv(
            "USER_AGENT",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        )

        self.memory_backend = os.getenv("MEMORY_BACKEND", "local")
        # Initialize the OpenAI API client
        openai.api_key = self.openai_api_key
        openai.api_type = "azure"
        openai.api_version = "2023-05-15"
        openai.api_base = os.getenv("OPENAI_API_BASE")

    def set_fast_llm_model(self, value: str) -> None:
        """Set the fast LLM model value."""
        self.fast_llm_model = value

    def set_smart_llm_model(self, value: str) -> None:
        """Set the smart LLM model value."""
        self.smart_llm_model = value

    def set_fast_token_limit(self, value: int) -> None:
        """Set the fast token limit value."""
        self.fast_token_limit = value

    def set_smart_token_limit(self, value: int) -> None:
        """Set the smart token limit value."""
        self.smart_token_limit = value

    def set_browse_chunk_max_length(self, value: int) -> None:
        """Set the browse_website command chunk max length value."""
        self.browse_chunk_max_length = value

    def set_openai_api_key(self, value: str) -> None:
        """Set the OpenAI API key value."""
        self.openai_api_key = value

    def set_debug_mode(self, value: bool) -> None:
        """Set the debug mode value."""
        self.debug_mode = value


def check_openai_api_key() -> None:
    """Check if the OpenAI API key is set in config.py or as an environment variable."""
    cfg = Config()
    if not cfg.openai_api_key:
        print(
            Fore.RED
            + "Please set your OpenAI API key in .env or as an environment variable."
        )
        print("You can get your key from https://platform.openai.com/account/api-keys")
        exit(1)
