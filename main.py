from talk_module import *
from random import choice
from webbrowser import open

goodbye = 0
# list
list_hello = ["hello", "hi", "hey"]
list_bye = ["bye", "goodbye", "good bye", "see you later"]
# start loading
try:
    hear = Hear()
    speak = Speak()
    print("done")
    clear()

    while True:
        user = hear.start()

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
                open("https://google.com/search?q=" + user)

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
                    "search [---] : for searching [---]\n"
                    "help : for help\n"
                    "command : for commands list\n"
                    "my name is [---] : for saving your name"
                )

            case "what is your name" | "who are you":
                speak.start("i am help-star and i want to help you")

            case "version":
                speak.start(hear.data["vers"])

            case "joke":
                joke = ["why chickens love pancake...idon't know"]
                speak.start(choice(joke))

            case "what is my name":
                speak.start(f"your name is {hear.data['name']}")

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
