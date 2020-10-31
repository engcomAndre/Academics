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
		
		$dataAtend = $_POST['dataFecha'];
		
		$dia = substr($dataAtend,0,2);
		$mes = substr($dataAtend,3,2);
		$ano = substr($dataAtend,6,4);
		
		$dataAtend = $ano.'-'.$mes.'-'.$dia;
		
		$query2 = "UPDATE marcacao,medicovagas,dias SET marcacao.presente='N' 
		WHERE marcacao.idMedicoVagas = medicovagas.id 
		AND medicovagas.idDias = dias.id 
		AND dias.data<'".$dataAtend." 23:59:59' 
		AND marcacao.presente='C'";
		
		$res2 = mysql_query($query2,$con) or die(mysql_error());
		
		$query3 = "UPDATE marcacao,medicovagas,dias SET marcacao.presente='C' 
		WHERE marcacao.idMedicoVagas = medicovagas.id 
		AND medicovagas.idDias = dias.id 
		AND dias.data=date_add('".$dataAtend."', interval 1 day) 
		AND marcacao.presente='A'";
		
		$res3 = mysql_query($query3,$con) or die(mysql_error());
		
		$_SESSION['mensagem_cadastro_usuario'] = 'Fechamento rodado';
		header('Location: home.php');
		
	}
	
	else{
		
		header('Location: http://localhost/GASPS/loginatende.php');
		
	}



?>
