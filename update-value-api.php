<?php
// Adicione cabeçalhos para permitir solicitações de origens diferentes
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST");
header("Access-Control-Allow-Headers: Content-Type");

// Configuração do banco de dados
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "tga-cotacao";

// Conexão com o banco de dados
$conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Verifica se os dados foram enviados via POST
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $data = json_decode(file_get_contents("php://input"), true);

    // Verifica se os dados recebidos são um array
    if (is_array($data)) {
        foreach ($data as $item) {
            // Verifica se os dados do item contêm um ID de produto e um valor
            if (isset($item["nseq"]) && isset($item["valor"])) {
                $id = $item["nseq"];
                $valor = $item["valor"];

                // Atualiza o valor no banco de dados
                $stmt = $conn->prepare("UPDATE tcotacaoorcitm SET valorcotado = :valor WHERE nseq = :nseq");
                $stmt->bindParam(':valor', $valor);
                $stmt->bindParam(':nseq', $id);
                $stmt->execute();
            }
        }

        $response = ["success" => true, "message" => "Valores atualizados com sucesso"];
    } else {
        // Retorna uma mensagem de erro se os dados não forem um array
        $response = ["success" => false, "message" => "Dados inválidos"];
    }
} else {
    // Retorna uma mensagem de erro se a requisição não for do tipo POST
    $response = ["success" => false, "message" => "Método não permitido"];
}

// Retorna a resposta como JSON
header('Content-Type: application/json');
echo json_encode($response);
?>
