<!DOCTYPE html>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="style.css">
    <link rel="stylesheet" type="text/css" href="NORMALIZE.CSS">
	<title></title>
</head>
<body>
    <header>
        <h1 style="text-align: center; margin: 1%;">PRODUTOS</h1>
    </header>
	<?php

// Verifica se o parâmetro 'email' está presente na URL
if (isset($_GET['codcotacao'], $_GET['codcfo'])) {
    // Obtém o valor do parâmetro 'email'
    $codcotacao = $_GET['codcotacao'];
    $codcfo = $_GET['codcfo'];

    // Conecta ao banco de dados
    $conn = new mysqli("localhost", "root", "", "tga-cotacao");

    // Verifica se houve algum erro na conexão
    if ($conn->connect_error) {
        die("Falha na conexão: " . $conn->connect_error);
    }

    // Prepara a consulta SQL com um parâmetro marcado (?)
    $sql = "SELECT a.nseq, b.nomefantasia FROM tcotacaoorcitm a JOIN tproduto b ON b.codprd = a.codprd WHERE a.codcotacao = ? AND codcfo = ?";
    $stmt = $conn->prepare($sql);

    // Verifica se houve algum erro ao preparar a consulta SQL
    if (!$stmt) {
        die("Erro ao preparar a consulta: " . $conn->error);
    }

    // Vincula o valor do email ao parâmetro marcado
    $stmt->bind_param("ss", $codcotacao, $codcfo);

    // Executa a consulta SQL
    $stmt->execute();

    // Obtém os resultados da consulta
    $result = $stmt->get_result();

    // Verifica se há resultados
    if ($result->num_rows > 0) {
        // Itera sobre os resultados
        while($row = $result->fetch_assoc()) {
            // Exibe os dados
            ?>
            <div>
                <p>ID: <?php echo $row["nseq"]; ?> - Nome: <?php echo $row["nomefantasia"]; ?></p>
                <input type='text' name='<?php echo $row["nomefantasia"]?>' placeholder='valor' required style='margin: 10px;'>
            </div>
            <?php
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
<div class="back_go">
    <a href="homepage.php"><svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="gray" class="bi bi-arrow-left-square-fill" viewBox="0 0 16 16">
    <path d="M16 14a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2zm-4.5-6.5H5.707l2.147-2.146a.5.5 0 1 0-.708-.708l-3 3a.5.5 0 0 0 0 .708l3 3a.5.5 0 0 0 .708-.708L5.707 8.5H11.5a.5.5 0 0 0 0-1"/>
    </svg></a>
    <button>Enviar</button>
</div>        

</body>
</html>
    