TGA – Cotações

Introdução: 
O TGA-Cotações é um software projetado para simplificar o manuseio do módulo de cotações do sistema TGA Estoque da empresa TGA. Seu objetivo é agilizar e organizar essa ferramenta, eliminando cliques desnecessários e otimizando o tempo necessário para realizar as ações. O software foi desenvolvido para beneficiar tanto o usuário responsável pela criação da cotação quanto o fornecedor que a receberá.


Requisitos Funcionais: 
O sistema deve permitir que o usuário faça login com o mesmo usuário do TGA Estoque.
O sistema deve permitir que o usuário faça consulta de cotações, gere links de cotações e resgate resultados.
O sistema deve permitir que o usuário veja o status da cotação

Requisitos não funcionais: 

Desempenho: 
O sistema deve permitir que todos os fornecedores acessem a cotação simultaneamente sem perda de desempenho.
O software deve ser capaz de rodar até mesmo nas máquinas mais lentas
O software deve ser capaz de se ajustar a todos os tipos de tela

Segurança: 
O software deve proteger todas as informações tanto do fornecedor quanto do usuário/empresa que gerou a cotação.

Confiabilidade: 
O sistema deve estar online em 99% do tempo, salvo momentos de manutenção previamente avisados.

Compatibilidade: 
O sistema será capaz de ser exibido nos principais navegadores e dispositivos



Informações de Software e sistema:


Software TGA-Cotações: 

O software foi desenvolvido utilizando a tecnologia Python, escolhida devido ao conhecimento da equipe, facilidade de uso e manutenção, além da compatibilidade com bancos de dados e sua abrangência de funcionalidades. A versão utilizada foi a 3.9, com possibilidade de atualização para versões mais recentes no futuro. Foram empregadas as seguintes bibliotecas para o desenvolvimento do software:

- from tkinter import ttk
- from tkinter import messagebox
- import customtkinter
- import fdb
- import hashlib
- import pyperclip
- from configparser import ConfigParser
- import openpyxl
- import pymysql
- import shutil

Rotina de implementação do sistema:

Para implementar o sistema de cotação TGA, primeiro será necessário executar o instalador do sistema que além de implementar o sistema na máquina, adiciona em "C:\USERS\USER\APPDATA\LOCAL\COTACAO" os arquivos 'desktop.ini' e 'base.xls'. Após instalado é preciso entrar no sistema do TGA Estoque e em 'Cadastros>Segurança>Perfil de Acesso>Acesso personalizado', deve ser criado o perfil de acesso 'ACESSA_COTACAO' os usuário que tiverem seu perfil de acesso com essa opção ativada poderão usar o 'TGA - Cotação'.

Rotina de Utilização do Sistema:

Após o usuário já ter gerado uma cotação pelo sistema do TGA - Estoque, ele irá ao TGA - Cotação. 1º Step: Primeiro ele deve entrar com o mesmo login e senha que foi criado para o TGA Estoque (Lembrando que o usuário precisa ter acesso para poder acessar). 2º Step: Após a tela de login ele cairá direto na tela de geração de link compartilhavel, nela, ele poderá filtrar a cotação desejada da maneira em que achar melhor. Após filtrar, para gerar o link basta dar um duplo clique na cotação que deseja, ao fazer isso automaticamente na área de transferência do usuário irá estar o link da cotação. 3º Step: Após o fornecedor ter devolvido a cotação, o usuário deve clicar no botão "Resposta Fornecedor" ao ter clicado basta consultar a cotação que deseja baixar, o usuário deve dar um duplo clique na cotação que deseja. O arquivo da cotação será gerado na área de trabalho o nome do arquivo será o código da cotação + código do fornecedor.
Após isso é necessário carregar no sistema TGA - Estoque utilizado a rotina de Cotação (Ctrl + Alt + O).
