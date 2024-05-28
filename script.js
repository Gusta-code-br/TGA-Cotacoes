function cadastrar() {
  const email = document.getElementById('user-name').value;
  const senha = document.getElementById('password').value;
  const confirmSenha = document.getElementById('confirm-senha').value;
  const newData = [];

  console.log('teste')

  // Verifica se as senhas são iguais
  if (senha !== confirmSenha) {
      alert('As senhas não são iguais');
      return;
  }

  if (!isNaN([email, senha])) {
    newData.push({ email: email, senha: senha });
} else {
    console.error(`Valor inválido para o produto ${nseq}`);
}
  // Envia os dados para a API PHP
  fetch('http://localhost/API-TGA/log-on-api.php', {
      method: 'POST',
      body: JSON.stringify(newData),
      headers: {
          'Content-Type': 'application/json',
      },
           
  })
  .then(response => response.json())
  .catch(error => {
      console.error('Erro ao enviar dados para a API:', error);
      alert('Erro ao cadastrar. Por favor, tente novamente.');
  });
}
