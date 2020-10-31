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
					
					<form action="cadastro_usuario2.php" method="post" >
					
						<div class="form-group">
							<label for="usuarioNome">Nome completo:</label>
							<input type="text" class="form-control" id="usuarioNome" name="usuarioNome" placeholder="Digite aqui o nome completo do usuario" required>
						  </div>
					
						  <div class="form-group">
							<label for="usuarioUser">Login:</label>
							<input type="text" class="form-control" id="usuarioLogin" name="usuarioLogin" aria-describedby="emailHelp" placeholder="Digite aqui o login para acesso ao sistema" required>
							<small id="emailHelp" class="form-text text-muted">Inserir .user no final do nome de usuario</small>
						  </div>
						  
						  <div class="form-group">
							<label for="usuarioRG">RG:</label>
							<input type="text" class="form-control" id="usuarioRG" name="usuarioRG" placeholder="Digite aqui o RG do usuario" required>
						  </div>
						  
						  <div class="form-group">
							<label for="usuarioCPF">CPF:</label>
							<input type="text" class="form-control" id="usuarioCPF" name="usuarioCPF" placeholder="Digite aqui o CPF do usuario" required>
						  </div>
						  
						  <div class="form-group">
							<label for="usuarioSUS">Cartão do SUS:</label>
							<input type="text" class="form-control" id="usuarioSUS" name="usuarioSUS" placeholder="Digite aqui o número do cartão do SUS do usuario" required>
						  </div>
						  
						  <div class="form-group">
							<label for="usuarioTel1">Telefone 1:</label>
							<input type="text" class="form-control" id="usuarioTel1" name="usuarioTel1" placeholder="Digite aqui um número de telefone do usuario" required>
						  </div>
						  
						  <div class="form-group">
							<label for="usuarioTel2">Telefone 2:</label>
							<input type="text" class="form-control" id="usuarioTel2" name="usuarioTel2" placeholder="Digite aqui outro número de telefone do usuario (Opcional)">
						  </div>
						  
						  <div class="form-group">
						  <label for="usuarioSexo">Sexo:</label>
						  <select id="usuarioSexo" name="usuarioSexo" class="form-control">
							<option selected>Masculino</option>
							<option>Feminino</option>
						  </select>
						  </div>
						  
						  <div class="form-group">
						  <label for="usuarioPref">Preferencial?:</label>
						  <select id="usuarioPref" name="usuarioPref" class="form-control">
							<option selected>Sim</option>
							<option>Não</option>
						  </select>
						  </div>
						  
						  <div class="form-group">
						  <label for="usuarioEstado">Estado:</label>
						  <select id="usuarioEstado" name="usuarioEstado" class="form-control">
							
							<?php
							
								$query2 = "SELECT * FROM estado";
								$res2 = mysql_query($query2,$con) or die(mysql_error());
								
								while($row2 = mysql_fetch_assoc($res2)){
									
									echo '<option>'.$row2['desc'].'</option>';
									
								}
							
							?>
							
						  </select>
						  </div>
						  
						  <button type="submit" class="btn btn-primary">Próximo Passo -></button>
						  
						</form>
			
				</div>
			
			</div>
		
		</div>
		
		<script type="text/javascript">
			function fncidade(){
				
				var option1 = document.getElementById("options").value;
				
				
			
			}
		</script>

	</body>

</html>