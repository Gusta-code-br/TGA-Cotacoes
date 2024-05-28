<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>Cadastro de Usuário</h2>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
        <input type="email" name="email" placeholder="Email" required><br><br>

        <input type="password" name="senha" placeholder="Senha" required><br><br>

        <input type="password" name="confirmar_senha" placeholder="Confirmar Senha" required><br><br>

        <input type="submit" value="Cadastrar">
    </form>

    <?php
        $host = 'localhost';
        $db = 'tga-cotacao';
        $username = 'root';
        $password = '';
        
        $conn = new mysqli($host, $username, $password, $db);
        
        if ($conn->connect_error) {
            die("Erro de conexão: " . $conn->connect_error);
        }
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $email = $_POST['email'];
            $senha = $_POST['senha'];
            $confirmar_senha = $_POST['confirmar_senha'];
        
            if ($senha !== $confirmar_senha) {
                echo "<p>As senhas não coincidem. Por favor, tente novamente.</p>";
            } else {
                $senha_hash = password_hash($senha, PASSWORD_DEFAULT);
        
                $sql = "INSERT INTO gusuarios (username, password) VALUES ('$email', '$senha')";
                if ($conn->query($sql) === TRUE) {
                    echo "<p>Usuário cadastrado com sucesso!</p>";
                } else {
                    echo "Erro ao cadastrar o usuário: " . $conn->error;
                }
            }
        }
        
    ?>
</body>
</html>
