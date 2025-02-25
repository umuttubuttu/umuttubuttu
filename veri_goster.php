<?php
// Veritabanı bağlantı bilgileri
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "sensor_veri";

// Veritabanı bağlantısını kur
$conn = new mysqli($servername, $username, $password, $dbname);

// Bağlantı hatası kontrolü
if ($conn->connect_error) {
    die("Bağlantı hatası: " . $conn->connect_error);
}

// Verileri al
$sql = "SELECT * FROM veriler ORDER BY zaman DESC LIMIT 10";
$result = $conn->query($sql);

// HTML sayfasını başlat
echo "<h1>Sıcaklık ve Nem Verileri</h1>";
echo "<table border='1'>
        <tr>
            <th>ID</th>
            <th>Sıcaklık</th>
            <th>Nem</th>
            <th>Zaman</th>
        </tr>";

// Verileri tablo olarak göster
if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo "<tr>
                <td>" . $row["id"] . "</td>
                <td>" . $row["sıcaklık"] . "</td>
                <td>" . $row["nem"] . "</td>
                <td>" . $row["zaman"] . "</td>
              </tr>";
    }
    echo "</table>";
} else {
    echo "Veri bulunamadı.";
}

// Bağlantıyı kapat
$conn->close();
?>
