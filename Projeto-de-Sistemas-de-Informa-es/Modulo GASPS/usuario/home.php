<?php 

	session_start();
	
	if(isset($_SESSION['usuario']) and isset($_SESSION['senha'])){
		
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
		
		$query10 = "SELECT * FROM marcacao WHERE marcacao.idUsuario=".$idUsuario." AND marcacao.presente='N'";
		$res10 = mysql_query($query10,$con) or die(mysql_error());
		
		if(mysql_num_rows($res10)>0){
			
			$_SESSION['mensagem_temfaltas'] = 'S';
			header('Location: http://localhost/GASPS/login.php');
			
		}
		else{
			
			if(isset($_SESSION['mensagem_temfaltas'])){
				
				unset($_SESSION['mensagem_temfaltas']);
				
			}
			
		}
		
		$query2 = "SELECT * FROM bairro WHERE bairro.id=".$idBairro;
		$res2 = mysql_query($query2,$con) or die(mysql_error());
		
		if(mysql_num_rows($res2)>0){
			
			while($row2 = mysql_fetch_assoc($res2)){
				
				$idRegional = $row2['idRegional'];
				
			}
			
		}
		
		$query3 = "SELECT * FROM postosaude WHERE postosaude.idBairro IN ( SELECT bairro.id FROM bairro WHERE bairro.idRegional=".$idRegional." )";
		$res3 = mysql_query($query3,$con) or die(mysql_error());
		
		$listaPostos = array();
		
		if(mysql_num_rows($res3)>0){
			
			while($row3 = mysql_fetch_assoc($res3)){
				
				$camposPostos = array($row3['id'],$row3['nome'],$row3['endereco'],$row3['numero'],$row3['idBairro']);
				
				$query4 = "SELECT medicovagas.* FROM medicovagas,dias 
				WHERE medicovagas.idDias=dias.id 
				AND CONCAT(dias.data,' ',medicovagas.horaMaxima)>NOW() 
				AND medicovagas.idPosto=".$row3['id']." 
				AND medicovagas.qtVagasRestantes".$preferencial.">0 
				AND DATE_FORMAT(dias.data,'%U') = DATE_FORMAT(NOW(),'%U')";
				
				$res4 = mysql_query($query4,$con) or die(mysql_error());
				
				$tiposMedico = array();
				
				if(mysql_num_rows($res4)>0){
					
					while($row4 = mysql_fetch_assoc($res4)){
						
						if(in_array($row4['idEspecialidade'],$tiposMedico)){}
						else{
							array_push($tiposMedico,$row4['idEspecialidade']);
						}
						
					}
					
				}
				
				array_push($camposPostos,$tiposMedico);
				
				array_push($listaPostos,$camposPostos);
				
			}
			
		}
		
		

	}
	
	else{
		
		header('Location: http://localhost/GASPS/login.php');
		
	}



?>


<html>

	<head>
		
		<title>Home - Usuário</title>
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
						<h2 class="txtquestao">Passo 1 - Escolha o posto de saúde e especialidade médica com a qual deseja se consultar:<h2>
					</div><br>
					
					<div class="row">
						
						<table class="table table-dark table-bordered">
						
						  <thead>
							<tr>
							  <th scope="col">#</th>
							  <th scope="col"><h3><img src="images/posto.png" width="100" height="100"> Posto de Saúde</h3></th>
							  <th scope="col"><h3><img src="images/medico.png" width="100" height="100"> Especialidade Médica</h3></th>
							</tr>
						  </thead>
						  
						  <tbody>
						    
							<?php foreach($listaPostos as $value){ ?>
							
							<tr>
							  <th scope="row"></th>
								  <td>
									<h4>
									<?php echo $value[1]; ?>
									<h4>
									<h5>
									<?php
									
									$query5 = "SELECT * FROM bairro WHERE bairro.id=".$value[4];
									$res5 = mysql_query($query5,$con) or die(mysql_error());
									
									while($row5 = mysql_fetch_assoc($res5)){
										
										$descBairro = $row5['desc'];
										
									}
									
									echo $value[2].", ".$value[3].", ".$descBairro;
									
									?>
									<h5>
								  </td>
							  <td>
							  <?php foreach($value[5] as $value2){ ?>
							  
							  <form class="bot2" action="dia.php" method="post">
							  
								<button type="submit" class="btn btn-primary bot" name="idEspecialidade" value="<?php 
									
									echo $value2." ".$value[0];
								
								?>"  ><?php 
							  
								$query7 = "SELECT * FROM especialidade WHERE especialidade.id=".$value2;
								$res7 = mysql_query($query7,$con) or die(mysql_error());
								
								while($row7 = mysql_fetch_assoc($res7)){
									
									$descMedico = $row7['desc'];
									
								}
							  
								echo $descMedico; ?>
								
								</button>
							  
							  </form>
							  
							  <?php } ?>
							  </td>
							</tr>
							
							<?php }; ?>
							
						  </tbody>
						  
						</table>
						
					</div>
			
				</div>
			
			</div>
		
		</div>

	</body>

</html>