import os

def restart_android_device():
    # Check if ADB is installed
    if os.system("adb version") != 0:
        print("ADB is not installed or not in PATH. Please install ADB and try again.")
        return

    # Restart the device
    os.system("adb reboot")

    print("Android device has been restarted.")

# Call the function to restart the Android device
restart_android_device()