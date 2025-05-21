from api.config.config import rl


def generate_chat_id():
    chat_id = str(rl.uuid.uuid4())[:8]
    return chat_id


def start_chat(message):
    return f"{message}"


def test_url():
    response = rl.requests.post(url=f"www.googlr.com", headers=rl.headers)
    return response.text
