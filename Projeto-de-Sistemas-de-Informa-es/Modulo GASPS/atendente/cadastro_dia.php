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
		
		<title>Cadastro de Dia</title>
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
						<h2 class="txtquestao">Cadastro de Dia:<h2>
					</div><br>
					
					<form action="cadastro_dia2.php" method="post" >
					
						  <div class="form-group">
							<label for="dataAtend">Data de atendimento:</label>
							<input type="text" class="form-control" id="dataAtend" name="dataAtend" aria-describedby="emailHelp" placeholder="Digite aqui a data de atendimento" required>
							<small id="emailHelp" class="form-text text-muted">formato dd/mm/aaaa</small>
						  </div>
						  
						  <div class="form-group">
							<label for="qtVagasPref">Quantidade de vagas preferenciais:</label>
							<input type="text" class="form-control" id="qtVagasPref" name="qtVagasPref" placeholder="Digite aqui a quantidade de vagas destinadas a pessoas preferenciais" required>
						  </div>
						  
						  <div class="form-group">
							<label for="qtVagasCom">Quantidade de vagas não preferenciais:</label>
							<input type="text" class="form-control" id="qtVagasCom" name="qtVagasCom" placeholder="Digite aqui a quantidade de vagas destinadas a pessoas não preferenciais" required>
						  </div>
						  
						  <div class="form-group">
						  <label for="descEspec">Especialidade Médica:</label>
						  <select id="descEspec" name="descEspec" class="form-control">
							
							<?php
							
								$query2 = "SELECT especialidade.* FROM especialidade,postomedico 
								WHERE postomedico.idEspecialidade = especialidade.id
								AND postomedico.idPosto = ".$idPosto."";
								
								$res2 = mysql_query($query2,$con) or die(mysql_error());
								
								while($row2 = mysql_fetch_assoc($res2)){
									
									echo '<option>'.$row2['desc'].'</option>';
									
								}
							
							?>
							
						  </select>
						  </div>
						  
						  <div class="form-group">
							<label for="horaMax">Hora máxima</label>
							<input type="text" class="form-control" id="horaMax" name="horaMax" aria-describedby="emailHelp2" placeholder="Digite até que horas as fichas serão distribuídas" required>
							<small id="emailHelp2" class="form-text text-muted">formato hh:mm</small>
						  </div>
						  
						  <button type="submit" class="btn btn-primary">Cadastrar dia</button>
						  
						</form>
			
				</div>
			
			</div>
		
		</div>

	</body>

</html>