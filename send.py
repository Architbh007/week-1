import serial
import time
import random
from datetime import datetime

ser = serial.Serial('COM5', 9600)  

def log_event(event):
    """Logs events with timestamps."""
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {event}")

while True:
    # Send a random number to the Arduino
    number_to_send = random.randint(1, 10)
    ser.write(f"{number_to_send}\n".encode())  # Send the number to Arduino
    log_event(f"Sent number to Arduino: {number_to_send}")

    # Wait for Arduino to respond
    while ser.in_waiting == 0:
        pass  # Waits until data is available

    # Read the response from Arduino
    response = ser.readline().decode('utf-8').strip()
    log_event(f"Received from Arduino: {response}")

    # Sleep for the number of seconds Arduino sends
    delay_time = int(response)
    log_event(f"Sleeping for {delay_time} seconds")
    time.sleep(delay_time)  # Sleep for the specified time
    log_event("Finished sleeping")
