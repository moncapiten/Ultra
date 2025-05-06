/* -------------------------------------------------------------
 *  HY-SFR05basic
 * -------------------------------------------------------------
 * SteRod2024
 *
 * The chip has no I2C, this requires an asynchronous control
 * of a couple of digital lines. To standardize everything,
 * we will use standard SDA and SCL as the digital control lines.
 *
 * D3 => TRIG
 * D2 => ECHO
 *
  * The reading of the sensor status will be done by the builtin
 * function pulseIn()
 *
 * Expectations...
 *
 * D[mm] = delay[usec]*0.17
 *
 *   100      17mm
 *   200      34mm
 *   300      51mm
 *   600      10cm
 *  1000      20cm
 *  3000      50cm
 *  6000       1m
 *
 */

#define STR_BUFFER_MAX  100
#define TRIG 3
#define ECHO 2

String inputString;
void commandParser(String);

void setup() 
{
  inputString.reserve(STR_BUFFER_MAX);
  Serial.begin(115200);
  while (!Serial) delay(1);
    
  pinMode(ECHO,INPUT);
  pinMode(TRIG,OUTPUT);

  Serial.println("HY-SRF05 Ultrasound sensor");
  Serial.println("Serial version");
}

void loop() 
{
  // Main serial loop
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if ((inChar == '\r')|(inChar == '\n')) {
      if (inputString.length()>0) commandParser(inputString);
      inputString = "";
    }
    else if (inputString.length()<STR_BUFFER_MAX) inputString += inChar;
  }
}

void commandParser(String message)
{
  message.toUpperCase();
  String cmd = message.substring(0,message.indexOf(" "));
  String value = "";

  /* Split the string into a command + value */
  if (message.indexOf(" ")>0) 
    value = message.substring(message.indexOf(" ")+1);
  cmd.trim();
  value.trim();

/* -[READ?]----------------------------------------------------------- */
  if (cmd == "READ?") {
    digitalWrite(TRIG,HIGH);
    delay(10);
    digitalWrite(TRIG,LOW);
    Serial.println(pulseIn(ECHO,HIGH));
  } else Serial.println("??");
}