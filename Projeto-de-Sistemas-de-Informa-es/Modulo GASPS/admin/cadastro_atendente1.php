<?php

session_start();

if(isset($_SESSION['usuario']) and isset($_SESSION['senha'])){

    $usuario = $_SESSION['usuario'];
    $senha = $_SESSION['senha'];

    $_SESSION['usuario'] = $usuario;
    $_SESSION['senha'] = $senha;

    $con = mysql_connect('localhost','root','');
    mysql_select_db("gaspsbd");
    $nome = $_POST['usuarioNome'];
    $login = $_POST['usuarioLogin'];
    $senha = $_POST['senha'];
    $endereco = $_POST['endereço'];
    $tel1 = $_POST['usuarioTel1'];
    $tel2 = $_POST['usuarioTel2'];
    $sexo = $_POST['usuarioSexo'];
    $post = $_POST['posto'];


    $query4 = "INSERT INTO atendente (id, nome, sexo, endereco, usuario, senha, telefone1, telefone2, idPosto)
               VALUES ('','".$nome."','".$sexo."','".$endereco."','".$login."','".$sexo."','".$tel1."','".$tel1."','".$post."')";

    $res4 = mysql_query($query4,$con) or die(mysql_error());

    $_SESSION['mensagem_cadastro_usuario'] = 'Atendente '.$nome.' cadastrado com sucesso.';
    header('Location: home.php');

}

else{

    header('Location: http://localhost/GASPS/loginadmin.php');

}



?>
