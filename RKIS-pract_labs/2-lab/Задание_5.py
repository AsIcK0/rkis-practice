class Construct:
    def __init__(self, game_title="-", studio="-"):
        self.game_title = game_title
        self.studio = studio
        print(f"Конструкт: {self.game_title} от {self.studio}")
    def __del__(self):
        print(f"Удаление игры из конструкта: {self.game_title} от {self.studio}")
    def show_info(self):
        for game in games:
            print(f"Название: {self.game_title}")
            print(f"Студия: {self.studio}")
if __name__ == "__main__":
    games = [
        Construct("War Thunder", "Gaijin"),
        Construct("Hollow Knight", "Team Cherry")]
    print("\nИгра 1:")
    games[0].show_info()
    print("\nИгра 2:")
    games[1].show_info()
