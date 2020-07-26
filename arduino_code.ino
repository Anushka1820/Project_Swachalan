const int ledPin = 3;
const int ledPin1 = 4;
const int ledPin2 = 5;
const int ledPin3 = 6;// the pin that the LED is attached to
int incomingByte;      // a variable to read incoming serial data into

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
   pinMode(ledPin1, OUTPUT);
    pinMode(ledPin2, OUTPUT);
     pinMode(ledPin3, OUTPUT);
  
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    if (incomingByte == 'H') {
      digitalWrite(ledPin, HIGH);
      digitalWrite(ledPin1, HIGH);
       digitalWrite(ledPin2, HIGH);
      digitalWrite(ledPin3, HIGH);
    }
    // if it's an L (ASCII 76) turn off the LED:
   else if (incomingByte == 'L') {
      digitalWrite(ledPin, LOW);
      digitalWrite(ledPin1, LOW);
       digitalWrite(ledPin2, HIGH);
      digitalWrite(ledPin3, HIGH);
    }
    else if (incomingByte == 'K') {
      digitalWrite(ledPin, HIGH);
      digitalWrite(ledPin1, HIGH);
       digitalWrite(ledPin2,LOW);
      digitalWrite(ledPin3, LOW);
      
  }
   else if (incomingByte == 'M') {
      digitalWrite(ledPin2,LOW);
      digitalWrite(ledPin3, LOW);
       digitalWrite(ledPin,LOW);
      digitalWrite(ledPin1, LOW);
 }
 
  } 
} 
