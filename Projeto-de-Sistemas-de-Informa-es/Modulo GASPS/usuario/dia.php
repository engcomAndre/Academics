<?php 

	session_start();
	
	if(isset($_SESSION['mensagemFicha'])){
		
		echo'
		<div class="alert alert-danger" role="alert">
			Vagas esgotaram um pouco antes de você escolher o dia. Favor tentar novamente escolhendo outra data.
		</div>
		';
		
	}

	if(isset($_SESSION['usuario']) and isset($_SESSION['senha'])){
		
		if(isset($_POST['idEspecialidade'])){
			
			
			$usuario = $_SESSION['usuario'];
			$senha = $_SESSION['senha'];
			
			$con = mysql_connect('localhost','root','');
			mysql_select_db("gaspsbd");
		
			$query = "SELECT * FROM usuario WHERE usuario.login='".$usuario."' AND usuario.senha='".$senha."'";
			$res = mysql_query($query,$con) or die(mysql_error());
			
			if(mysql_num_rows($res)>0){
				
				while($row=mysql_fetch_assoc($res)){
					
					$nome = $row['nome'];
					$sexo = $row['sexo'];
					$idBairro = $row['idBairro'];
					$preferencial = $row['preferencial'];
					$idUsuario = $row['id'];
					
				}
				
			}
			
			$lista = array(explode(" ",$_POST['idEspecialidade']));
			
			$idEspecialidade = intval($lista[0][0]);
			$idPosto = intval($lista[0][1]);
			
			$listaDias = array();
			
			$query2 = "SELECT medicovagas.*,dias.data,dias.diaSemana FROM medicovagas,dias 
			WHERE medicovagas.idDias=dias.id 
			AND CONCAT(dias.data,' ',medicovagas.horaMaxima)>NOW() 
			AND medicovagas.idPosto=".$idPosto." 
			AND medicovagas.idEspecialidade=".$idEspecialidade." 
			AND medicovagas.qtVagasRestantes".$preferencial.">0 
			AND DATE_FORMAT(dias.data,'%U') = DATE_FORMAT(NOW(),'%U')";
			
			
			$res2 = mysql_query($query2,$con) or die(mysql_error());
			
			if(mysql_num_rows($res2)>0){
				
				while($row2 = mysql_fetch_assoc($res2)){
					
					$query3 = "SELECT marcacao.* FROM marcacao,medicovagas,dias 
					WHERE marcacao.idMedicoVagas = medicovagas.id 
					AND medicovagas.idDias = dias.id 
					AND DATE_FORMAT(dias.data,'%U') = DATE_FORMAT('".$row2['data']."','%U') 
					AND marcacao.idUsuario=".$idUsuario."";
					
					$res3 = mysql_query($query3,$con) or die(mysql_error());
					
					if(mysql_num_rows($res3)>0){
						//ja existem marcacoes na semana.
					}
					else{
						array_push($listaDias,$row2);
					}
			
					
				}
				
			}
			
			else{
				
				echo'
				<div class="alert alert-danger" role="alert">
					Infelizmente não há vagas disponíveis no momento para a especialidade médica escolhida.
				</div>
				';
				
			}
			
		}
		
		else{
			
			$_SESSION['usuario'] = $usuario;
			$_SESSION['senha'] = $senha;
			header('Location: http://localhost/GASPS/usuario/home.php');
			
		}
		
	}
	else{
		
		header('Location: http://localhost/GASPS/login.php');
		
	}

?>


<html>

	<head>
		
		<title>Dia - Usuário</title>
		<link href="dist/css/bootstrap.min.css" rel="stylesheet">
		<link href="dia.css" rel="stylesheet">
		<link href="https://fonts.googleapis.com/css?family=Barlow+Condensed" rel="stylesheet">
		
	</head>

	<body>

		<div class="container">
		
			<div class="row">
			
				<div class="col-md-auto">
				
					<div class="col-md-auto c1 rounded" style="background-color:
					<?php 
					
						if($sexo=='M'){
								
								echo "#3333cc";
							}
						else{
							
							echo "#ff0066";
							
						}
					
					
					?>">
					<div class="row c1-logo">
						<img src="images/logo2.png" width="315" height="100">
					</div>
				
					<div class="row c1-l1">
						
						<img src="<?php 
						
							if($sexo=='M'){
								
								echo "images/homem.png";
							}
							else{
								
								echo "images/mulher.png";
								
							}
						
						?>">
						
					</div>
					
					<div class="row c1-l2">
						<h3 class="txtnome"><?php echo $nome; ?></h3>
					</div>
					
					<div class="row">
						<a href="logout.php"><button type="button" class="btn btn-danger btn-lg">Sair do sistema</button></a>
					</div><br>
					
					<div class="row">
						<a href="home.php"><button type="button" class="btn btn-success btn-lg">Voltar à tela de seleção <br>de postos e especialidades</button></a>
					</div>
					
					</div>
				
				</div>
				
				<div class="col-sm c2">
				
					<div class="row c2-l1 rounded border border-secondary">
						<h2 class="txtquestao">Passo 2 - Escolha o dia da consulta:<h2>
					</div><br>
					
					<div class="row rounded dias border border-secondary">
					
						<?php 
						
						$_SESSION['usuario'] = $usuario;
						$_SESSION['senha'] = $senha;
						
						foreach($listaDias as $value){ ?>
						
						<form action="ficha.php" method="post">
						
						<button type="submit" class="btn btn-primary" name="idMedicoVagas" value="<?php
						
							echo $value['id'];
						
						?>"
						><h3><?php echo $value['diaSemana']; ?></h3><h4>Dia <?php 
						
						$data = date_create($value['data']);
						echo date_format($data, 'd/m/Y');
						
						?></h4></button>
						
						</form>
						
						<?php } ?>
					
					</div>
			
				</div>
			
			</div>
		
		</div>

	</body>

</html>