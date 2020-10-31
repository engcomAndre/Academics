<?php 

	session_start();
	
	if(isset($_SESSION['usuario']) and isset($_SESSION['senha'])){
		
		$usuario = $_SESSION['usuario'];
		$senha = $_SESSION['senha'];
		
		$_SESSION['usuario'] = $usuario;
		$_SESSION['senha'] = $senha;
		
		if(isset($_POST['usuarioCidade'])){}
		else{
			
			header('Location: cadastro_usuario.php');
			
		}
		
		if($_POST['usuarioCidade']=='Escolha uma opção...' and ($_POST['usuarioCidade2']==NULL or $_POST['usuarioCidade2']=='') ){
			
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
		
		$usuarioNome = $_SESSION['usuarioNome'] ;
		$usuarioLogin = $_SESSION['usuarioLogin'];
		$usuarioRG = $_SESSION['usuarioRG']; 
		$usuarioCPF = $_SESSION['usuarioCPF']; 
		$usuarioSUS = $_SESSION['usuarioSUS']; 
		$usuarioTel1 = $_SESSION['usuarioTel1']; 
		$usuarioTel2 = $_SESSION['usuarioTel2'];
		$usuarioSexo = $_SESSION['usuarioSexo'];
		$usuarioPref = $_SESSION['usuarioPref'];
		$usuarioEstado = $_SESSION['usuarioEstado'];
		$idUsuarioEstado = $_SESSION['idUsuarioEstado'];
		
		
		if(isset($_POST['usuarioCidade2']) and $_POST['usuarioCidade2']!=NULL and $_POST['usuarioCidade2']!=''){
			//cidade nao cadastrada
			
			$query4 = "INSERT INTO cidade(cidade.desc,cidade.idEstado) VALUES('".$_POST['usuarioCidade2']."',".$_SESSION['idUsuarioEstado'].")";
			$res4 = mysql_query($query4,$con) or die(mysql_error());
			
			$_SESSION['usuarioCidade'] = $_POST['usuarioCidade2'];
		}
		else{
			//cidade ja cadastrada
			$_SESSION['usuarioCidade'] = $_POST['usuarioCidade'];
		}
		
		$_SESSION['usuarioNome'] = $usuarioNome;
		$_SESSION['usuarioLogin'] = $usuarioLogin;
		$_SESSION['usuarioRG'] = $usuarioRG;
		$_SESSION['usuarioCPF'] = $usuarioCPF;
		$_SESSION['usuarioSUS'] = $usuarioSUS;
		$_SESSION['usuarioTel1'] = $usuarioTel1;
		$_SESSION['usuarioTel2'] = $usuarioTel2;
		$_SESSION['usuarioSexo'] = $usuarioSexo;
		$_SESSION['usuarioPref'] = $usuarioPref;
		$_SESSION['usuarioEstado'] = $usuarioEstado;
		$_SESSION['idUsuarioEstado'] = $idUsuarioEstado;
		
		if($_SESSION['usuarioSexo']=='Masculino'){
			
			$_SESSION['usuarioSexo'] = 'M';
			
		}
		else{
			
			$_SESSION['usuarioSexo'] = 'F';
			
		}
		
		if($_SESSION['usuarioPref']=='Sim'){
			
			$_SESSION['usuarioPref'] = 'S';
			
		}
		
		else{
			
			$_SESSION['usuarioPref'] = 'N';
			
		}
		
	
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
					
					<form action="cadastro_usuario4.php" method="post" >
					
						  
						  <div class="form-group">
						  <label for="usuarioBairro">Bairro:</label>
						  <select id="usuarioBairro" name="usuarioBairro" class="form-control">
						  <option>Escolha uma opção...</option>
							
							<?php
							
								$query2 = "SELECT * FROM cidade WHERE cidade.desc='".$_SESSION['usuarioCidade']."' AND cidade.idEstado=".$_SESSION['idUsuarioEstado']."";
								$res2 = mysql_query($query2,$con) or die(mysql_error());
								
								while($row2 = mysql_fetch_assoc($res2)){
									
									$_SESSION['idUsuarioCidade'] = $row2['id'];
									
								}
								
								$query3 = "SELECT * FROM regional WHERE regional.idCidade=".$_SESSION['idUsuarioCidade']." AND regional.idEstado=".$_SESSION['idUsuarioEstado']."";
								$res3 = mysql_query($query3,$con) or die(mysql_error());
								
								while($row3 = mysql_fetch_assoc($res3)){
									
									array_push($listaRegional,$row2['id']);
									
									$query5 = "SELECT * FROM bairro WHERE bairro.idRegional=".$row3['id']."";
									$res5 = mysql_query($query5,$con) or die(mysql_error());
									
									while($row5 = mysql_fetch_assoc($res5)){
										
										echo '<option>'.$row5['desc'].'</option>';
										
									};
									
								}
							
							?>
							
						  </select>
						  </div>
						  
						  <div class="form-group">
							<label for="usuarioBairro2">Não encontrou o bairro?:</label>
							<input type="text" class="form-control" id="usuarioBairro2" name="usuarioBairro2" placeholder="Digite aqui o bairro">
							<select id="usuarioRegional" name="usuarioRegional" class="form-control">
							<option>Escolha uma regional...</option>
							
							<?php
							
							$query6 = "SELECT * FROM regional WHERE regional.idCidade=".$_SESSION['idUsuarioCidade']." AND regional.idEstado=".$_SESSION['idUsuarioEstado']."";
							$res6 = mysql_query($query6,$con) or die(mysql_error());
							
							while($row6 = mysql_fetch_assoc($res6)){

								echo '<option>'.$row6['desc'].'</option>';
									
							}
							
							?>
							
							
							</select>
						  </div>
						  
						  <button type="submit" class="btn btn-primary">Cadastrar Usuário</button>
						  
						  
					</form>
					
			
				</div>
			
			</div>
		
		</div>
		
	</body>

</html>