from talk_module import *
import webbrowser, random, os

init()
goodbye = False
try:
    while True:
        clear()
        user = hear()

        match user:
            case _ if user.startswith("my name is "):
                name_save = user.replace("my name is ", "")
                with open("data.json", "r") as file:
                    data = json.load(file)
                data["name"] = name_save
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
                speak(
                    f"saved, your name is {name_save}",
                    f"{Fore.GREEN}saved:{Fore.RESET} your name [{Fore.CYAN}{name_save}{Fore.RESET}]",
                )

            case "hello" | "hi" | "hey":
                choose = ["hey", "hi", "hello"]
                speak(random.choice(choose) + " " + data["name"])

            case "good bye" | "bye" | "goodbye":
                raise KeyboardInterrupt("bye")

            case _ if user.startswith("search "):
                user = user.replace("search ", "")
                user = user.replace(" ", "+")
                webbrowser.open("https://google.com/search?q=" + user)
                # remove "search" so we can have only the word
            case "help":
                speak(
                    "say (command) for commands list:\n"
                    "you can also change your vosk model in (data.json) file"
                )
            case "command":
                speak(
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
                speak("i am help-star and i want to help you")
            case "version":
                speak(data["vers"])
            case 'joke':
                joke=["why chickens love pancake...idon't know"]
                speak(random.choice(joke))
            case 'what is my name':
                speak(f'your name is {data["name"]}')
except KeyboardInterrupt:
    try:
        print(Fore.RESET, end="")
        choose = ["bye", "goodbye"]
        speak(random.choice(choose) + " " + data["name"])
        goodbye = True
    # handle 'keyboardinterrupt' during exiting mid-speech
    except:  # 2 keyboardinterupt
        pass
except AttributeError:  # vosk
    if goodbye == True:
        pass
    else:
        print("something wrong with model")
# pttsx3 (RuntimeError: run loop already started)
except RuntimeError:
    pass
except:
    print("error something is wrong")
finally:
    if goodbye == True:
        exit()
