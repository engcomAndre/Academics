<?php 

	session_start();
	
	if(isset($_SESSION['usuario']) and isset($_SESSION['senha'])){
		
		$usuario = $_SESSION['usuario'];
		$senha = $_SESSION['senha'];
		
		$_SESSION['usuario'] = $usuario;
		$_SESSION['senha'] = $senha;
		
		$con = mysql_connect('localhost','root','');
		mysql_select_db("gaspsbd");
		
		if(isset($_POST['usuarioBairro'])){}
		else{
			
			header('Location: cadastro_usuario.php');
			
		}
		
		if($_POST['usuarioBairro']=='Escolha uma opção...' and ($_POST['usuarioBairro2']==NULL or $_POST['usuarioBairro2']=='')){
			
			header('Location: cadastro_usuario.php');
			
		}
		
		if($_POST['usuarioBairro2']!=NULL and $_POST['usuarioBairro2']!='' and $_POST['usuarioRegional']=='Escolha uma regional...'){
			
			header('Location: cadastro_usuario.php');
			
		}
		
		if(isset($_POST['usuarioBairro2']) and $_POST['usuarioBairro2']!=NULL and $_POST['usuarioBairro2']!='' ){
			
			//bairro nao cadastrado
			
			$query2 = "SELECT * FROM regional WHERE regional.desc = '".$_POST['usuarioRegional']."' 
			AND regional.idCidade = ".$_SESSION['idUsuarioCidade']." 
			AND regional.idEstado = ".$_SESSION['idUsuarioEstado']."";
			
			$res2 = mysql_query($query2,$con) or die(mysql_error());
			
			while($row2 = mysql_fetch_assoc($res2)){
				
				$idRegional = $row2['id'];
				
			}
			
			$query = "INSERT INTO bairro(bairro.desc,bairro.idRegional) VALUES ('".$_POST['usuarioBairro2']."',".$idRegional.")";
			$res = mysql_query($query,$con) or die(mysql_error());
			
			$_SESSION['usuarioBairro'] = $_POST['usuarioBairro2'];
			
			
		}
		else{
			
			//bairro cadastrado
			$_SESSION['usuarioBairro'] = $_POST['usuarioBairro'];
			
		}
		
		
		$query3 = "SELECT bairro.id AS idBairro,bairro.desc,regional.* FROM bairro,regional 
		WHERE bairro.idRegional=regional.id 
		AND bairro.desc='".$_SESSION['usuarioBairro']."' 
		AND regional.idEstado=".$_SESSION['idUsuarioEstado']." 
		AND regional.idCidade=".$_SESSION['idUsuarioCidade']."";
		
		$res3 = mysql_query($query3,$con) or die(mysql_error());
		
		while($row3 = mysql_fetch_assoc($res3)){
			
			$idUsuarioBairro = $row3['idBairro'];
			
		}
		
		$query4 = "INSERT INTO usuario(nome,sexo,cartaoSUS,RG,idBairro,CPF, 
		login,senha,preferencial,telefone1,telefone2) 
		VALUES ('".$_SESSION['usuarioNome']."', 
		'".$_SESSION['usuarioSexo']."', '".$_SESSION['usuarioSUS']."', '".$_SESSION['usuarioRG']."', 
		'".$idUsuarioBairro."', '".$_SESSION['usuarioCPF']."', '".$_SESSION['usuarioLogin']."', '', '".$_SESSION['usuarioPref']."', 
		'".$_SESSION['usuarioTel1']."', '".$_SESSION['usuarioTel2']."')";
		
		$res4 = mysql_query($query4,$con) or die(mysql_error());
		
		$_SESSION['mensagem_cadastro_usuario'] = 'Usuário '.$_SESSION['usuarioLogin'].' cadastrado com sucesso.';
		header('Location: home.php');		
	
	}
	
	else{
		
		header('Location: http://localhost/GASPS/loginatende.php');
		
	}



?>
