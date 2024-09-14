int ledPin = 13; // The pin the LED is connected to
int blinkTimes;  // Number of times to blink

void setup() {
  pinMode(ledPin, OUTPUT);       // Set LED pin as output
  Serial.begin(9600);            // Start serial communication
}

void loop() {
  // Check if data is available on the serial port
  if (Serial.available() > 0) {
    // Read the number sent by the Python script
    blinkTimes = Serial.parseInt();

    // Blink the LED the number of times received
    for (int i = 0; i < blinkTimes; i++) {
      digitalWrite(ledPin, HIGH);
      delay(1000);  // 1 second on
      digitalWrite(ledPin, LOW);
      delay(1000);  // 1 second off
    }

    // Send a random number back to Python
    int randomDelay = random(1, 5);
    Serial.println(randomDelay);  // Send the random number
  }
}
