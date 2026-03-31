import hashlib


class AdminController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.player_map = {}
        self.session_map = {}

        self.view.login_button.config(command=self.login)
        self.view.refresh_button.config(command=self.refresh_sessions)
        self.view.logout_button.config(command=self.logout)
        self.view.kick_button.config(command=self.kick_player)
        self.view.end_session_button.config(command=self.close_session)
        self.view.users_button.config(command=self.show_users)

        self.view.show_login_frame()

    def login(self):
        login = self.view.get_admin_name()
        password = self.view.get_password()

        if not login or not password:
            self.view.set_login_status("Введіть логін і пароль")
            return

        self.view.set_login_status("Підключення до сервера...")

        if not self.model.connect():
            self.view.set_login_status("Не вдалося підключитися до сервера")
            return

        password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
        response_type = self.model.login(login, password_hash)

        if response_type != "auth_ok":
            self.view.set_login_status("Невірний логін або пароль")
            self.model.close()
            return

        self.view.set_login_status("Вхід виконано успішно")
        self.view.set_admin_info(f"Адмін: {login}")
        self.view.set_server_status("Сервер: онлайн")
        self.view.show_main_frame()

        self.refresh_sessions()

    def show_users(self):
        response = self.model.get_users()

        if not response or response.get("type") != "users_list":
            self.view.set_action_status("Помилка отримання списку користувачів")
            return

        users = response.get("users", [])
        self.view.show_users_window(users)

    def refresh_sessions(self):
        response = self.model.get_sessions()

        if not response or response.get("type") != "sessions_list":
            self.view.set_action_status("Помилка отримання списку сесій")
            return

        sessions = response.get("sessions", [])

        self.player_map = {}
        self.session_map = {}

        if not sessions:
            self.view.set_sessions_text("Активних сесій немає")
            self.view.update_player_menu([])
            self.view.update_session_menu([])
            self.view.set_action_status("Список сесій оновлено")
            return

        text_lines = []
        player_list = []
        session_list = []

        for session in sessions:
            session_id = session.get("session_id")

            player_x = session.get("x_login", "-")
            player_o = session.get("o_login", "-")

            if not player_x:
                player_x = "-"
            if not player_o:
                player_o = "-"

            line = f"Сесія {session_id}: {player_x} (X) - {player_o} (O)"
            text_lines.append(line)

            session_text = f"Сесія {session_id}: {player_x} vs {player_o}"
            session_list.append(session_text)
            self.session_map[session_text] = session_id

            if player_x != "-":
                player_text = f"{player_x} (Сесія {session_id}, X)"
                player_list.append(player_text)
                self.player_map[player_text] = (session_id, "X")

            if player_o != "-":
                player_text = f"{player_o} (Сесія {session_id}, O)"
                player_list.append(player_text)
                self.player_map[player_text] = (session_id, "O")

        self.view.set_sessions_text("\n".join(text_lines))
        self.view.update_player_menu(player_list)
        self.view.update_session_menu(session_list)
        self.view.set_action_status("Список сесій оновлено")

    def kick_player(self):
        selected_player = self.view.get_selected_player()

        if not selected_player or selected_player not in self.player_map:
            self.view.set_action_status("Оберіть гравця")
            return

        session_id, symbol = self.player_map[selected_player]

        response = self.model.kick_player(session_id, symbol)

        if not response or response.get("type") != "kick_ok":
            self.view.set_action_status("Помилка під час відключення гравця")
            return

        self.view.set_action_status(f"Гравця {selected_player} відключено")
        self.refresh_sessions()

    def close_session(self):
        selected_session = self.view.get_selected_session()

        if not selected_session or selected_session not in self.session_map:
            self.view.set_action_status("Оберіть сесію")
            return

        session_id = self.session_map[selected_session]

        response = self.model.close_session(session_id)

        if not response or response.get("type") != "close_ok":
            self.view.set_action_status("Помилка під час завершення сесії")
            return

        self.view.set_action_status(f"Сесію {session_id} завершено")
        self.refresh_sessions()

    def logout(self):
        self.model.close()

        self.player_map = {}
        self.session_map = {}

        self.view.set_server_status("Сервер: офлайн")
        self.view.set_admin_info("Адмін: -")
        self.view.set_action_status("")
        self.view.set_login_status("Введіть дані адміністратора")

        self.view.clear_login_fields()
        self.view.show_login_frame()