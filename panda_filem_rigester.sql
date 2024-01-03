-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2024 at 05:59 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `panda_filem_rigester`
--

-- --------------------------------------------------------

--
-- Table structure for table `panda_filem`
--

CREATE TABLE `panda_filem` (
  `tajuk_filem` text NOT NULL,
  `durasi` varchar(100) NOT NULL,
  `tarikh` varchar(100) NOT NULL,
  `jenis` text NOT NULL,
  `had_umur` int(11) NOT NULL,
  `negara` text NOT NULL,
  `pelakon` varchar(100) NOT NULL,
  `pengarah_filem` varchar(100) NOT NULL,
  `studio_prodaksi` varchar(100) NOT NULL,
  `sinopsis_filem` text NOT NULL,
  `jumlah_kutipan_Malaysia` int(100) NOT NULL,
  `jumlah_kutipan_luar` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `panda_filem`
--

INSERT INTO `panda_filem` (`tajuk_filem`, `durasi`, `tarikh`, `jenis`, `had_umur`, `negara`, `pelakon`, `pengarah_filem`, `studio_prodaksi`, `sinopsis_filem`, `jumlah_kutipan_Malaysia`, `jumlah_kutipan_luar`) VALUES
('', '', '', '1.horror\n2.thriller\n3.mystery', 13, 'USA', '1.Demián Bichir\n2.Taissa \n3.FarmigaJonas Bloquet', '\nCorin Hardy', 'Warner Bros. Pictures and New Line Cinema. ', 'A priest with a haunted past and a novice on the threshold of her final vows are sent by the Vatican to investigate the death of a young nun in Romania and confront a malevolent force in the form of a demonic nun.', 2147483647, 2147483647),
('', '', '', '1.horror\n2.thriller\n3.mystery', 13, 'USA', '1.Demián Bichir\n2.Taissa \n3.FarmigaJonas Bloquet', '\nCorin Hardy', 'Warner Bros. Pictures and New Line Cinema. ', 'A priest with a haunted past and a novice on the threshold of her final vows are sent by the Vatican to investigate the death of a young nun in Romania and confront a malevolent force in the form of a demonic nun.', 2147483647, 2147483647),
('', '', '', '1.horror\n2.thriller\n3.mystery', 13, 'USA', '1.Demián Bichir\n2.Taissa \n3.FarmigaJonas Bloquet', '\nCorin Hardy', 'Warner Bros. Pictures and New Line Cinema. ', 'A priest with a haunted past and a novice on the threshold of her final vows are sent by the Vatican to investigate the death of a young nun in Romania and confront a malevolent force in the form of a demonic nun.', 2147483647, 2147483647),
('kungfu panda', '1 jam 32 minit', '20 december 2008', '1.action\n2.comedy\n3.cartoon\n4.fiction', 0, 'USA', '1.Jack Black\n2.Ian McShane\n2.Angelina Jolie', '1.Mark Osborne\n2.John Stevenson', ' DreamWorks Animation ', 'To everyone\'s surprise, including his own, Po, an overweight, clumsy panda, is chosen as protector of the Valley of Peace. His suitability will soon be tested as the valley\'s arch-enemy is on his way.', 515556454, 564564564),
('Hachi: A Dog\'s Tale', '1 jam 33 minit', '21 Oktober 2010', '1.biography\n2.family\n3.drama', 0, 'USA', '1.Richard Gere\n2.Joan Allen\n3.Cary-Hiroyuki Tagawa', 'Lasse Hallström', 'Inferno Entertainment', 'A college professor bonds with an abandoned dog he takes into his home.', 2147483647, 2147483647),
('Hachi: A Dog\'s Tale', '1 jam 33 minit', '21 Oktober 2010', '1.biography\n2.family\n3.drama', 0, 'USA', '1.Richard Gere\n2.Joan Allen\n3.Cary-Hiroyuki Tagawa', 'Lasse Hallström', 'Inferno Entertainment', 'A college professor bonds with an abandoned dog he takes into his home.', 2147483647, 2147483647),
('the nun', '', '', '1.horror\n2.thriller\n3.mystery', 13, 'USA', '', '', '', '', 2147483647, 2147483647),
('the nun', '', '', '1.horror\n2.thriller\n3.mystery', 13, 'USA', '', '', '', '', 2147483647, 2147483647),
('Train to Busan', '2 jam', '2016', '1.action\n2.horror', 13, 'korea', '1.Gong Yoo\n2.Jung Yu-mi\n3.Ma Dong-seok', '\nSang-ho Yeon', ' Next Entertainment World.', 'While a zombie virus breaks out in South Korea, passengers struggle to survive on the train from Seoul to Busan.', 2147483647, 2147483647);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
