<?php
// Verifica se as variáveis de usuário e senha estão vazias
if (empty($_POST['user-name']) || empty($_POST['password'])) {
    header('Location: login.php');
    exit;
}

$user = $_POST['user-name'];
$senha = $_POST['password'];

$host = 'localhost';
$db = 'tga-cotacao';
$username = 'root';
$password = '';

$conn = new mysqli($host, $username, $password, $db);

if ($conn->connect_error) {
    die("Erro de conexão: " . $conn->connect_error);
}

$sql = "SELECT password, codcfo FROM gusuarios WHERE `username` = '$user' AND `password` = '$senha'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    $hashed_password = $row['password'];
    
    // Verifica se a senha fornecida pelo usuário corresponde à senha no banco de dados
    if ($sql) {
        header('Location: homepage.php?codcfo='. $row['codcfo']);
        exit;
    } else {
        header('Location: login.php');
        exit;
    }
} else {
    echo "Usuário não encontrado.";
}

$conn->close();
?>
