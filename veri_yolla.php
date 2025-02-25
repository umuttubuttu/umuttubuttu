<?php
// Veritabanı bağlantı bilgileri
$servername = "localhost"; // Sunucu
$username = "root";        // MySQL kullanıcı adı
$password = "";            // MySQL şifresi
$dbname = "sensor_veri";   // Veritabanı adı

// Veritabanı bağlantısını kur
$conn = new mysqli($servername, $username, $password, $dbname);

// Bağlantı hatası kontrolü
if ($conn->connect_error) {
    die("Bağlantı hatası: " . $conn->connect_error);
}

// Sıcaklık ve nem verisini al
$sıcaklık = $_GET['sıcaklık'];
$nem = $_GET['nem'];

// SQL sorgusunu hazırlayın
$sql = "INSERT INTO veriler (sıcaklık, nem) VALUES ($sıcaklık, $nem)";

// Sorguyu çalıştır
if ($conn->query($sql) === TRUE) {
    echo "Veri başarıyla kaydedildi.";
} else {
    echo "Hata: " . $sql . "<br>" . $conn->error;
}

// Bağlantıyı kapat
$conn->close();
?>
