<?php

	session_start();
	
	if(isset($_POST['usuario'])){
		
		$usuario = $_POST['usuario'];
		$senha = $_POST['senha'];
	
		$con = mysql_connect('localhost','root','');
		mysql_select_db("gaspsbd");
	
		$query = "SELECT * FROM usuario WHERE usuario.login='".$usuario."' AND usuario.senha='".$senha."'";
		$res = mysql_query($query,$con) or die(mysql_error());
	
		if(mysql_num_rows($res)>0){
			
			if($senha==''){
				
				$_SESSION['mensagem_login'] = 'redefinir';
				$_SESSION['usuario'] = $usuario;
				$_SESSION['senha'] = $senha;
				header("Location: login.php");
				
			}
			
			else{
				
				$_SESSION['usuario'] = $usuario;
				$_SESSION['senha'] = $senha;
				header("Location: usuario\home.php");
				
			}
			
		}
		
		else{
			
			$_SESSION['mensagem_login'] = 'Usuário ou senha incorretos. Favor verifique e tente novamente.';
			header("Location: login.php");
			
		}
		
	}
	
	else{
		
		header("Location: login.php");
		
	}

?>