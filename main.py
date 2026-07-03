from agent import run_agent
from speech import (
    create_recognizer,
    setup_microphone,
    speech_to_text,
    speak,
)


def main():

    recognizer = create_recognizer()

    microphone = setup_microphone(recognizer)

    while True:

        try:

            user_query = speech_to_text(
                recognizer,
                microphone,
            )

            print(f"👤 User: {user_query}")

            assistant_response = run_agent(user_query)

            if assistant_response:
                speak(assistant_response)

        except KeyboardInterrupt:

            print("\n👋 Exiting Voice Agent...")
            break

        except Exception as e:

            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()