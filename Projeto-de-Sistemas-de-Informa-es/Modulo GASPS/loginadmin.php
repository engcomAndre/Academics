
<?php

session_start();

if(isset($_SESSION['mensagem_login'])){

    echo
        '<div class="alert alert-danger" role="alert">
		'.$_SESSION['mensagem_login'].'
		</div>';

    unset($_SESSION['mensagem_login']);

}


?>


<html>

<head>

    <title>
        GASPS-Login
    </title>

    <link href="https://fonts.googleapis.com/css?family=Lobster" rel="stylesheet">
    <link href="dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="login.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Barlow+Condensed" rel="stylesheet">

</head>

<body>

<div class="container rounded float-left">

    <div class="row justify-content-md-center linha1">

        <div class="col-md-auto linha1-coluna1">
            <img src="images/logo.png" width="250" height="100"></img>
        </div>

        <div class="col-md-auto linha1-coluna2">
            <h2 class="txtbemvindo">Bem-vindo(a) ao Gasps!</h2>
        </div>

    </div>

    <div class="row justify-content-md-center linha2">

        <h2 class="txtefetue">Para acessar o sistema, efetue o login</h2>

    </div>

    <div class="row justify-content-md-center linha3">

        <div class="col-md-auto linha3-coluna2">

            <form action="checaloginadmin.php" method="post">

                <div class="input-group input-group-lg">
                    <input type="text" class="form-control" id="usuario" name="usuario" placeholder="Usuário" required>
                </div>

                <div class="input-group input-group-lg">
                    <input type="password" class="form-control" id="senha" name="senha" placeholder="Senha" required>
                </div>

                <div class="row">

                    <div class="col-sm">
                        <h5 class="btnesqueceu"><a href>Esqueceu a senha?</a></h5>
                    </div>

                    <div class="col-sm">
                        <button type="submit" class="btn btn-success btn-lg float-right">Entrar</button>
                    </div>

                </div>

            </form>

        </div>

    </div>

    <br>
    <div class="row linha4">
        <h6>Desenvolvido por Luan/André<h6>
    </div>

</div>

</body>

</html>