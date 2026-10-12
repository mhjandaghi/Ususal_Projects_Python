import random
class BingoGame:
    player_list = []
    def __init__(self):
        self.name = input("Enter ur name: ")
        self.__rand_num = random.randint(0,10)
        self.__guess_left = 3
        self.__win_state = False
        self.player_list.append(self)
        
    def check_answer(self):
        answer = int(input(f"\n{self.name} ,Enter ur guess: "))
        if answer > self.__rand_num:
            print( "choose lower num")
        if answer < self.__rand_num:
            print( "choose higher num")
        else:
            print("Bingo!")
            self.__win_state = True
            
        self.__set_guess_left()
        print(f"{self.__guess_left} Guesses Left.")
        
    def __set_guess_left(self):
        self.__guess_left -= 1
            
    def has_guess_left(self):
        if self.__guess_left > 0:
            return True
        return False   
        
    def has_won(self):
        return self.__win_state
    
    @classmethod
    def game_has_winner(cls):
        if any( player.has_won() for player in cls.player_list):
            return True
        return False
    
    
class GameController:
    def __init__(self):
        while True:
            for player in BingoGame.player_list:
                if not player.has_won() and player.has_guess_left():
                    player.check_answer()
                else:
                    break
            if BingoGame.game_has_winner():
                break
        
        
if __name__ == "__main__":
    while True:
        order = input("What do u want to do?\norder:")
        if order == 'add':
            BingoGame()
        elif order == 'start':
            GameController()
        elif order == 'exit':
            break