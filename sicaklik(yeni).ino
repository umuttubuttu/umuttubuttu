#include <ESP8266WiFi.h>
#include <DHT.h>

// DHT11 pin bağlantısı
//#define DHTPIN 2           // DHT11 sensörünün bağlı olduğu pin (GPIO2)
#define DHTTYPE DHT11      // DHT11 sensörü
const int DHTPIN=D2;
DHT dht(DHTPIN, DHTTYPE);  // DHT sensörünü başlat

// Wi-Fi bilgileri
const char* ssid = "linksys";           // Wi-Fi ağınızın adı
const char* password = "baef2016";     // Wi-Fi şifreniz

// PHP sunucu bilgileri
const char* host = "192.168.1.102";         // PHP sunucusunun adresi
const char* path = "/veri_yolla.php";      // PHP dosyasının yolu

WiFiClient client;

void setup() {
  Serial.begin(115200);
  delay(10);

  // Wi-Fi'ye bağlan
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Bağlanıyor...");
  }
  Serial.println("Wi-Fi'ye bağlanıldı");

  dht.begin();  // DHT sensörünü başlat
}

void loop() {
  // Sıcaklık ve nem değerlerini oku
  float sıcaklık = dht.readTemperature();  
  float nem = dht.readHumidity();

  // Eğer okuma hatalıysa tekrar dene
  if (isnan(sıcaklık) || isnan(nem)) {
    Serial.println("Veri okunamadı!");
    return;
  }

  // Veriyi PHP sunucusuna gönder
  if (client.connect(host, 80)) {  
    String url = String(path) + "?sıcaklık=" + sıcaklık + "&nem=" + 10;
    client.print(String("GET ") + url + " HTTP/1.1\r\n" +
                 "Host: " + host + "\r\n" +
                 "Connection: close\r\n\r\n");
    delay(2000);  // 2 saniye bekle
  } else {
    Serial.println("Sunucuya bağlanılamadı!");
    Serial.println(sıcaklık);
  }
  delay(5000);  // Her 5 saniyede bir veri gönder
}
