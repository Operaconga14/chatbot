from api.config.config import rl


def generate_session_id():
    session_id = str(rl.uuid.uuid4().hex)[:8]
    return session_id
