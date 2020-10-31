<?php

	session_start();

?>

<html>

<head>
<title>Impressão de Ficha</title>

<link href="dist/css/bootstrap.min.css" rel="stylesheet">
<link href="imprimeficha.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Barlow+Condensed" rel="stylesheet">

</head>

<body>

<a href="javascript://" onclick="javascript:window.print();"><h3 class="text-center">Clique aqui para imprimir</h3></a>

<div class="container">

	<div class="row border border-dark rounded">
		
		<div class="col-md" align="center">
	
			<h2 class="text-center">Senha de Atendimento:</h2>
			<h1 class="text-center"><?php echo $_SESSION['ficha']; ?></h1>
			<h3>--------------------------------------</h3>
			<h2>Local de Atendimento:<h3><?php echo $_SESSION['nomePosto']; ?><h3></h2>
			<h3>--------------------------------------</h3>
			<h2>Endereço:<h3><?php echo $_SESSION['enderecoPosto']; ?></h3></h2>
			<h3>--------------------------------------</h3>
			<h2>Especialidade Médica:<h3 class="fim"><?php echo $_SESSION['especialidade']; ?></h3></h2>
		
		</div>
		
	</div>
	
</div>

<h3 style="margin-top:20;" class="text-center">Levar e apresentar os seguintes documentos: <h3>
<h4 class="text-center"><?php echo $_SESSION['listaDocumentos']; ?><h4>

</body>


</html>