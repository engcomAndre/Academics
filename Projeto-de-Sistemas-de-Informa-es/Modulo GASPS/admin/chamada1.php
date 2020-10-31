<?php

session_start();

if(isset($_SESSION['usuario']) and isset($_SESSION['senha'])){

    $usuario = $_SESSION['usuario'];
    $senha = $_SESSION['senha'];

    $con = mysql_connect('localhost','root','');
    mysql_select_db("gaspsbd");

    $query = "SELECT * FROM administrador WHERE administrador.login='".$usuario."' AND administrador.senha='".$senha."'";
    $res = mysql_query($query,$con) or die(mysql_error());

    if(mysql_num_rows($res)>0){

        while($row=mysql_fetch_assoc($res)){

            $nome = $row['nome'];
            $sexo = $row['sexo'];
            $idPosto = $row['idPosto'];
            $idAtendente = $row['id'];
        }

    }

    $_SESSION['usuario'] = $usuario;
    $_SESSION['senha'] = $senha;
    $data = $_POST['descEspec'];


}

else{

    header('Location: http://localhost/GASPS/loginatende.php');

}





?>


<html>

<head>

    <title>Chamada de Fichas</title>
    <link href="dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="home.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Barlow+Condensed" rel="stylesheet">

</head>

<body>
<div class="container">

    <div class="col-md align-items-center" style="background-color:#ffffff">
        <h1 class="col-md-6">Chamada Ficha dia <?php echo $data;?></h1>

        <form action="chamada2.php">
            <table class="table table-bordered col-md-auto" >
                <thead>
                <tr>
                    <th scope="col" >#</th>
                    <th scope="col">Usuário</th>
                    <th scope="col" >Observação</th>
                </tr>
                </thead>
                <tbody>
                <?php
                $data1 = new DateTime('18-12-2017');
                $data =  date_format($data1,'Y-m-d');
                ####################################################################################################################
                $query1 = "SELECT usuario.nome,dias.data 
                                       FROM usuario,medicovagas,marcacao,dias 
                                       WHERE usuario.id = marcacao.idUsuario 
                                       AND marcacao.idMedicoVagas = medicovagas.id 
                                       AND medicovagas.idDias = dias.id 
                                       AND dias.data = '2017-12-18'
                                       AND medicovagas.idPosto = 1";
                ####################################################################################################################
                $res1 = mysql_query($query1,$con) or die(mysql_error());

                if(mysql_num_rows($res1)>0){
                    $i = 1;

                    while($row=mysql_fetch_assoc($res1)){
                        echo '<tr>';
                        echo '<th scope="row">'.$i.'</th>';
                        echo '<td>'.$row['nome'].'</a></td>';
                        echo '<th><input name "chamada" id="chamada "type="checkbox" class="btn-light"> </th>';
                        echo '</tr>';
                        $i = $i+1;
                    }

                }
                ?>
                </tbody>
            </table>
        <button type="submit" class="btn btn-primary">Verificar Lista</button>

        </form>
    </div>
</div>
</body>


</div>
<html>

