import dotenv
import os
from pathlib import Path

current_dir = Path(__file__).parent.absolute()

env_file = os.getenv("SCWEET_ENV_FILE", current_dir.parent.joinpath(".env"))
dotenv.load_dotenv(env_file, verbose=True)
