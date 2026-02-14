#include <WiFi.h>
#include <HTTPClient.h>

const int phPin = 34;
const int tdsPin = 35;

String ssid = ""; String pass = "";

void getWifi() {
  Serial.println("\n--- Water Monitor Setup ---");
  Serial.println("SSID:"); while(Serial.available() == 0){}
  ssid = Serial.readStringUntil('\n'); ssid.trim();
  Serial.println("Pass:"); while(Serial.available() == 0){}
  pass = Serial.readStringUntil('\n'); pass.trim();
}

void setup() {
  Serial.begin(115200);
  getWifi();
  WiFi.begin(ssid.c_str(), pass.c_str());
  while(WiFi.status() != WL_CONNECTED){ delay(500); Serial.print("."); }
}

void loop() {
  float phVal = analogRead(phPin) * (5.0 / 4095.0) * 3.5; // Basic pH scaling
  float tdsVal = analogRead(tdsPin) * (5.0 / 4095.0) * 0.5 * 1000; // Basic TDS scaling

  HTTPClient http;
  http.begin("http://your-water-app.com/update");
  http.addHeader("Content-Type", "application/json");
  String payload = "{\"ph\":" + String(phVal) + ",\"tds\":" + String(tdsVal) + "}";
  http.POST(payload);
  http.end();
  
  delay(5000);
}
