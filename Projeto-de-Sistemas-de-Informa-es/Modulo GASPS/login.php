
<?php 

	session_start();
	
	if(isset($_SESSION['mensagem_temfaltas'])){
		
		echo'
		<div class="alert alert-danger" role="alert">
			Você possui faltas não justificadas. Apresente-se ao posto de saúde mais próximo e justifique suas faltas.
		</div>
		';	
		
	}
	
	else{
	
	if(isset($_SESSION['usuario']) and isset($_SESSION['senha']) and $_SESSION['senha']!=''){
		
		header('Location: usuario\home.php');
		
	}
	
	else{

		if(isset($_SESSION['mensagem_login'])){
			
			if($_SESSION['mensagem_login']=='redefinir'){
				
				$usuario = $_SESSION['usuario'];
				$senha = $_SESSION['senha'];
				
				$_SESSION['usuario'] = $usuario;
				$_SESSION['senha'] = $senha;	
				
				echo '
				<html>
					
					<head>
					
						<link href="dist/css/bootstrap.min.css" rel="stylesheet">
						<link href="trocasenha.css" rel="stylesheet">
						<link href="https://fonts.googleapis.com/css?family=Barlow+Condensed" rel="stylesheet">
					
					</head>
					
					<body>
					
					<div class="redefine rounded">
						
						<br>
						<h4 class="text-center">Redefinir senha</h4><br>
						<h5 class="text-center">Insira uma nova senha para acessar o sistema</h5><br>
						
						<form action="redefinesenha.php" method="post">
						
							<div class="input-group input-group-lg">
							<input type="password" class="form-control" id="senha1" name="senha1" style="margin-right:50;margin-left:50" placeholder="Digite a nova senha" required>
							</div>
							
							<div class="input-group input-group-lg">
							<input type="password" class="form-control" id="senha2" name="senha2" style="margin-right:50;margin-left:50" placeholder="Digite a nova senha novamente" required>
							</div>
							
							<div class="col-sm">
								<button type="submit" class="btn btn-success btn-lg float-right" style="margin-right:50">Entrar</button>
							</div>
						
						</form>
					
					</div>
					
					</body>
					
				</html>
				';
				
			}
			
			else if($_SESSION['mensagem_login']=='SenhaAlterada'){
				
				echo'
				<div class="alert alert-success" role="alert">
				   Senha alterada com sucesso. Faça login novamente utilizando sua nova senha.
				</div>
				';
				
			}
			
			else{
				echo'
				<div class="alert alert-danger" role="alert">
					'.$_SESSION['mensagem_login'].'
				</div>
				';		
			}
			
			unset($_SESSION['mensagem_login']);
			
		};
	
	}
	
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
			
				<div class="col-md-auto linha3-coluna1">
					<h3><img src="images/check.png" width="30" height="30" > Marque consultas sem sair de casa</h3><br>
					<h3><img src="images/check.png" width="30" height="30" > Rápido, fácil e seguro</h3>
				</div>
				
				<div class="linha3-centro"></div>
				
				<div class="col-md-auto linha3-coluna2">
					
					<form action="checalogin.php" method="post">
					
						<div class="input-group input-group-lg">
						<input type="text" class="form-control" id="usuario" name="usuario" placeholder="Usuário" required>
						</div>
						
						<div class="input-group input-group-lg">
						<input type="password" class="form-control" id="senha" name="senha" placeholder="Senha">
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