<?php 

	session_start();

	if(isset($_SESSION['usuario']) and isset($_SESSION['senha'])){
		
		if(isset($_POST['idMedicoVagas'])){
		
			$usuario = $_SESSION['usuario'];
			$senha = $_SESSION['senha'];
			
			$_SESSION['usuario'] = $usuario;
			$_SESSION['senha'] = $senha;
			
			$con = mysql_connect('localhost','root','');
			mysql_select_db("gaspsbd");
		
			$query = "SELECT * FROM usuario WHERE usuario.login='".$usuario."' AND usuario.senha='".$senha."'";
			$res = mysql_query($query,$con) or die(mysql_error());
			
			if(mysql_num_rows($res)>0){
				
				while($row=mysql_fetch_assoc($res)){
					
					$nome = $row['nome'];
					$sexo = $row['sexo'];
					$idBairro = $row['idBairro'];
					$idUsuario = $row['id'];
					$preferencial = $row['preferencial'];		
					
				}
				
			}
			
			$idMedicoVagas = $_POST['idMedicoVagas'];
			
			$query14 = "SELECT * FROM marcacao WHERE marcacao.idUsuario=".$idUsuario." AND marcacao.idMedicoVagas=".$idMedicoVagas."";
			$res14 = mysql_query($query14,$con) or die(mysql_error());
			
			if(mysql_num_rows($res14)>0){
				
				header('Location: home.php');
				
			}
			
			if($row['preferencial']=='S'){
				$tipo = "GSPP";
			}
			else{
				$tipo = "GSPC";
			}
			
			$query2 = "SELECT * FROM medicovagas WHERE medicovagas.id=".$idMedicoVagas." AND medicovagas.qtVagasRestantes".$preferencial.">0";
			$res2 = mysql_query($query2,$con) or die(mysql_error());
			
			if(mysql_num_rows($res2)>0){
				
				$query3 = "UPDATE medicovagas SET medicovagas.qtVagasRestantes".$preferencial."= medicovagas.qtVagasRestantes".$preferencial."-1,
				medicovagas.qtVagasOcupadas".$preferencial."= medicovagas.qtVagasOcupadas".$preferencial."+1 WHERE medicovagas.id=".$idMedicoVagas."";
				$res3 = mysql_query($query3,$con) or die(mysql_error());
				
				$query4 = "SELECT * FROM medicovagas WHERE medicovagas.id=".$idMedicoVagas."";
				$res4 = mysql_query($query4,$con) or die(mysql_error());
				
				while($row4 = mysql_fetch_assoc($res4)){
					
					$numVaga = $row4['qtVagasOcupadas'.$preferencial];
					$idEspecialidade = $row4['idEspecialidade'];
					
				}
				
				$query5 = "INSERT INTO ficha(ficha.idMedicoVagas,ficha.tipo,ficha.numero) VALUES(".$idMedicoVagas.",'".$tipo."',".$numVaga.")";
				$res5 = mysql_query($query5,$con) or die(mysql_error());
				
				$query6 = "SELECT MAX(ficha.id) AS idFicha FROM ficha ";
				$res6 = mysql_query($query6,$con) or die(mysql_error());
				
				while($row6 = mysql_fetch_assoc($res6)){
					
					$idFicha = $row6['idFicha'];
					
				}
				
				$query7 = "INSERT INTO marcacao(marcacao.idUsuario,marcacao.idMedicoVagas,marcacao.idFicha,marcacao.presente)
				VALUES(".$idUsuario.",".$idMedicoVagas.",".$idFicha.",'A')";
				$res7 = mysql_query($query7,$con) or die(mysql_error());
				
				while($row2=mysql_fetch_assoc($res2)){
					
					$idPosto = $row2['idPosto'];
					
				}
				
				$query8 = "SELECT * FROM postosaude WHERE postosaude.id=".$idPosto."";
				$res8 = mysql_query($query8,$con) or die(mysql_error());
				
				while($row8 = mysql_fetch_assoc($res8)){
					
					$nomePosto = $row8['nome'];
					$enderecoPosto = $row8['endereco'];
					$numeroPosto = $row8['numero'];
					$idBairroPosto = $row8['idBairro'];
					
				}
				
				$query9 = "SELECT * FROM bairro WHERE id=".$idBairroPosto."";
				$res9 = mysql_query($query9,$con) or die(mysql_error());
				
				while($row9 = mysql_fetch_assoc($res9)){
					
					$bairroPosto = $row9['desc'];
					$idRegionalPosto = $row9['idRegional'];
					
				}
				
				$query10 = "SELECT * FROM especialidade WHERE id=".$idEspecialidade."";
				$res10 = mysql_query($query10,$con) or die(mysql_error());
				
				while($row10 = mysql_fetch_assoc($res10)){
					
					$especialidade = $row10['desc'];
					
				}
				
				$query13 = "SELECT cidade.desc,estado.sigla FROM regional,cidade,estado WHERE cidade.id = regional.idCidade 
							AND estado.id = regional.idEstado AND regional.id=".$idRegionalPosto."";
				
				$res13 = mysql_query($query13,$con) or die(mysql_error());
				
				while($row13=mysql_fetch_assoc($res13)){
					
					$descCidade = $row13['desc'];
					$siglaEstado = $row13['sigla'];
					
				}
				
				$_SESSION['nomePosto'] = $nomePosto;
				$_SESSION['enderecoPosto'] = $enderecoPosto.", ".$numeroPosto." - ".$bairroPosto.", ".$descCidade." - ".$siglaEstado;
				$_SESSION['especialidade'] = $especialidade;
				
				
			}
			else{
				
				$_SESSION['mensagemFicha'] = "Infelizmente as fichas se encerraram pouco antes de você escolher o dia. 
				Favor tente de novo escolhendo uma nova data.";
				
				header('Location: http://localhost/GASPS/usuario/dia.php');
				
			}
		
		}
		else{
			
			header('Location: http://localhost/GASPS/usuario/home.php');
			
		}
		
	}
	else{
		
		header('Location: http://localhost/GASPS/login.php');
		
	}

