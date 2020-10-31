-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 18-Dez-2017 às 10:37
-- Versão do servidor: 10.1.28-MariaDB
-- PHP Version: 5.6.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gaspsbd`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `administrador`
--

CREATE TABLE `administrador` (
  `id` int(11) NOT NULL,
  `login` varchar(50) NOT NULL,
  `senha` varchar(20) NOT NULL,
  `idPosto` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `administrador`
--

INSERT INTO `administrador` (`id`, `login`, `senha`, `idPosto`, `nome`) VALUES
(0, 'admin', '1234', 1, 'admin'),
(0, 'admin1', '1234', 2, 'admin2'),
(3, 'admin3', '1234', 1, 'admin3');

-- --------------------------------------------------------

--
-- Estrutura da tabela `atendente`
--

CREATE TABLE `atendente` (
  `id` int(11) NOT NULL,
  `nome` varchar(200) NOT NULL,
  `sexo` varchar(3) NOT NULL,
  `endereco` varchar(200) NOT NULL,
  `usuario` varchar(100) NOT NULL,
  `senha` varchar(100) NOT NULL,
  `telefone1` varchar(20) NOT NULL,
  `telefone2` varchar(20) NOT NULL,
  `idPosto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `atendente`
--

INSERT INTO `atendente` (`id`, `nome`, `sexo`, `endereco`, `usuario`, `senha`, `telefone1`, `telefone2`, `idPosto`) VALUES
(1, 'Carlos Alberto', 'M', '', 'carlos.atende', 'b', '(85) 9999-0000', '(85) 0000-9999', 1),
(0, 'atende1', 'M', 'rua 1', 'atende1', '123456', '00000000', '00000000', 2);

-- --------------------------------------------------------

--
-- Estrutura da tabela `bairro`
--

