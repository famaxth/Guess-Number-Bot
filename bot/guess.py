import random


class GuessGame: 
    random_number = 0
    number_of_tries = 0

    def start_game(self):
        self.random_number = random.randrange(1, 11)
        self.number_of_tries = 5
        return " New game started. You have " + str(self.number_of_tries) + " tries"

    def show_answer(self):
        return "Correct answer is: " + str(self.random_number)

    def guess_number(self, guessed_number):
        if self.isPlayable():
            self.number_of_tries = self.number_of_tries - 1
            if guessed_number < self.random_number:
                return "The entered number is less than secret number. You have " + str(self.number_of_tries) + " tries left."
            elif guessed_number > self.random_number:
                return "The entered number is greater than secret number You have " + str(self.number_of_tries) + " tries left."
            else:
                self.number_of_tries = 0
                self.user_won = True
                return True
        else:
            return False

    def isPlayable(self):
        return self.number_of_tries > 0
