<?php 

	session_start();
	
	if(isset($_SESSION['usuario']) and isset($_SESSION['senha'])){
		
		$usuario = $_SESSION['usuario'];
		$senha = $_SESSION['senha'];
		
		$con = mysql_connect('localhost','root','');
		mysql_select_db("gaspsbd");
	
		$query = "SELECT * FROM administrador WHERE administrador.login ='".$usuario."' AND administrador.senha='".$senha."'";
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
		
	}
	
	else{
		
		header('Location: http://localhost/GASPS/loginatende.php');
		
	}



?>


<html>

	<head>
		
		<title>Cadastro de Especialidade</title>
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
						<h2 class="txtquestao">Cadastro de Especialidade:<h2>
					</div><br>
					
					<form action="cadastro_especialidade2.php" method="post" >
					
						  <div class="form-group">
							<label for="espec">Especialidade Medica:</label>
							<input type="text" class="form-control" id="espec" name="espec" aria-describedby="emailHelp" placeholder="Digite aqui a especialidade médica que deseja associar ao posto" required>
							<small id="emailHelp" class="form-text text-muted">Primeira letra deve ser maiúscula</small>
						  </div>
						  
						  <button type="submit" class="btn btn-primary">Cadastrar Especialidade</button>
						  
					</form>
			
				</div>
			
			</div>
		
		</div>

	</body>

</html>