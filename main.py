from talk_module import *
from random import choice
from webbrowser import open as search
from keyboard import block_key, unblock_key
from joke.main import joke
block_key("ctrl")#stop the vosk crashing
goodbye = 0
# list
list_hello = ("hello", "hi", "hey")
list_bye = ("bye", "goodbye", "good bye", "see you later")
# start loading
hear = Hear()
speak = Speak()
unblock_key("ctrl")#done
try:
    while True:
        clear()
        if hear.data["speech-mode"] is True:
            user = hear.start()
        else:
            user = input("--")
        match user:
            case _ if user.startswith("my name is "):
                name_save = user.replace("my name is ", "")
                hear.data["name"] = name_save
                with open("data.json", "w") as file:
                    dump(hear.data, file, indent=4)
                speak.start(
                    f"saved, your name is {name_save}",
                    f"{Fore.GREEN}saved:{Fore.RESET} your name [{Fore.CYAN}{name_save}{Fore.RESET}]",
                )

            case _ if user in list_hello:
                speak.start(choice(list_hello) + " " + hear.data["name"])

            case _ if user in list_bye:
                raise KeyboardInterrupt("leave")

            case _ if user.startswith("search "):
                user = user.replace("search ", "")
                user = user.replace(" ", "+")
                search("https://google.com/search?q=" + user)

            case "help":
                speak.start(
                    "say (command) for commands list:\n"
                    "you can also change your vosk model in (data.json) file"
                )

            case "command":
                speak.start(
                    "you can say:\n"
                    "hello , hi , hey : will say hello back to you\n"
                    "bye , goodbye , good bye : for exit\n"
                    "you can also press (crlt+c) for exit too\n"
                    "search (name) : for searching (name)\n"
                    "help : for help\n"
                    "command : for commands list\n"
                    "my name is (name) : for saving your name"
                )

            case "what is your name" | "who are you":
                speak.start("i am help star , and i want to help you")

            case "version":
                speak.start(hear.data["vers"])

            case "joke":
                speak.start(choice(joke))

            case "what is my name":
                speak.start(f"your name is {hear.data['name']}")
            case "speech mode":
                if hear.data["speech-mode"] == False:
                    hear.data["speech-mode"] = True
                else:
                    hear.data["speech-mode"] = False

                with open("data.json", "w") as f:
                    dump(hear.data, f, indent=4)
except KeyboardInterrupt:
    try:
        print(Fore.RESET, end="")
        speak.start(choice(list_bye) + " " + hear.data["name"])
        goodbye = 1
    except:
        pass
except AttributeError:
    if goodbye == 1:
        pass
    else:
        print("something wrong with model")
except RuntimeError:
    pass
except:
    print("error something is wrong")
finally:
    if goodbye == 1:
        exit()
