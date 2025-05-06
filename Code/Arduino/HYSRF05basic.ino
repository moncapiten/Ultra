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

#define WAITTIME 100
#define TRIG 3
#define ECHO 2

void setup() 
{
  Serial.begin(115200);
  while (!Serial) delay(1);

  pinMode(ECHO,INPUT);
  pinMode(TRIG,OUTPUT);
  
  Serial.println("HY-SRF05 Ultrasound sensor");
}

void loop() 
{
  delay(WAITTIME);
  digitalWrite(TRIG,HIGH);
  delay(10);
  digitalWrite(TRIG,LOW);
  Serial.println(pulseIn(ECHO,HIGH));
}