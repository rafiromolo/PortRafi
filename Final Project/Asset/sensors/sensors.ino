#include <FastLED.h>

#define PIN_RGB     12
#define PIN_BL      11
#define NUM_LEDS    8
#define NUM_BL      16
#define BRIGHTNESS  512
#define BRIGHT_BL   32
#define LED_TYPE    WS2812B
#define COLOR_ORDER GRB

CRGB leds[NUM_LEDS]; CRGB bl[NUM_BL];

#define UPDATES_PER_SECOND 100

int x;
const int PIN_S0 = 2; const int PIN_S1 = 3; const int PIN_S3 = 4; const int PIN_S2 = 5; const int PIN_TCSOUT = 8;

void setup() {
  FastLED.addLeds<LED_TYPE, PIN_RGB, COLOR_ORDER>(leds, NUM_LEDS); FastLED.setBrightness(BRIGHTNESS);
  FastLED.addLeds<LED_TYPE, PIN_BL, COLOR_ORDER>(bl, NUM_BL); FastLED.setBrightness(BRIGHT_BL);
  
  pinMode(PIN_S0, OUTPUT); pinMode(PIN_S1, OUTPUT); pinMode(PIN_S2, OUTPUT); pinMode(PIN_S3, OUTPUT); pinMode(PIN_TCSOUT, INPUT);
  pinMode(PIN_RGB, OUTPUT);

  digitalWrite(PIN_S0, HIGH); digitalWrite(PIN_S1, LOW);
  
  Serial.begin(9600); Serial.setTimeout(1);
}

void loop() {
  int dataRC, dataGC, dataBC, dataRI, dataGI, dataBI;
  x = Serial.readString().toInt();
  delay(200);
  if(x == 1) {
    leds[2] = CRGB(255, 0, 0); leds[3] = CRGB(255, 0, 0); leds[4] = CRGB(255, 0, 0);
    leds[5] = CRGB(255, 0, 0); leds[6] = CRGB(255, 0, 0);  FastLED.show();
    dataRC = redC_value(); Serial.println(dataRC);
  }
  else if(x == 2) {
    leds[2] = CRGB(0, 255, 0); leds[3] = CRGB(0, 255, 0); leds[4] = CRGB(0, 255, 0);
    leds[5] = CRGB(0, 255, 0); leds[6] = CRGB(0, 255, 0); FastLED.show();
    dataGC = greenC_value(); Serial.println(dataGC);
  }
  else if(x == 3) {
    leds[2] = CRGB(0, 0, 255); leds[3] = CRGB(0, 0, 255); leds[4] = CRGB(0, 0, 255);
    leds[5] = CRGB(0, 0, 255); leds[6] = CRGB(0, 0, 255); FastLED.show();
    dataBC = blueC_value(); Serial.println(dataBC);
  }
  else if(x == 4) {
    bl[0] = CRGB(255, 255, 255); bl[1] = CRGB(255, 255, 255); bl[2] = CRGB(255, 255, 255); bl[3] = CRGB(255, 255, 255);
    bl[4] = CRGB(255, 255, 255); bl[5] = CRGB(255, 255, 255); bl[6] = CRGB(255, 255, 255); bl[7] = CRGB(255, 255, 255);
    bl[8] = CRGB(255, 255, 255); bl[9] = CRGB(255, 255, 255); bl[10] = CRGB(255, 255, 255); bl[11] = CRGB(255, 255, 255);
    bl[12] = CRGB(255, 255, 255); bl[13] = CRGB(255, 255, 255); bl[14] = CRGB(255, 255, 255); bl[15] = CRGB(255, 255, 255);
    FastLED.show();
  }
}

int redC_value(){
  digitalWrite(PIN_S2, LOW); digitalWrite(PIN_S3, LOW);
  int pulse_len = pulseIn(PIN_TCSOUT, LOW);
  int color = map(pulse_len, 10, 140, 255, 0);
  if (color > 255) {
    color = 255;
  }
  if (color < 0) {
    color = abs(color);
  }
  return color;
}

int greenC_value(){
  digitalWrite(PIN_S2, HIGH); digitalWrite(PIN_S3, HIGH);
  int pulse_len = pulseIn(PIN_TCSOUT, LOW);
  int color = map(pulse_len, 21, 141, 255, 0);
  if (color > 255) {
    color = 255;
  }
  if (color < 0) {
    color = abs(color);
  }
  return color;
}

int blueC_value(){
  digitalWrite(PIN_S2, LOW); digitalWrite(PIN_S3, HIGH);
  int pulse_len = pulseIn(PIN_TCSOUT, LOW);
  int color = map(pulse_len, 15, 133, 255, 0);
  if (color > 255) {
    color = 255;
  }
  if (color < 0) {
    color = abs(color);
  }
  return color;
}
