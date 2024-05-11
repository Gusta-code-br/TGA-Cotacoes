<!DOCTYPE html>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
</head>
<body>
	<?php

// Verifica se o parâmetro 'email' está presente na URL
if (isset($_GET['email'])) {
    // Obtém o valor do parâmetro 'email'
    $email = $_GET['email'];

    // Conecta ao banco de dados
    $conn = new mysqli("localhost", "root", "", "cotacao");

    // Verifica se houve algum erro na conexão
    if ($conn->connect_error) {
        die("Falha na conexão: " . $conn->connect_error);
    }

    // Prepara a consulta SQL com um parâmetro marcado (?)
    $sql = "SELECT id, nome, quantidade, codcfo FROM produtos WHERE email = ?";
    $stmt = $conn->prepare($sql);

    // Verifica se houve algum erro ao preparar a consulta SQL
    if (!$stmt) {
        die("Erro ao preparar a consulta: " . $conn->error);
    }

    // Vincula o valor do email ao parâmetro marcado
    $stmt->bind_param("s", $email);

    // Executa a consulta SQL
    $stmt->execute();

    // Obtém os resultados da consulta
    $result = $stmt->get_result();

    // Verifica se há resultados
    if ($result->num_rows > 0) {
        // Itera sobre os resultados
        while($row = $result->fetch_assoc()) {
            // Exibe os dados
            echo "ID: " . $row["id"]. " - Nome: " . $row["nome"]. " - Quantidade: " . $row["quantidade"]. "<input type='text' placeholder='valor' required style='margin: 10px;'>"."<br>"  ;
        }
    } else {
        echo "Não foram encontrados resultados para o email: " . $email;
    }

    // Fecha a conexão
    $stmt->close();
    $conn->close();
} else {
    // Se 'email' não estiver presente na URL, exiba uma mensagem de erro
    echo "Parâmetro 'email' não encontrado na URL";
}

?>


</body>
</html>