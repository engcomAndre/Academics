<?php

session_start();

if(isset($_SESSION['usuario']) and isset($_SESSION['senha'])){

    $usuario = $_SESSION['usuario'];
    $senha = $_SESSION['senha'];

    $con = mysql_connect('localhost','root','');
    mysql_select_db("gaspsbd");

    $query = "SELECT * FROM atendente WHERE atendente.usuario='".$usuario."' AND atendente.senha='".$senha."'";
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

}

else{

    header('Location: http://localhost/GASPS/loginatende.php');

}





?>


<html>

<head>

    <link href="dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="home.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Barlow+Condensed" rel="stylesheet">

</head>

<body>

<div class="container">

    <div class="row">

        <div class="col-md-auto">

            <div class="col-md-auto c1 rounded" style="background-color:<?php

            if($sexo=='M'){

                echo "#3333cc";
            }
            else{

                echo "#ff0066";

            }


            ?>" >
                <div class="row c1-logo">
                    <img src="images/logo2.png" width="315" height="100">
                </div>

                <div class="row c1-l1">
                    <img src=<?php

                    if($sexo=='M'){

                        echo "images/homem.png";
                    }
                    else{

                        echo "images/mulher.png";

                    }


                    ?>>
                </div>

                <div class="row c1-l2">
                    <h3 class="txtnome"><?php echo $nome; ?></h3>
                </div>

                <div class="row">
                    <a href="logout.php"><button type="button" class="btn btn-danger btn-lg">Sair do sistema</button></a>
                </div><br>

                <div class="row">
                    <a href="home.php"><button type="button" class="btn btn-success btn-lg">Voltar à tela de opções</button></a>
                </div>

            </div>

        </div>

        <div class="col-sm c2">

            <div class="row c2-l1 rounded border border-secondary">
                <h2 class="txtquestao">Imprimir Fichas<h2>
            </div><br>

            <form action="imprimirfichas2.php" method="post" >

                <div class="form-group">
                    <label for="imprimeFicha">Impressão de Fichas:(Escolha um Data)</label>
                    <select id="descEspec" name="descEspec" class="form-control">
                        <?php

                        $query = "SELECT dias.data FROM marcacao,medicovagas,dias,atendente 
                                  WHERE marcacao.idMedicoVagas = medicovagas.id 
                                  AND medicovagas.idPosto = atendente.idPosto 
                                  AND atendente.id = ".$idAtendente." group by dias.id having Count(Nome)>1";

                        $res = mysql_query($query,$con) or die(mysql_error());

                        while($row = mysql_fetch_assoc($res)){

                            echo '<option >'.$row['data'].'</option>';

                        }
                        ?>

                    </select>

                </div>
                <br>
                <button type="submit" class="btn btn-primary">Imprimir Lista</button>



            </form>

        </div>

    </div>

</div>

</body>

</html>