import random, webbrowser, os, time, wikipedia, getpass
import pyautogui 

responses1 = ["Hi", "Hello", "hi", "hello", "How can I help you?"]
responses2 = ["bye", "Goodbye", "goodbye", "Bye"]
responses3 = ["How are you?", "how are you?", "how are you", "How Are You", "How Are You?", "How are you"]
search = ["Search", "search", "SEARCH"]
exit = ["exit", "Exit", "EXIT"]
game = ["game", "Game", "GAME", "start game", "Start Game", "start Game", "start Game"]
terminal = ["terminal", "Terminal", "TREMINAL"]
user = ["fine", "Fine", "FINE"]
ls = ["ls"]

def response1():
    return random.choice(responses1)
def response2():
    return random.choice(responses2)

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open_new_tab(url)

AI = "Max"
y = ": "
you = "(You)"
ai = "(AI)"





def mainTasK():
    while (True):
        i = input(you+y).lower()
        if i in (responses1):
           print (AI + ai + y + response1() +" " + "Master")
    
        elif i in (search):
            s = input("What do you want to search on google?:")
            search_google(s)
        
    
        elif i in (game):
    
            print("Starting game")
            # game starting
            import random
            
            board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            
            def display_board():
                print(board[0] + "|" + board[1] + "|" + board[2])
                print("-+-+-")
                print(board[3] + "|" + board[4] + "|" + board[5])
                print("-+-+-")
                print(board[6] + "|" + board[7] + "|" + board[8])
            
            def check_win(player):
                return ((board[0] == player and board[1] == player and board[2] == player) or
                        (board[3] == player and board[4] == player and board[5] == player) or
                        (board[6] == player and board[7] == player and board[8] == player) or
                        (board[0] == player and board[3] == player and board[6] == player) or
                        (board[1] == player and board[4] == player and board[7] == player) or
                        (board[2] == player and board[5] == player and board[8] == player) or
                        (board[0] == player and board[4] == player and board[8] == player) or
                        (board[2] == player and board[4] == player and board[6] == player))
            
            def player_move():
                while True:
                    try:
                        move = int(input("Enter your move (1-9): "))
                        if board[move-1] == " ":
                            board[move-1] = "X"
                            break
                        else:
                            print("That space is already taken. Try again.")
                    except ValueError:
                        print("Invalid input. Try again.")
            
            def ai_move():
                move = None
                for i in range(1, 10):
                    if board[i-1] == " ":
                        board[i-1] = "O"
                        if check_win("O"):
                            move = i
                            break
                        board[i-1] = " "
                if move is None:
                    for i in range(1, 10):
                        if board[i-1] == " ":
                            board[i-1] = "X"
                            if check_win("X"):
                                move = i
                                break
                            board[i-1] = " "
                if move is None:
                    while True:
                        move = random.randint(1, 9)
                        if board[move-1] == " ":
                            break
                board[move-1] = "O"
            
            while True:
                board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
                display_board()
                while True:
                    player_move()
                    display_board()
                    if check_win("X"):
                        print("You won!")
                        break
                    if " " not in board:
                        print("It's a tie!")
                        break
                    ai_move()
                    display_board()
                    if check_win("O"):
                        print("You lost!")
                        break
                play_again = input("Do you want to play again? (y/n): ")
                if play_again.lower() != "y":
                    break
        #game ending
        elif i in (terminal):
            #terminal start
            print("Starting Terminal")
            import subprocess
            
            while True:
                cmd = input('$ ')
                if cmd.lower() == 'exit':
                    break
                try:
                    result = subprocess.run(cmd.split(), capture_output=True, text=True)
                    print(result.stdout.strip())
                    if result.stderr:
                        print(result.stderr.strip())
                except FileNotFoundError:
                    print(f'{cmd}: command not found')
        #terminal end
    
        elif i in (responses3):
            print("I am fine ")
            fine = input("And you " + "Master" + y)
            if i in (user):
                print("I am happy to hear it :)")
            else:
                print("I am so sorry ")
            
        elif i in (responses2):
            print(AI + ai + y + response2() +" " + "Master")
            break
        elif i in (exit):
            break

        elif 'play music' in i:
            """Change the file path"""
            music_dir = ""
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir, song[0]))

        elif 'open instagram' in i:
            webbrowser.open_new_tab("https://www.instagram.com")
        
        elif 'open youtube' in i:
            webbrowser.open_new_tab("https://www.youtube.com")
        
        elif 'open zoro' in i:
            webbrowser.open_new_tab("https://zoro.to/home?source=pwa")
        
        elif 'open google' in i:
            webbrowser.open_new_tab("https://www.google.com")
        
        elif 'open chat gpt' in i:
            webbrowser.open_new_tab("https://chat.openai.com/chat")


        elif 'play video' in i:
            """Change the file path"""
            video_path = ""
            os.startfile(video_path)

        elif 'wikipedia' in i:
            print('Searching on wikipedia...')
            quray = i.replace("wikipedia", "")
            results = wikipedia.summary(quray, sentences = 3)
            print("Accoding to wikipedia")
            print(results)        
        
        elif 'let me control the pc with my hands' in i:
            print("Wait a second...")
            hands.main()

        else:
            print(AI + ai + y + "Error, command not found :( ")
            yes_no = input("Do you yant to search this on google(Y/n): ")
            if (yes_no=='n' or yes_no=='N'):
                continue
            else:
                search_google(i)
        
            
        

if __name__ == "__main__":
        mainTasK()