CREATE TABLE `bairro` (
  `id` int(11) NOT NULL,
  `desc` varchar(100) NOT NULL,
  `idRegional` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `bairro`
--

INSERT INTO `bairro` (`id`, `desc`, `idRegional`) VALUES
(1, 'Vila Velha', 1),
(2, 'Barra do Ceara', 1),
(3, 'Jardim Iracema', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `cidade`
--

CREATE TABLE `cidade` (
  `id` int(11) NOT NULL,
  `desc` varchar(100) NOT NULL,
  `idEstado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `cidade`
--

INSERT INTO `cidade` (`id`, `desc`, `idEstado`) VALUES
(1, 'Fortaleza', 6);

-- --------------------------------------------------------

--
-- Estrutura da tabela `dias`
--

CREATE TABLE `dias` (
  `id` int(11) NOT NULL,
  `diaSemana` varchar(30) NOT NULL,
  `data` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `dias`
--

INSERT INTO `dias` (`id`, `diaSemana`, `data`) VALUES
(1, 'Segunda - Feira', '2017-12-11'),
(2, 'Terca - Feira', '2017-12-12'),
(3, 'Quarta - Feira', '2017-12-13'),
(4, 'Quinta - Feira', '2017-12-14'),
(5, 'Sexta - Feira', '2017-12-15'),
(6, 'Sabado', '2017-12-16'),
(7, 'Domingo', '2017-12-17'),
(8, 'Segunda - Feira', '2017-12-18'),
(9, 'Terca - Feira', '2017-12-19'),
(10, 'Quarta - Feira', '2017-12-20'),
(11, 'Quinta - Feira', '2017-12-21'),
(12, 'Quinta Feira', '2017-12-21'),
(13, 'Sabado', '2017-12-30'),
(14, 'Quarta-Feira', '2018-01-17');

-- --------------------------------------------------------

--
-- Estrutura da tabela `documentos`
--

CREATE TABLE `documentos` (
  `id` int(11) NOT NULL,
  `descricao` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `documentos`
--

INSERT INTO `documentos` (`id`, `descricao`) VALUES
(1, 'Documento de Identificacao com foto'),
(2, 'CPF'),
(3, 'Certidao de Nascimento'),
(4, 'Cartao do SUS'),
(5, 'Comprovante de residencia');

-- --------------------------------------------------------

--
-- Estrutura da tabela `especialidade`
--

CREATE TABLE `especialidade` (
  `id` int(11) NOT NULL,
  `desc` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 ROW_FORMAT=COMPACT;

--
-- Extraindo dados da tabela `especialidade`
--

INSERT INTO `especialidade` (`id`, `desc`) VALUES
(1, 'Odontologia'),
(2, 'Pediatria'),
(3, 'Cardiologia'),
(4, 'Clinica Geral'),
(5, 'Dermatologia'),
(6, 'Endocrinologia'),
(7, 'Fisioterapia'),
(8, 'Gastroenterologia'),
(9, 'Ginecologia'),
(10, 'Homeopatia'),
(11, 'Nutrição'),
(12, 'Oftalmologia');

-- --------------------------------------------------------

--
-- Estrutura da tabela `estado`
--

CREATE TABLE `estado` (
  `id` int(11) NOT NULL,
  `desc` varchar(50) NOT NULL,
  `sigla` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `estado`
--

INSERT INTO `estado` (`id`, `desc`, `sigla`) VALUES
(1, 'Acre', 'AC'),
(2, 'Alagoas', 'AL'),
(3, 'Amapá', 'AP'),
(4, 'Amazonas', 'AM'),
(5, 'Bahia', 'BA'),
(6, 'Ceará', 'CE'),
(7, 'Distrito Federal', 'DF'),
(8, 'Espírito Santo', 'ES'),
(9, 'Alagoas', 'AL'),
(10, 'Goiás', 'GO'),
(11, 'Maranhão', 'MA'),
(12, 'Mato Grosso', 'MT'),
(13, 'Mato Grosso do Sul', 'MS'),
(14, 'Minas Gerais', 'MG'),
(15, 'Pará', 'PA'),
(16, 'Paraíba', 'PB'),
(17, 'Paraná', 'PR'),
(18, 'Pernambuco', 'PE'),
(19, 'Piauí', 'PI'),
(20, 'Rio de Janeiro', 'RJ'),
(21, 'Rio Grande do Norte', 'RN'),
(22, 'Rio Grande do Sul', 'RS'),
(23, 'Rondônia', 'RO'),
(24, 'Roraima', 'RR'),
(25, 'Santa Catarina', 'SC'),
(26, 'São Paulo', 'SP'),
(27, 'Sergipe', 'SE'),
(28, 'Tocantins', 'TO');

-- --------------------------------------------------------

--
-- Estrutura da tabela `ficha`
--

CREATE TABLE `ficha` (
  `id` int(11) NOT NULL,
  `idMedicoVagas` int(11) NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `numero` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `ficha`
--

INSERT INTO `ficha` (`id`, `idMedicoVagas`, `tipo`, `numero`) VALUES
(11, 3, 'GSPC', 2),
(12, 6, 'GSPC', 6),
(13, 6, 'GSPC', 7),
(14, 1, 'GSPC', 23),
(15, 6, 'GSPC', 8);

-- --------------------------------------------------------

--
-- Estrutura da tabela `marcacao`
--

CREATE TABLE `marcacao` (
  `id` int(11) NOT NULL,
  `idUsuario` int(11) NOT NULL,
  `idMedicoVagas` int(11) NOT NULL,
  `idFicha` int(11) NOT NULL,
  `presente` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `marcacao`
--

INSERT INTO `marcacao` (`id`, `idUsuario`, `idMedicoVagas`, `idFicha`, `presente`) VALUES
(11, 4, 3, 11, 'A'),
(12, 2, 6, 12, 'A'),
(13, 2, 6, 13, 'A'),
(14, 3, 1, 14, 'A'),
(15, 5, 6, 15, 'A'),
(16, 1, 1, 15, 'A');

-- --------------------------------------------------------

--
-- Estrutura da tabela `medicovagas`
--

CREATE TABLE `medicovagas` (
  `id` int(11) NOT NULL,
  `idEspecialidade` int(11) NOT NULL,
  `idDias` int(11) NOT NULL,
  `idPosto` int(11) NOT NULL,
  `qtVagas` int(11) NOT NULL,
  `qtVagasOcupadasS` int(11) NOT NULL,
  `qtVagasRestantesS` int(11) NOT NULL,
  `qtVagasOcupadasN` int(11) NOT NULL,
  `qtVagasRestantesN` int(11) NOT NULL,
  `horaMaxima` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `medicovagas`
--

INSERT INTO `medicovagas` (`id`, `idEspecialidade`, `idDias`, `idPosto`, `qtVagas`, `qtVagasOcupadasS`, `qtVagasRestantesS`, `qtVagasOcupadasN`, `qtVagasRestantesN`, `horaMaxima`) VALUES
(1, 1, 8, 1, 40, 0, 0, 23, 17, '10:00:00'),
(2, 2, 8, 1, 50, 0, 16, 10, 24, '10:00:00'),
(3, 3, 8, 1, 30, 2, 12, 1, 15, '10:00:00'),
(4, 4, 8, 2, 30, 0, 15, 0, 15, '10:00:00'),
(5, 5, 9, 2, 40, 0, 20, 0, 20, '10:00:00'),
(6, 2, 9, 1, 20, 8, 12, 1, 20, '10:00:00'),
(7, 3, 9, 1, 20, 0, 20, 1, 20, '10:00:00'),
(8, 4, 9, 1, 20, 0, 20, 1, 20, '10:00:00'),
(9, 2, 14, 1, 20, 0, 20, 0, 20, '23:00:00');

-- --------------------------------------------------------

--
-- Estrutura da tabela `medicovagasdocumento`
--

CREATE TABLE `medicovagasdocumento` (
  `idMedicoVagas` int(11) NOT NULL,
  `idDocumento` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `medicovagasdocumento`
--

INSERT INTO `medicovagasdocumento` (`idMedicoVagas`, `idDocumento`) VALUES
(1, 1),
(2, 1),
(3, 2),
(1, 2),
(4, 3);

-- --------------------------------------------------------

--
-- Estrutura da tabela `postomedico`
--

CREATE TABLE `postomedico` (
  `idPosto` int(11) NOT NULL,
  `idEspecialidade` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `postomedico`
--

INSERT INTO `postomedico` (`idPosto`, `idEspecialidade`) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 4),
(2, 5);

-- --------------------------------------------------------

--
-- Estrutura da tabela `postosaude`
--

CREATE TABLE `postosaude` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `endereco` varchar(100) NOT NULL,
  `numero` int(11) NOT NULL,
  `idBairro` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `postosaude`
--

INSERT INTO `postosaude` (`id`, `nome`, `endereco`, `numero`, `idBairro`) VALUES
(1, 'Posto de Saude Lineu Juca', 'Via Parque Vila Velha II', 101, 1),
(2, 'Posto de Saude Casemiro Lima Filho', 'Avenida Francisco Sa', 6449, 2);

-- --------------------------------------------------------

--
-- Estrutura da tabela `regional`
--

CREATE TABLE `regional` (
  `id` int(11) NOT NULL,
  `desc` varchar(100) NOT NULL,
  `idCidade` int(11) NOT NULL,
  `idEstado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `regional`
--

INSERT INTO `regional` (`id`, `desc`, `idCidade`, `idEstado`) VALUES
(1, 'Regional GASPS 1', 1, 6);

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `sexo` varchar(3) NOT NULL,
  `cartaoSUS` varchar(100) NOT NULL,
  `RG` varchar(50) NOT NULL,
  `idBairro` int(11) NOT NULL,
  `CPF` varchar(50) NOT NULL,
  `login` varchar(100) NOT NULL,
  `senha` varchar(30) NOT NULL,
  `preferencial` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `usuario`
--

INSERT INTO `usuario` (`id`, `nome`, `sexo`, `cartaoSUS`, `RG`, `idBairro`, `CPF`, `login`, `senha`, `preferencial`) VALUES
(1, 'Luiz Otavio Sousa', 'M', '123456789', '123456789', 1, '123.456.789-00', 'LuizOtavio1.gasps', 'a', 'N'),
(2, 'admin', '', '', '', 1, '', 'admin', '1234', 'S'),
(3, 'Paciente 1', 'I', '123456123', '123456789', 1, '12345612311', 'Paciente1', '123456', 'N'),
(4, 'Paciente2', 'i', '132465123456', '123456131', 2, '123456123', 'Paciente2', '123465', 'S'),
(5, 'Paciente3', 'M', '12345612311', '12345612341', 1, '12346512311', 'Paciente3', '123456', 'S');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bairro`
--
ALTER TABLE `bairro`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cidade`
--
ALTER TABLE `cidade`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dias`
--
ALTER TABLE `dias`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `documentos`
--
ALTER TABLE `documentos`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `especialidade`
--
ALTER TABLE `especialidade`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `estado`
--
ALTER TABLE `estado`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ficha`
--
ALTER TABLE `ficha`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `marcacao`
--
ALTER TABLE `marcacao`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `medicovagas`
--
ALTER TABLE `medicovagas`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `postosaude`
--
ALTER TABLE `postosaude`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `regional`
--
ALTER TABLE `regional`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bairro`
--
ALTER TABLE `bairro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `cidade`
--
ALTER TABLE `cidade`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `dias`
--
ALTER TABLE `dias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `documentos`
--
ALTER TABLE `documentos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `especialidade`
--
ALTER TABLE `especialidade`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `estado`
--
ALTER TABLE `estado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `ficha`
--
ALTER TABLE `ficha`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `marcacao`
--
ALTER TABLE `marcacao`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `medicovagas`
--
ALTER TABLE `medicovagas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `postosaude`
--
ALTER TABLE `postosaude`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `regional`
--
ALTER TABLE `regional`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
