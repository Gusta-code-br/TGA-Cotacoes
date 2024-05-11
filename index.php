<!DOCTYPE HTML>
<html>
	<head>
		<meta name="viewport" content="width=100%, initial-scale=1">
		<link rel="stylesheet" href="style.css">
	</head>
	<body>
		<?php

			// Configurações do banco de dados
			$servername = "localhost"; // Host do banco de dados
			$username = "root"; // Nome de usuário do banco de dados
			$password = ""; // Senha do banco de dados
			$database = "cotacao"; // Nome do banco de dados

			// Cria a conexão
			$conn = new mysqli($servername, $username, $password, $database);

			// Verifica a conexão
			if ($conn->connect_error) {
			    die("Falha na conexão: " . $conn->connect_error);
			}

			// Query SQL
			$sql = "SELECT email FROM produtos WHERE codcfo = 'cod00' GROUP BY email";

			// Executa a query
			$result = $conn->query($sql);

			// Verifica se há resultados
			if ($result->num_rows > 0) {
			    // Itera sobre os resultados
			    while($row = $result->fetch_assoc()) {
			        // Exibe os dados
			        ?>
			        <div>
					    <p>Cotação de: <?php echo $row["email"]; ?></p>
					    <a href="form_produto.php?email=<?php echo urlencode($row["email"]); ?>">Ver cotação</a>
					</div>
			        <?php 
			    }
			} else {
			    echo "Não foram encontrados resultados";
			}

			// Fecha a conexão
			$conn->close();

		?>

	</body>
</html>
