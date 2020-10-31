<?php 

	session_start();
	
	if(isset($_SESSION['usuario']) and isset($_SESSION['senha'])){
		
		$usuario = $_SESSION['usuario'];
		$senha = $_SESSION['senha'];
		
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
		
		$_SESSION['usuario'] = $usuario;
		$_SESSION['senha'] = $senha;
		
		$dataAtend = $_POST['dataAtend'];
		$qtVagasPref = $_POST['qtVagasPref'];
		$qtVagasCom = $_POST['qtVagasCom'];
		$descEspec = $_POST['descEspec'];
		$horaMax = $_POST['horaMax'];
		
		$qtVagas = $qtVagasCom+$qtVagasPref;
		
		$dia = substr($dataAtend,0,2);
		$mes = substr($dataAtend,3,2);
		$ano = substr($dataAtend,6,4);
		
		$dataAtend = $ano.'-'.$mes.'-'.$dia;
		
		$listaDias = array("Domingo","Segunda - Feira","Terca - Feira","Quarta - Feira","Quinta - Feira","Sexta - Feira","Sabado");
		
		$query2 = "SELECT * FROM dias WHERE dias.data='".$dataAtend."'";
		$res2 = mysql_query($query2,$con) or die(mysql_error());
		
		if(mysql_num_rows($res2)>0){
			
			//dia ja cadastrado na tabela dias
			
			while($row2 = mysql_fetch_assoc($res2)){
				
				$idDia = $row2['id'];
				
			}
			
		}
		else{
			
			//dia NAO está cadastrado na tabela dias
			
			$query3 = "SELECT DATE_FORMAT('".$dataAtend."', '%w') AS diaSemana";
			$res3 = mysql_query($query3,$con) or die(mysql_error());
			
			while($row3 = mysql_fetch_assoc($res3)){
				
				$diaSemana = $listaDias[$row3['diaSemana']];
				
			}
			
			$query4 = "INSERT INTO dias(dias.diaSemana,dias.data) VALUES('".$diaSemana."','".$dataAtend."')";
			$res4 = mysql_query($query4,$con) or die(mysql_error());
			
			$query5 = "SELECT MAX(dias.id) AS maxdia FROM dias";
			$res5 = mysql_query($query5,$con) or die(mysql_error());
			
			while($row5 = mysql_fetch_assoc($res5)){
				
				$idDia = $row5['maxdia'];
				
			}
			
		}
		
		$query6 = "SELECT especialidade.* FROM postomedico,especialidade 
		WHERE postomedico.idEspecialidade = especialidade.id 
		AND especialidade.desc='".$descEspec."' 
		AND postomedico.idPosto=".$idPosto."";
		
		$res6 = mysql_query($query6,$con) or die(mysql_error());
		
		while($row6 = mysql_fetch_assoc($res6)){
			
			$idEspecialidade = $row6['id'];
			
		}
		
		$query7 = "INSERT INTO medicovagas (idEspecialidade, idDias, idPosto, qtVagas, 
		qtVagasOcupadasS, qtVagasRestantesS, qtVagasOcupadasN, qtVagasRestantesN, horaMaxima) 
		VALUES (".$idEspecialidade.",".$idDia.",".$idPosto.",".$qtVagas.",0,".$qtVagasPref.",0,".$qtVagasCom.",'".$horaMax."')";
		
		$res7 = mysql_query($query7,$con) or die(mysql_error());
		
		$_SESSION['mensagem_cadastro_usuario'] = 'Dia e vagas cadastrados com sucesso';
		header('Location: home.php');
		
	}
	
	else{
		
		header('Location: http://localhost/GASPS/loginatende.php');
		
	}



?>
