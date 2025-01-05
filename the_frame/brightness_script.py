import os
import asyncio
import urllib3

# Suppress insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from samsungtvws.async_art import SamsungTVAsyncArt
from samsungtvws import exceptions

# Environment Variables
TV_IP = os.getenv("TV_IP", "192.168.1.33")
PORT = int(os.getenv("PORT", 8002))

# Paths for token and brightness files within /share
TOKEN_FILE = "/share/samsung_token.txt"
BRIGHTNESS_OUTPUT_FILE = "/share/brightness.txt"

async def main():
    print(f"Starting Samsung Frame Add-on with TV_IP: {TV_IP} and PORT: {PORT}")
    print(f"Using TOKEN_FILE: {TOKEN_FILE}")
    
    # Initialize the SamsungTVAsyncArt instance
    tv = SamsungTVAsyncArt(
        host=TV_IP,
        port=PORT,
        token_file=TOKEN_FILE,  # Handles token generation if not present
    )
    
    try:
        # Start listening for token authorization if needed
        await tv.start_listening()
        print("WebSocket connection established.")
        
        # Check if the TV supports the required APIs
        if await tv.supported():
            print("TV reports: Art Mode is supported.")
        else:
            print("TV reports: Art Mode is NOT supported.")
            return
        
        # Connect to the TV
        try:
            await tv.connect()
            print("Connected to the Samsung Frame TV.")
        except Exception as e:
            print(f"Failed to connect to the Samsung Frame TV: {e}")
            return
        
        # Retrieve current brightness
        try:
            current_brightness = await tv.get_brightness()
            print(f"Current brightness: {current_brightness}")
        except Exception as e:
            print(f"Failed to retrieve brightness: {e}")
            return
        
        # Write the brightness value to brightness.txt
        try:
            with open(BRIGHTNESS_OUTPUT_FILE, "w") as file:
                file.write(str(current_brightness))
            print(f"Brightness value saved to {BRIGHTNESS_OUTPUT_FILE}.")
        except Exception as e:
            print(f"Failed to write brightness to file: {e}")
            return
    
    except exceptions.ConnectionFailure as e:
        print(f"ConnectionFailure: {e}")
    except exceptions.ResponseError as e:
        print(f"ResponseError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Cleanly close the websocket connection
        try:
            await tv.close()
            print("Connection closed.")
        except Exception as e:
            print(f"Failed to close connection: {e}")

if __name__ == "__main__":
    asyncio.run(main())
