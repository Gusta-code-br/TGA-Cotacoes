<?php
// Permitir solicitações de qualquer origem
header("Access-Control-Allow-Origin: *");

// Permitir os métodos POST, GET, OPTIONS
header("Access-Control-Allow-Methods: POST, GET, OPTIONS");

// Permitir os cabeçalhos Content-Type e Authorization
header("Access-Control-Allow-Headers: Content-Type, Authorization");

// Encerrar a execução do script se a solicitação for OPTIONS
if ($_SERVER['REQUEST_METHOD'] == 'OPTIONS') {
    http_response_code(200);
    exit();
}

$idcotacao = $_GET['cotid'];
$codcfo = $_GET['cfo'];

// Configuração do banco de dados
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "tga-cotacao";

// Conexão com o banco de dados
$conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Consulta SQL para obter os produtos
$stmt = $conn->prepare("SELECT nseq, pr.nomefantasia FROM tcotacaoorcitm ci JOIN tproduto pr ON ci.codprd = pr.codprd WHERE codcotacao = 2021.000001 AND codcfo = 'C00428' ");
$stmt->execute();
$produtos = $stmt->fetchAll(PDO::FETCH_ASSOC);

// Retornar os produtos como JSON
header('Content-Type: application/json');
echo json_encode($produtos);
?>
