from dotenv import load_dotenv, find_dotenv


def init_env():
    load_dotenv(find_dotenv())
