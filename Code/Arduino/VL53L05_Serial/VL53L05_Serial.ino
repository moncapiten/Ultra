/* -------------------------------------------------------------
 *  VL52L05basic
 * -------------------------------------------------------------
 * SteRod2024
 *
 * Just a minor adatpation from the library examples
 *
 */
 
#define STR_BUFFER_MAX  100
#include "Adafruit_VL53L0X.h"
Adafruit_VL53L0X lox = Adafruit_VL53L0X();
String inputString;
void commandParser(String);

void setup() 
{
  Serial.begin(115200);
  while (! Serial) delay(1);
  
  if (!lox.begin()) 
  {
    Serial.println(F("Failed to boot VL53L0X"));
    while(1);
  }
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
    VL53L0X_RangingMeasurementData_t measure;
    lox.rangingTest(&measure, false); 
    if (measure.RangeStatus != 4) 
    {  
      // phase failures have incorrect data
      Serial.println(measure.RangeMilliMeter);
      } else Serial.println("-1");
  } else Serial.println("??");
}