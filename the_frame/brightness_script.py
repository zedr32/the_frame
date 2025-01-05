import os
from samsungtvws.art import SamsungTVArt

def main():
    # Read configuration from environment variables
    TV_IP = os.getenv("TV_IP", "192.168.1.33")
    TOKEN_FILE = os.getenv("TOKEN_FILE", "/config/samsung_token.txt")

    tv = SamsungTVArt(
        host=TV_IP,
        port=8002,
        token_file=TOKEN_FILE,
        name="BrightnessScript"
    )

    # Check if token file exists; if not, generate token
    if not os.path.exists(TOKEN_FILE):
        print(f"Token file '{TOKEN_FILE}' not found. Attempting to generate a new token...")
        try:
            tv.open()  # This should initiate token generation
            print("Token generated and saved successfully.")
        except Exception as e:
            print(f"Failed to generate token: {e}")
            return

    # Open the WebSocket connection
    tv.open()
    print("Connected to The Frame TV.")

    # Read the current brightness
    current_brightness = tv.get_brightness()
    print(f"Current brightness: {current_brightness}")

    # Write to a text file in the config directory
    brightness_file = "/config/brightness.txt"
    with open(brightness_file, "w") as file:
        file.write(str(current_brightness))

    print(f"Brightness value saved to {brightness_file}.")

    # Close the connection
    tv.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()
