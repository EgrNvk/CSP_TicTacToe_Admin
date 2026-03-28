import socket
import json

from cryptography.fernet import Fernet
from config import ADMIN_HOST, ADMIN_PORT, FERNET_KEY


class AdminModel:
    def __init__(self):
        self.host = ADMIN_HOST
        self.port = ADMIN_PORT

        self.client = None
        self.cipher_suite = Fernet(FERNET_KEY)

        self.connected = False

    def connect(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.host, self.port))
            self.connected = True
            return True
        except Exception as e:
            print(f"[ADMIN] Помилка підключення: {e}")
            self.connected = False
            return False

    def close(self):
        try:
            if self.client:
                self.client.close()
        except:
            pass
        finally:
            self.client = None
            self.connected = False

    def send_line(self, text):
        token = self.cipher_suite.encrypt(text.encode("utf-8"))
        self.client.sendall(token + b"\n")

    def recv_line(self):
        token = b""

        while True:
            b = self.client.recv(1)

            if not b:
                return ""

            if b == b"\n":
                break

            token += b

        try:
            plain = self.cipher_suite.decrypt(token)
            return plain.decode("utf-8")
        except:
            return ""

    def send_json(self, data):
        try:
            self.send_line(json.dumps(data))
        except:
            return False
        return True

    def recv_json(self):
        line = self.recv_line()
        if not line:
            return None

        try:
            return json.loads(line)
        except:
            return None

    def login(self, login, password_hash):
        request = {
            "type": "admin_auth",
            "login": login,
            "password_hash": password_hash
        }

        self.send_json(request)
        response = self.recv_json()

        if not response:
            return None

        return response.get("type")

    def get_sessions(self):
        self.send_json({
            "type": "get_sessions"
        })

        response = self.recv_json()
        if not response:
            return None

        return response

    def kick_player(self, session_id, symbol):
        self.send_json({
            "type": "kick_player",
            "session_id": session_id,
            "symbol": symbol
        })

        return self.recv_json()

    def close_session(self, session_id):
        self.send_json({
            "type": "close_session",
            "session_id": session_id
        })

        return self.recv_json()