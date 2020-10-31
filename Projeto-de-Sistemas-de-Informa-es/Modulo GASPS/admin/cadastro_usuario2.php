<?php 

	session_start();
	
	if(isset($_SESSION['usuario']) and isset($_SESSION['senha'])){
		
		$usuario = $_SESSION['usuario'];
		$senha = $_SESSION['senha'];
		
		$_SESSION['usuario'] = $usuario;
		$_SESSION['senha'] = $senha;
		
		if(isset($_POST['usuarioNome'])){}
		else{
			
			header('Location: cadastro_usuario.php');
			
		}
		
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
		
		$_SESSION['usuarioNome'] = $_POST['usuarioNome'];
		$_SESSION['usuarioLogin'] = $_POST['usuarioLogin'];
		$_SESSION['usuarioRG'] = $_POST['usuarioRG'];
		$_SESSION['usuarioCPF'] = $_POST['usuarioCPF'];
		$_SESSION['usuarioSUS'] = $_POST['usuarioSUS'];
		$_SESSION['usuarioTel1'] = $_POST['usuarioTel1'];
		$_SESSION['usuarioTel2'] = $_POST['usuarioTel2'];
		$_SESSION['usuarioSexo'] = $_POST['usuarioSexo'];
		$_SESSION['usuarioPref'] = $_POST['usuarioPref'];
		$_SESSION['usuarioEstado'] = $_POST['usuarioEstado'];
	
	}
	
	else{
		
		header('Location: http://localhost/GASPS/loginatende.php');
		
	}



?>


<html>

	<head>
		
		<title>Cadastro de Usuário</title>
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
						<h2 class="txtquestao">Cadastro de Usuário:<h2>
					</div><br>
					
					<form action="cadastro_usuario3.php" method="post" >
					
						  
						  <div class="form-group">
						  <label for="usuarioCidade">Cidade:</label>
						  <select id="usuarioCidade" name="usuarioCidade" class="form-control">
						  <option>Escolha uma opção...</option>
							
							<?php
							
								$query2 = "SELECT * FROM estado WHERE estado.desc='".$_SESSION['usuarioEstado']."'";
								$res2 = mysql_query($query2,$con) or die(mysql_error());
								
								while($row2 = mysql_fetch_assoc($res2)){
									
									$_SESSION['idUsuarioEstado'] = $row2['id'];
									
									$query3 = "SELECT * FROM cidade WHERE cidade.idEstado=".$row2['id']."";
									$res3 = mysql_query($query3,$con) or die(mysql_error());
									
									while($row3 = mysql_fetch_assoc($res3)){
										
										echo '<option>'.$row3['desc'].'</option>';
										
									}
									
								}
							
							?>
							
						  </select>
						  </div>
						  
						  <div class="form-group">
							<label for="usuarioCidade2">Não encontrou a cidade?:</label>
							<input type="text" class="form-control" id="usuarioCidade2" name="usuarioCidade2" placeholder="Digite aqui a cidade">
						  </div>
						  
						  <button type="submit" class="btn btn-primary">Próximo Passo -></button>
						  
						  
					</form>
					
			
				</div>
			
			</div>
		
		</div>
		
	</body>

</html>