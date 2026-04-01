import tkinter as tk


class AdminView:
    def __init__(self, root):
        self.root = root
        self.root.title("CSP TicTacToe Admin")
        self.root.geometry("700x500")

        self.admin_name_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.login_status_var = tk.StringVar(value="Введіть дані адміністратора")
        self.server_status_var = tk.StringVar(value="Сервер: offline")
        self.admin_info_var = tk.StringVar(value="Адмін: -")
        self.action_status_var = tk.StringVar(value="")

        self.selected_player_var = tk.StringVar(value="Немає гравців")
        self.selected_session_var = tk.StringVar(value="Немає сесій")

        self.player_options = ["Немає гравців"]
        self.session_options = ["Немає сесій"]

        self.login_frame = tk.Frame(self.root, padx=20, pady=20)
        self.login_frame.pack(fill="both", expand=True)

        self.login_title_label = tk.Label(
            self.login_frame,
            text="Вхід в адмінку",
            font=("Arial", 16, "bold")
        )
        self.login_title_label.pack(pady=(20, 20))

        self.admin_name_label = tk.Label(
            self.login_frame,
            text="Ім'я адміністратора:"
        )
        self.admin_name_label.pack(anchor="w")

        self.admin_name_entry = tk.Entry(
            self.login_frame,
            textvariable=self.admin_name_var,
            width=35
        )
        self.admin_name_entry.pack(pady=(0, 10))

        self.password_label = tk.Label(
            self.login_frame,
            text="Пароль:"
        )
        self.password_label.pack(anchor="w")

        self.password_entry = tk.Entry(
            self.login_frame,
            textvariable=self.password_var,
            show="*",
            width=35
        )
        self.password_entry.pack(pady=(0, 15))

        self.login_button = tk.Button(
            self.login_frame,
            text="Увійти",
            width=20
        )
        self.login_button.pack(pady=(0, 15))

        self.login_status_label = tk.Label(
            self.login_frame,
            textvariable=self.login_status_var,
            fg="blue"
        )
        self.login_status_label.pack()

        self.main_frame = tk.Frame(self.root, padx=15, pady=15)

        self.top_frame = tk.Frame(self.main_frame)
        self.top_frame.pack(fill="x", pady=(0, 10))

        self.admin_info_label = tk.Label(
            self.top_frame,
            textvariable=self.admin_info_var,
            font=("Arial", 10, "bold")
        )
        self.admin_info_label.pack(side="left", padx=(0, 20))

        self.server_status_label = tk.Label(
            self.top_frame,
            textvariable=self.server_status_var,
            fg="green"
        )
        self.server_status_label.pack(side="left")

        self.refresh_button = tk.Button(
            self.top_frame,
            text="Оновити",
            width=12
        )
        self.refresh_button.pack(side="right", padx=(10, 0))

        self.logout_button = tk.Button(
            self.top_frame,
            text="Вийти",
            width=12
        )
        self.logout_button.pack(side="right")

        self.users_button = tk.Button(
            self.top_frame,
            text="Усі користувачі",
            width=16
        )
        self.users_button.pack(side="right", padx=(0, 10))

        self.sessions_frame = tk.Frame(self.main_frame)
        self.sessions_frame.pack(fill="both", expand=True, pady=(0, 10))

        self.sessions_title_label = tk.Label(
            self.sessions_frame,
            text="Активні сесії:",
            font=("Arial", 12, "bold")
        )
        self.sessions_title_label.pack(anchor="w", pady=(0, 5))

        self.sessions_text = tk.Text(
            self.sessions_frame,
            height=12,
            width=80,
            state="disabled"
        )
        self.sessions_text.pack(fill="both", expand=True)

        self.actions_frame = tk.Frame(self.main_frame)
        self.actions_frame.pack(fill="x", pady=(10, 10))

        self.player_frame = tk.Frame(self.actions_frame)
        self.player_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

        self.player_label = tk.Label(
            self.player_frame,
            text="Оберіть гравця:"
        )
        self.player_label.pack(anchor="w")

        self.player_option_menu = tk.OptionMenu(
            self.player_frame,
            self.selected_player_var,
            *self.player_options
        )
        self.player_option_menu.config(width=28)
        self.player_option_menu.pack(fill="x", pady=(5, 10))

        self.kick_button = tk.Button(
            self.player_frame,
            text="Кікнути гравця",
            width=20
        )
        self.kick_button.pack(anchor="w")

        self.session_frame = tk.Frame(self.actions_frame)
        self.session_frame.pack(side="left", fill="both", expand=True, padx=(10, 0))

        self.session_label = tk.Label(
            self.session_frame,
            text="Оберіть сесію:"
        )
        self.session_label.pack(anchor="w")

        self.session_option_menu = tk.OptionMenu(
            self.session_frame,
            self.selected_session_var,
            *self.session_options
        )
        self.session_option_menu.config(width=28)
        self.session_option_menu.pack(fill="x", pady=(5, 10))

        self.end_session_button = tk.Button(
            self.session_frame,
            text="Завершити сесію",
            width=20
        )
        self.end_session_button.pack(anchor="w")

        self.action_status_label = tk.Label(
            self.main_frame,
            textvariable=self.action_status_var,
            fg="darkred",
            anchor="w",
            justify="left"
        )
        self.action_status_label.pack(fill="x", pady=(10, 0))

    def show_login_frame(self):
        self.main_frame.pack_forget()
        self.login_frame.pack(fill="both", expand=True)

    def show_main_frame(self):
        self.login_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)

    def get_admin_name(self):
        return self.admin_name_var.get().strip()

    def get_password(self):
        return self.password_var.get().strip()

    def get_selected_player(self):
        return self.selected_player_var.get()

    def get_selected_session(self):
        return self.selected_session_var.get()

    def set_login_status(self, text):
        self.login_status_var.set(text)

    def set_server_status(self, text):
        self.server_status_var.set(text)

    def set_admin_info(self, text):
        self.admin_info_var.set(text)

    def set_action_status(self, text):
        self.action_status_var.set(text)

    def set_sessions_text(self, text):
        self.sessions_text.config(state="normal")
        self.sessions_text.delete("1.0", tk.END)
        self.sessions_text.insert(tk.END, text)
        self.sessions_text.config(state="disabled")

    def show_users_window(self, users, get_games, get_moves):
        win = tk.Toplevel(self.root)
        win.title("Зареєстровані користувачі")
        win.geometry("420x620")
        win.resizable(False, True)

        tk.Label(
            win,
            text="Зареєстровані користувачі:",
            font=("Arial", 12, "bold")
        ).pack(anchor="w", padx=15, pady=(15, 5))

        users_frame = tk.Frame(win)
        users_frame.pack(fill="both", expand=False, padx=15, pady=(0, 10))

        users_scrollbar = tk.Scrollbar(users_frame)
        users_scrollbar.pack(side="right", fill="y")

        users_listbox = tk.Listbox(
            users_frame,
            yscrollcommand=users_scrollbar.set,
            font=("Arial", 11),
            height=8
        )
        users_listbox.pack(fill="both", expand=True)
        users_scrollbar.config(command=users_listbox.yview)

        if not users:
            users_listbox.insert(tk.END, "Користувачів немає")
        else:
            for user in users:
                users_listbox.insert(tk.END, user.get("login", "-"))

        tk.Label(
            win,
            text="Ігри користувача:",
            font=("Arial", 11, "bold")
        ).pack(anchor="w", padx=15, pady=(5, 5))

        games_frame = tk.Frame(win)
        games_frame.pack(fill="both", expand=False, padx=15, pady=(0, 10))

        games_scrollbar = tk.Scrollbar(games_frame)
        games_scrollbar.pack(side="right", fill="y")

        games_listbox = tk.Listbox(
            games_frame,
            yscrollcommand=games_scrollbar.set,
            font=("Arial", 10),
            height=8
        )
        games_listbox.pack(fill="both", expand=True)
        games_scrollbar.config(command=games_listbox.yview)

        tk.Label(
            win,
            text="Історія ходів у грі:",
            font=("Arial", 11, "bold")
        ).pack(anchor="w", padx=15, pady=(5, 5))

        moves_frame = tk.Frame(win)
        moves_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        moves_scrollbar = tk.Scrollbar(moves_frame)
        moves_scrollbar.pack(side="right", fill="y")

        moves_text = tk.Text(
            moves_frame,
            wrap="word",
            state="disabled",
            font=("Arial", 10),
            yscrollcommand=moves_scrollbar.set
        )
        moves_text.pack(fill="both", expand=True)
        moves_scrollbar.config(command=moves_text.yview)

        game_map = {}

        def set_moves_text(text):
            moves_text.config(state="normal")
            moves_text.delete("1.0", tk.END)
            moves_text.insert(tk.END, text)
            moves_text.config(state="disabled")

        def on_user_select(event):
            selection = users_listbox.curselection()
            if not selection:
                return

            login = users_listbox.get(selection[0])

            games_listbox.delete(0, tk.END)
            game_map.clear()
            set_moves_text("")

            if login == "Користувачів немає":
                return

            games = get_games(login)

            if not games:
                games_listbox.insert(tk.END, "Ігор немає")
                return

            for game in games:
                text = (
                    f"{game.get('played_at', '')} - "
                    f"{game.get('game_id', '')} - "
                    f"{game.get('opponent', '')} - "
                    f"{game.get('result', '')}"
                )
                games_listbox.insert(tk.END, text)
                game_map[text] = game.get("game_id")

        def on_game_select(event):
            selection = games_listbox.curselection()
            if not selection:
                return

            game_text = games_listbox.get(selection[0])

            if game_text == "Ігор немає":
                set_moves_text("")
                return

            game_id = game_map.get(game_text)
            if game_id is None:
                set_moves_text("Не вдалося визначити гру.")
                return

            moves = get_moves(game_id)

            if not moves:
                set_moves_text("Історія ходів відсутня.")
                return

            lines = []
            for move in moves:
                lines.append(
                    f"{move.get('move_number', '')}. "
                    f"{move.get('player', '')} "
                    f"({move.get('login', '')}) -> "
                    f"{move.get('position', '')}"
                )

            set_moves_text("\n".join(lines))

        users_listbox.bind("<<ListboxSelect>>", on_user_select)
        games_listbox.bind("<<ListboxSelect>>", on_game_select)

    def update_player_menu(self, players):
        if not players:
            players = ["Немає гравців"]

        self.player_options = players
        self.selected_player_var.set(players[0])

        menu = self.player_option_menu["menu"]
        menu.delete(0, "end")

        for player in players:
            menu.add_command(
                label=player,
                command=lambda value=player: self.selected_player_var.set(value)
            )

    def update_session_menu(self, sessions):
        if not sessions:
            sessions = ["Немає сесій"]

        self.session_options = sessions
        self.selected_session_var.set(sessions[0])

        menu = self.session_option_menu["menu"]
        menu.delete(0, "end")

        for session in sessions:
            menu.add_command(
                label=session,
                command=lambda value=session: self.selected_session_var.set(value)
            )

    def clear_login_fields(self):
        self.admin_name_var.set("")
        self.password_var.set("")

    def clear_action_status(self):
        self.action_status_var.set("")