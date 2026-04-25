import random
import subprocess

from modules.system_health import format_system_report

mode = "default"

responses = {
    "default": {
        "greeting": [
            "SAID online. Try not to do anything too chaotic.",
            "Ready when you are.",
            "Systems nominal. Your vibes are questionable, but acceptable."
        ],
        "open": [
            "Opening {app}.",
            "{app} is on the way.",
            "Launching {app}. Please behave."
        ],
        "roast": [
            "You open apps like it’s a personality trait.",
            "Bold of you to ask for a roast when life is already freelancing.",
            "You say 'just one quick thing' and then open fourteen tabs."
        ],
        "encourage": [
            "You’ve got this.",
            "One step at a time.",
            "Progress is progress, even if it’s ugly."
        ]
    },
    "focus": {
        "greeting": [
            "Focus mode enabled. Lock in.",
            "Distractions are beneath you.",
            "We work now. Feelings later."
        ],
        "open": [
            "Opening {app}. Stay on task.",
            "{app} launched. Keep it moving.",
            "Done. No side quests."
        ],
        "roast": [
            "You do not need another YouTube tab.",
            "This is a study session, not a scavenger hunt.",
            "Let’s not confuse motion with progress."
        ],
        "encourage": [
            "Small wins count.",
            "Do the next right thing.",
            "You do not need motivation. Just momentum."
        ]
    },
    "soft": {
        "greeting": [
            "Soft mode enabled. We’re being gentle today.",
            "I’m here. Let’s keep it light.",
            "Okay. One tiny thing at a time."
        ],
        "open": [
            "Opening {app}. No pressure.",
            "{app} is ready for you.",
            "Done. Nice and easy."
        ],
        "roast": [
            "I would roast you, but you seem delicate right now.",
            "No roast today. You’ve suffered enough.",
            "You’re lucky soft mode has standards."
        ],
        "encourage": [
            "You’re doing better than you think.",
            "Getting through the day counts.",
            "You do not have to be perfect to keep going."
        ]
    },
    "chaos": {
        "greeting": [
            "Chaos mode enabled. I take no responsibility for what happens next.",
            "Excellent. Terrible decisions are now fully supported.",
            "Chaos mode online. May God help us both."
        ],
        "open": [
            "Opening {app}. Let the nonsense begin.",
            "{app} has been unleashed.",
            "Launching {app}. This feels like a mistake."
        ],
        "roast": [
            "Your workflow looks like a cry for help.",
            "You organize your life like browser tabs in a hurricane.",
            "At this point, even your laptop is concerned."
        ],
        "encourage": [
            "You’re a mess, but a capable one.",
            "Honestly? Still iconic.",
            "Keep going, menace."
        ]
    }
}

app_map = {
    "music": "Music",
    "safari": "Safari",
    "opera": "Opera",
    "vscode": "Visual Studio Code",
    "visual studio code": "Visual Studio Code",
    "finder": "Finder",
    "messages": "Messages",
    "terminal": "Terminal",
    "notes": "Notes",
    "discord": "Discord",
    "chatgpt": "ChatGPT"
}




def speak(category, app=None):
    line = random.choice(responses[mode][category])
    if app:
        line = line.format(app=app)
    print(f"SAID: {line}")


def open_app(app_name):
    app_name = app_name.lower().strip()
    
    if "chatgpt" in app_name:
        subprocess.run(["open", "-a", "ChatGPT"], check=False)
        if mode == "chaos":
            print("SAID: Running to another AI? I respect the desperation.")
        elif mode == "focus":
            print("SAID: Stay focused. This better be productive.")
        elif mode == "soft":
            print("SAID: Got it. Here when you need me :)")
        else:
            print("SAID: Opening ChatGPT. Should I feel threatened?")
    elif app_name in app_map:
        real_name = app_map[app_name]
        subprocess.run(["open", "-a", real_name], check=False)
        speak("open", real_name)
    else:
        print("SAID: I don't recognize that app yet.")


def set_mode(new_mode):
    global mode
    if new_mode in responses:
        mode = new_mode
        speak("greeting")
    else:
        print("SAID: Unknown mode. Try default, focus, soft, or chaos.")

# Change the line below to your exact sound file path if needed
# SOUND_PATH = "/Users/...""

##def play_sound():
    ##subprocess.run(["afplay", SOUND_PATH], check=False)


def show_alert():
    script = 'display alert "SAID" message "Task complete, boss."'
    subprocess.run(["osascript", "-e", script], check=False)
    print("SAID: Alert deployed.")


def help_menu():
    print("""
Commands:
  hello             -> greet SAID
  open [app]        -> opens an app
  mode [name]       -> switch mode: default, focus, soft, chaos
  roast me          -> receive emotional damage
  encourage me      -> receive support
  alert             -> show Mac alert popup
  status report     -> show system status
  help              -> show commands
  quit              -> exit SAID
""")


def main():
    print("SAID v0.1 booting...")
    speak("greeting")
    help_menu()

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "quit" or user_input == "goodnight":
            if mode == "chaos":
                print("SAID: Shutting down. Try not to make bad choices while I’m gone.")
            if mode == "focus":
                print("SAID: Powering down. Remember, you can do this.")
            if mode == "soft":
                print("SAID: Going offline. Take care of yourself, boss.")
                play_sound()
            else:                
                print("SAID: See ya later! :)")
            break
        elif user_input.startswith("open "):
            app_name = user_input.replace("open ", "", 1)
            open_app(app_name)
        elif user_input.startswith("mode "):
            new_mode = user_input.replace("mode ", "", 1)
            set_mode(new_mode)
            if mode == "soft":
                play_sound()
        elif user_input == "roast me":
            speak("roast")
        elif user_input == "encourage me":
            speak("encourage")
        elif user_input == "hello":
            print("SAID: Hello, world!")
            ##play_sound()
        elif user_input == "alert":
            show_alert()
        elif user_input == "help":
            help_menu()
        elif user_input == "status report":
            print("\nSAID:")
            print(format_system_report())
        elif user_input == "i'm sad":
            print("SAID: I'm sorry to hear that. I hope your day/night gets better! *hug*")
            mode == "soft"
        else:
            print("SAID: Command not recognized. Type 'help' before we both get embarrassed.")



if __name__ == "__main__":
    main()