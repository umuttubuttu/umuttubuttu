<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RGB Ledi - LED Kontrol</title>
</head>
<body>
    <h2>RGB Ledi - LED Kontrol</h2>
    <form method="post">
        <button type="submit" name="ac">Kırmızı Aç</button>
        <button type="submit" name="kapat">Kırmızı Kapat</button>
    </form>
    <?php
    $esp_ip = "http://192.168.1.100"; // NodeMCU'nun IP adresini buraya girin
    if (isset($_POST['ac'])) {
        file_get_contents("$esp_ip/led/on");
        echo "<p>LED Açıldı</p>";
    } elseif (isset($_POST['kapat'])) {
        file_get_contents("$esp_ip/led/off");
        echo "<p>LED Kapandı</p>";
    }
    ?>
</body>
</html>
