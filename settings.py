from pydantic import BaseSettings

class Settings(BaseSettings):
    # General settings
    app_environment = 'dev'
    model: str = 'gpt4all-falcon-q4_0.gguf'
    gpt4all_path: str = './models'

    # GPT4All settings
    n_threads: int = None
    temp: float = 0.18
    top_p: float = 1.0
    top_k: int = 50
    repeat_penalty: float = 1.18

settings = Settings()
