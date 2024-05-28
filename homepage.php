<!DOCTYPE HTML>
<html>
	<head>
		<meta name="viewport" content="device-width, initial-scale=1">
		<link rel="stylesheet" href="style.css">
		<link rel="stylesheet" type="text/css" href="normalize.css">
	</head>
	<body>
		<header>
			<h1 style="text-align: center; margin: 2%;">COTAÇÕES</h1>	
		</header>
		
		<?php
		if (isset($_GET['codcfo'])) {
			// Obtém o valor do parâmetro 'email'
			$codcfo = $_GET['codcfo'];
			// Configurações do banco de dados
			$servername = "localhost"; // Host do banco de dados
			$username = "root"; // Nome de usuário do banco de dados
			$password = ""; // Senha do banco de dados
			$database = "tga-cotacao"; // Nome do banco de dados

			// Cria a conexão
			$conn = new mysqli($servername, $username, $password, $database);

			// Verifica a conexão
			if ($conn->connect_error) {
			    die("Falha na conexão: " . $conn->connect_error);
			}	

			// Query SQL
			$sql = "SELECT a.codcotacao FROM tcotacaoorcitm a JOIN gusuarios b ON b.codcfo = a.codcfo WHERE a.codcfo = '$codcfo' GROUP BY codcotacao";

			// Executa a query
			$result = $conn->query($sql);

			// Verifica se há resultados
			if ($result->num_rows > 0) {
			    // Itera sobre os resultados
			    while($row = $result->fetch_assoc()) {
			        // Exibe os dados
			        ?>
			        <div>
					    <p>Cotação de: <?php echo $row["codcotacao"]; ?></p>
					    <a href="form_produto.php?codcotacao=<?php echo urlencode($row["codcotacao"]); ?>&codcfo=<?php echo urlencode($codcfo);?>">Ver cotação</a>
					</div>
			        <?php 
			    }
			} else {
			    echo "Não foram encontrados resultados";
			}

			// Fecha a conexão
			$conn->close();
		}
		else{
			echo 'Deu ruim';
		}
		?>

	</body>
</html>
