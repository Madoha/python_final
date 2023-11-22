from concurrent.futures import ThreadPoolExecutor
from web.main_flask import run_flask
from main_fastapi import run_fastapi

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as executor:
        future_flask = executor.submit(run_flask)
        future_fastapi = executor.submit(run_fastapi)

        # Ожидаем завершения обоих потоков
        future_flask.result()
        future_fastapi.result()