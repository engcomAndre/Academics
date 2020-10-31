<?php 

	session_start();
	
	if(isset($_SESSION['mensagem_cadastro_usuario'])){
		
		echo'
		<div class="alert alert-success" role="alert">'.
		  $_SESSION['mensagem_cadastro_usuario'].
		'</div>';
		
		unset($_SESSION['mensagem_cadastro_usuario']);
		
	}
	
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
				
				$_SESSION['idPosto'] = $idPosto;
				
			}
			
		}
	
	}
	
	else{
		
		header('Location: http://localhost/GASPS/loginatende.php');
		
	}



?>


<html>

	<head>
		
		<title>Home - Atendente</title>
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
					</div>
					
					</div>
				
				</div>
				
				<div class="col-sm c2">
				
					<div class="row c2-l1 rounded border border-secondary">
						<h2 class="txtquestao">Escolha uma opção:<h2>
					</div><br>
					
					<?php 
					
						$query2 = "SELECT * FROM postosaude WHERE postosaude.id=".$idPosto."";
						$res2 = mysql_query($query2,$con) or die(mysql_error());
						
						while($row2 = mysql_fetch_assoc($res2)){
							
							$nomePosto = $row2['nome'];
							
						}
					
					
					?>
					
					<div class="row">
						<h3 class="txtquestao"><?php echo $nomePosto; ?><h3>
					</div><br>
					
					<div class="row" style="background-color:#ffffff">
						
						<table class="table table-bordered">
						  <thead>
							<tr>
							  <th scope="col">#</th>
							  <th scope="col">Usuário</th>
							  <th scope="col">Posto</th>
							</tr>
						  </thead>
						  <tbody>
							<tr>
							  <th scope="row">1</th>
							  <td><a href="cadastro_usuario.php">Cadastrar usuário</a></td>
							  <td><a href="cadastro_dia.php">Cadastrar dia de atendimento</a></td>
							</tr>
							<tr>
							  <th scope="row">2</th>
							  <td><a href="fechamento.php">Fechamento de dia</a></td>
							  <td><a href="cadastro_especialidade.php">Cadastrar Especialidade Médica no Posto</a></td>
							</tr>
                            <tr>
                                <th scope="row">3</th>
                                <td><a href="imprimirfichas.php">Imprimir Fichas</a></td>
                                <td><a href="verificarfichas.php">Chamada de Fichas</a></td>
                            </tr>
						  </tbody>
						</table>
						
					</div>
			
				</div>
			
			</div>
		
		</div>

	</body>

</html>