?>

<html>

	<head>
		
		<title>Ficha - Usuário</title>
		
		<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
		<script src="assets/js/vendor/popper.min.js"></script>
		<script src="dist/js/bootstrap.min.js"></script>
		<script src="assets/js/docs.min.js"></script>
		<script src="assets/js/ie-emulation-modes-warning.js"></script>
		<script src="dist/js/bootstrap.js"></script>
		
		<link href="dist/css/bootstrap.min.css" rel="stylesheet">
		<link href="ficha.css" rel="stylesheet">
		<link href="https://fonts.googleapis.com/css?family=Barlow+Condensed" rel="stylesheet">
		
	</head>

	<body>

		<div class="container">
		
			<div class="row">
			
				<div class="col-md-auto">
				
					<div class="col-md-auto c1 rounded"style="background-color:
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
						<h2 class="txtquestao">Passo 3 - Imprima ou salve sua senha no celular e apresente-a no local 
						e no dia do atendimento junto com a documentação listada abaixo:<h2>
					</div><br>
					
					<div class="row">
					
						<div class="col-sm rouded c231">
						
							<div class="col-md-auto">
								
								<div class="border border-dark" style="background-color:#ffffff">
							
									<h4 class="text-center txc1">Sua senha de atendimento é:</h4>
									<h1 class="text-center txc2"><?php echo $tipo."-".$numVaga; ?></h1>
									<?php $_SESSION['ficha']=$tipo."-".$numVaga; ?>
							
								</div>
								
								<div class="dropdown" style="margin-top:20; margin-bottom:20">
								  <button class="btn btn-primary dropdown-toggle btn-lg" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" autofocus>
									<img src="images/printer.png" width="50" height="50"> Imprimir ou baixar
								  </button>
								  <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
									<a class="dropdown-item" href="imprimeficha.php"><h5>Imprimir</h5></a>
									<div class="dropdown-divider border border-dark"></div>
									<a class="dropdown-item" href="#"><h5>Baixar Senha</h5></a>
								  </div>
								</div>
								
							</div>
						
						</div>
						
						<div class="col-sm c232">
							
							<div class="row border border-dark" style="background-color:#ffffff">
							<div style="margin-left:10;margin-right:10">
							<h3 style="margin-top:10"><img src="images/doc.png" width="50" height="50"> Documentos Necessários:</h3>
							
							<?php 
							
								$query11 = "SELECT * FROM medicovagasdocumento WHERE medicovagasdocumento.idMedicoVagas=".$idMedicoVagas."";
								$res11 = mysql_query($query11,$con) or die(mysql_error());
								
								$listaDocumentos = "";
								
								while($row11 = mysql_fetch_assoc($res11)){
									
									$query12 = "SELECT * FROM documentos WHERE documentos.id=".$row11['idDocumento']."";
									$res12 = mysql_query($query12,$con) or die(mysql_error());
									
									while($row12 = mysql_fetch_assoc($res12)){
										
										$listaDocumentos = $listaDocumentos.$row12['descricao'].", ";
										echo "<h4>".$row12['descricao']."</h4>";
										
									}
									
								}
								
								$_SESSION['listaDocumentos'] = $listaDocumentos;
							
							?>
							
							</div>
							</div>
							
							<div class="row border border-dark" style="background-color:#ffffff; margin-top:20">
							<div style="margin-left:10;margin-right:10">
							
							<table class="table">
							  <tbody>
								<tr>
								  <td><h4>Local de atendimento:</h4></td>
								  <td><h5><?php echo $nomePosto; ?></h5></td>
								</tr>
								<tr>
								  <td><h4>Endereço:</h4></td>
								  <td><h5><?php echo $enderecoPosto.", ".$numeroPosto." - ".$bairroPosto.", ".$descCidade." - ".$siglaEstado; ?></h5></td>
								</tr>
								<tr>
								  <td><h4>Especialidade Médica:</h4></td>
								  <td><h5><?php echo $especialidade; ?></h5></td>
								</tr>
							  </tbody>
							</table>
							
							</div>
							</div>
							
								
						</div>
					
					</div>
			
				</div>
			
			</div>
		
		</div>
		
		
		<script>
			function printMe() {
				var mywindow = window.open('', 'PRINT', 'height=800,width=800');

				mywindow.document.write("<html></html>");

				mywindow.document.close(); // necessary for IE >= 10
				mywindow.focus(); // necessary for IE >= 10*/

				mywindow.print();
				mywindow.close();

				return true;
			}
			
		</script>
		

	</body>

</html>