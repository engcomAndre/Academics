<?php

session_start();

if(isset($_POST['usuario']) and isset($_POST['senha'])){

    $con = mysql_connect('localhost','root','');
    mysql_select_db("gaspsbd");

    $query = "SELECT * FROM administrador WHERE administrador.login='".$_POST['usuario']."' AND administrador.senha='".$_POST['senha']."'";
    $res =  mysql_query($query,$con) or die(mysql_error());

    if(mysql_num_rows($res)>0){

        $_SESSION['usuario'] = $_POST['usuario'];
        $_SESSION['senha'] = $_POST['senha'];
        header('Location: admin/home.php');

    }
    else{

        $_SESSION['mensagem_login'] = 'Usuário ou senha incorretos. Por favor verifique e tente novamente.';
        header('Location: loginadmin.php');

    }

}
else{

    header('Location: loginadmin.php');

}

?>