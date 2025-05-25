# Add these to __init__:
self.current_question_in_round = 0
self.total_rounds = 10
self.questions_per_round = 5

def start_game(self):
    self.set_bg(self.bg_choice.get())
    self.players = [e.get() or f"Player {i+1}" for i, e in enumerate(self.name_entries)]
    self.scores = [0] * len(self.players)
    self.round = 1
    self.current_question_in_round = 0
    self.wheel_effect = None
    self.play_round()

def play_round(self):
    if self.round > self.total_rounds:
        self.show_scores(intermission=False, final=True)
        return
    if self.current_question_in_round == self.questions_per_round:
        # End of this round, intermission time
        self.show_scores(intermission=True)
    else:
        self.ask_question()

def submit_answers(self):
    try:
        guesses = [float(e.get()) for e in self.guess_entries]
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for all guesses.")
        return
    self.guesses = guesses
    diffs = [abs(g - self.current_answer) for g in guesses]
    winner_idx = diffs.index(min(diffs))
    winner_name = self.players[winner_idx]

    points = 1
    msg = f"{winner_name} was closest! Correct answer: {self.current_answer}. "
    if self.wheel_effect == "double":
        points = 2
        msg += "Double points applied! "
    elif self.wheel_effect == "winner_minus3":
        self.scores[winner_idx] -= 3
        msg += "But lost 3 points due to the wheel!"
    else:
        self.scores[winner_idx] += points

    if self.wheel_effect != "winner_minus3":
        self.scores[winner_idx] += points

    self.current_question_in_round += 1
    self.wheel_effect = None
    self.play_round()

def show_scores(self, intermission=False, final=False):
    self.clear_window()
    tk.Label(self.root, text="Scores so far:" if not final else "Final Scores:", font=('Arial', 18, 'bold')).pack(pady=10)
    for name, score in zip(self.players, self.scores):
        tk.Label(self.root, text=f"{name}: {score}").pack()
    if intermission:
        tk.Label(self.root, text=f"\nIntermission! End of Round {self.round}", font=('Arial', 16, 'bold')).pack(pady=10)
        tk.Button(self.root, text="Hear a dad joke", command=self.tell_joke).pack(pady=5)
    elif final:
        tk.Button(self.root, text="Play Again", command=self.start_game).pack(pady=10)
    else:
        tk.Button(self.root, text="Next Question", command=self.play_round).pack(pady=10)

def tell_joke(self):
    self.clear_window()
    joke = random.choice(DAD_JOKES)
    tk.Label(self.root, text="Dad Joke:", font=('Arial', 16, 'bold')).pack(pady=10)
    tk.Label(self.root, text=joke, font=('Arial', 14)).pack(pady=10)
    tk.Button(self.root, text="Spin the Wheel!", command=self.spin_the_wheel).pack(pady=10)

def spin_the_wheel(self):
    self.clear_window()
    option, effect = random.choice(WHEEL_OPTIONS)
    tk.Label(self.root, text="Spinning the wheel...", font=('Arial', 16, 'bold')).pack(pady=10)
    self.root.update()
    time.sleep(1)
    tk.Label(self.root, text=option, font=('Arial', 14, 'bold')).pack(pady=10)
    self.apply_wheel_effect(effect)
    tk.Button(self.root, text="Continue", command=self.next_round).pack(pady=10)

def next_round(self):
    self.round += 1
    self.current_question_in_round = 0
    self.play_round()
