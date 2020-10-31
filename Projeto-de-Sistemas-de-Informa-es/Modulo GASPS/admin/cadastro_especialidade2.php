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

			}

		}

		$_SESSION['usuario'] = $usuario;
		$_SESSION['senha'] = $senha;

		$espec = $_POST['espec'];

		$query2 = "SELECT * FROM especialidade WHERE especialidade.desc='".$espec."'";
		$res2 = mysql_query($query2,$con) or die(mysql_error());

		if(mysql_num_rows($res2)>0){
		}
		else{

			$query3 = "INSERT INTO especialidade(especialidade.desc) VALUES('".$espec."')";
			$res3 = mysql_query($query3,$con) or die(mysql_error());

		}

		$query4 = "SELECT * FROM especialidade WHERE especialidade.desc='".$espec."'";
		$res4 = mysql_query($query4,$con) or die(mysql_error());

		if(mysql_num_rows($res4)>0){

			while($row4 = mysql_fetch_assoc($res4)){

				$idEspecialidade = $row4['id'];

			}

		}

		$query5 = "SELECT * FROM postomedico WHERE postomedico.idPosto=".$idPosto." AND postomedico.idEspecialidade=".$idEspecialidade."";
		$res5 = mysql_query($query5,$con) or die(mysql_error());

		if(mysql_num_rows($res5)>0){

			$_SESSION['mensagem_cadastro_usuario'] = 'Especialidade já associada ao posto';
			header('Location: home.php');

		}
		else{

			$query6 = "INSERT INTO postomedico(postomedico.idPosto,postomedico.idEspecialidade) 
			VALUES(".$idPosto.",".$idEspecialidade.")";

			$res6 = mysql_query($query6,$con) or die(mysql_error());

			$_SESSION['mensagem_cadastro_usuario'] = 'Especialidade cadastrada com sucesso';
			header('Location: home.php');

		}

	}

	else{

		header('Location: http://localhost/GASPS/loginatende.php');

	}



?>
