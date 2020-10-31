<?php 

	session_start();
	
	if(isset($_SESSION['usuario']) and isset($_SESSION['senha']) and isset($_POST['senha1']) and isset($_POST['senha2'])){
	
		$usuario = $_SESSION['usuario'];
		$senha = $_SESSION['senha'];
		
		$senha1 = $_POST['senha1'];
		$senha2 = $_POST['senha2'];

		$con = mysql_connect('localhost','root','');
		mysql_select_db("gaspsbd");
		
		$query = "SELECT * FROM usuario WHERE usuario.login='".$usuario."' AND usuario.senha='".$senha."'";
		$res = mysql_query($query,$con) or die(mysql_error());
		
		if(mysql_num_rows($res)>0){
			
			if($senha1==$senha2){
				
				$query2 ="START TRANSACTION"; 
				$query3 = "UPDATE usuario SET usuario.senha='".$senha1."' WHERE usuario.login='".$usuario."' AND usuario.senha='".$senha."'"; 
				$query4 = "COMMIT";
				
				$res2 = mysql_query($query2,$con) or die(mysql_error());
				$res3 = mysql_query($query3,$con) or die(mysql_error());
				$res4 = mysql_query($query4,$con) or die(mysql_error());
				
				$_SESSION['mensagem_login'] = 'SenhaAlterada';
				header("Location: login.php");
				
			}
			
			else{
				
				$_SESSION['mensagem_login'] = 'Erro ao tentar redefinir senha. As senhas digitadas não são compatíveis.';
				header("Location: login.php");
				
			}
			
		}
	
	}
	
	else{
		
		header("Location: login.php");
		
	}


?>