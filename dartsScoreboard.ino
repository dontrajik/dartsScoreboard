#include <LiquidCrystal.h>
#include <IRremote.h>

const int RECV_PIN = 7;
boolean wtf = false;

String signal = "";
String input = "";

IRrecv irrecv(RECV_PIN);
decode_results results;

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
byte arrow[8] = {
  B00000,
  B00010,
  B00110,
  B01110,
  B01110,
  B00110,
  B00010,
  B00000,
};

boolean throwable(int thrown){
  int unthrowable[9] = {
    179, 178, 176, 175, 173, 172, 169, 166, 163    };
  if(thrown > 180){
    return false;
  }
  for(int i = 0; i < 9; i++){
    if(thrown == unthrowable[i]){
      return false;
    }
  }
  return true;
} 

void setup() {
  Serial.begin(9600);
  irrecv.enableIRIn();
  lcd.begin(16, 2);
  lcd.print("ENG 501 1 1    ");
  lcd.createChar(0, arrow);
  lcd.setCursor(15,0);
  lcd.write(byte(0));
  lcd.setCursor(0, 1);
  lcd.print("HUN 501 1 1     ");
}

void loop() {
  wtf = false;
  signal = "";
  input = "";
  while(signal != "ENTER"){
    if (irrecv.decode(&results)) {

      signal = "";
      switch (results.value) {
      case 0xE0E020DF:
        signal = "1";
        break;
      case 0xE0E0A05F:
        signal = "2";
        break;
      case 0xE0E0609F:
        signal = "3";
        break;
      case 0xE0E010EF:
        signal = "4";
        break;
      case 0xE0E0906F:
        signal = "5";
        break;
      case 0xE0E050AF:
        signal = "6";
        break;
      case 0xE0E030CF:
        signal = "7";
        break;
      case 0xE0E0B04F:
        signal = "8";
        break;
      case 0xE0E0708F:
        signal = "9";
        break;
      case 0xE0E08877:
        signal = "0";
        break;
      case 0xE0E016E9:
        signal = "ENTER";
        break;
      case 0xE0E01AE5:
        signal = "BACK";
        break;
      case 0xE0E0B44B:
        signal = "EXIT";
        break;
      default:
        wtf = true;
        break;
      }
      Serial.print(signal);
      if (!wtf and (signal !="ENTER")) {
        if(input.length() < 3){
          input = input + signal;
          lcd.setCursor(12,1);
          lcd.print("   ");
          lcd.setCursor(12,1);
          lcd.print(input);
        }
        signal = "";
      }
      delay(100);
      irrecv.resume();
    }
  }
  input = input.substring(0,3);
  if((input != "")and(throwable(input.toInt()))){
    lcd.setCursor(12,0);
    lcd.print("   ");
    lcd.setCursor(12,0);
    lcd.print(input);
  }
  Serial.println(input);
  input = "";
  lcd.setCursor(12,1);
  lcd.print("    ");
  lcd.setCursor(12,1);
}








