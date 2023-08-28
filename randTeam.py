import random
import tkinter as tk
from tkinter import messagebox


class TeamNameSelectionGUI:
    def __init__(self, teams):
        self.teams = teams
        self.team_name = None

        self.root = tk.Tk()
        self.root.title("Team Name Selection")
        self.root.geometry("400x300")

        self.title_label = tk.Label(self.root, text="Team Name Selection for Arduino", font=("Arial", 36, "bold"))
        self.title_label.pack(pady=20)

        self.team_label = tk.Label(self.root, text="", font=("Arial", 48), anchor="center")
        self.team_label.pack()

        self.next_button = tk.Button(self.root, text="Next", font=("Arial", 14), command=self.pick_next_team)
        self.next_button.pack(pady=20)

        self.root.mainloop()

    def pick_next_team(self):
        if not self.teams:
            messagebox.showinfo("Team Name Selection", "All team names have been used. Please restart the program.")
            self.root.destroy()
            return

        self.team_name = random.choice(self.teams)
        self.teams.remove(self.team_name)
        self.team_label.config(text=f"{self.team_name}")


def main():
    teams = [
        "Xi Jinping", "Snicker", "Botania", "Hephaestus", "Tubelight",
        "Project Insight", "Mars", "Nuclear HellHounds", "Team Shark",
        "Astroworld", "Agri Buddy"
    ]

    TeamNameSelectionGUI(teams)


if __name__ == "__main__":
    main()
