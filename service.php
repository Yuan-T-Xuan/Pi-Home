<?php
header("Content-Type: text/plain;charset=utf-8");
//first, read the file
$fromfile = fopen("state.txt", "r");
$count = 0;
$data_file = array();
while($count < 3) {
	$aline = fgets($fromfile);
	$data_file[$count] = trim($aline);
	$count = $count + 1;
}
fclose($fromfile);
$fromfile = fopen("state2.txt", "r");
while($count < 13) {
	$aline = fgets($fromfile);
	$data_file[$count] = trim($aline);
	$count = $count + 1;
}
fclose($fromfile);

if($_GET["askfor"] == "values") {
	echo "{\"temperature\":" . $data_file[0] . 
		 ",\"moisture\":" . $data_file[1] . 
		 ",\"distance\":" . $data_file[2] . 
		 "}";
} elseif($_GET["askfor"] == "init") {
	echo "{\"temperature\":" . $data_file[0] . 
		 ",\"moisture\":" . $data_file[1] . 
		 ",\"distance\":" . $data_file[2] . 
		 ",\"air_mode\":\"" . $data_file[3] . "\"" . 
		 ",\"air_on\":\"" . $data_file[4] . "\"" . 
		 ",\"air_threshold\":" . $data_file[5] . 
		 ",\"air_start\":\"" . $data_file[6] . "\"" . 
		 ",\"air_stop\":\"" . $data_file[7] . "\"" . 
		 ",\"dry_mode\":\"" . $data_file[8] . "\"" . 
		 ",\"dry_on\":\"" . $data_file[9] . "\"" . 
		 ",\"dry_threshold\":" . $data_file[10] . 
		 ",\"dry_start\":\"" . $data_file[11] . "\"" . 
		 ",\"dry_stop\":\"" . $data_file[12] . "\"" . 
		 "}";
} else {
	switch($_POST["req_type"]) {
		case "air_mode":
			$data_file[3] = $_POST["air_mode"];
			$tofile = fopen("state2.txt", "w");
			$str2write = $data_file[3] . "\n";
			$i = 4;
			while($i < 13) {
				$str2write = $str2write . $data_file[$i] . "\n";
				$i = $i + 1;
			}
			fwrite($tofile, $str2write);
			fclose($tofile);
			break;
		case "air_on_off":
			$data_file[4] = $_POST["air_on_off"];
			$tofile = fopen("state2.txt", "w");
			$str2write = $data_file[3] . "\n";
			$i = 4;
			while($i < 13) {
				$str2write = $str2write . $data_file[$i] . "\n";
				$i = $i + 1;
			}
			fwrite($tofile, $str2write);
			fclose($tofile);
			break;
		case "air_threshold":
			$data_file[5] = $_POST["air_threshold"];
			$tofile = fopen("state2.txt", "w");
			$str2write = $data_file[3] . "\n";
			$i = 4;
			while($i < 13) {
				$str2write = $str2write . $data_file[$i] . "\n";
				$i = $i + 1;
			}
			fwrite($tofile, $str2write);
			fclose($tofile);
			break;
		case "air_start":
			$data_file[6] = $_POST["air_start"];
			$tofile = fopen("state2.txt", "w");
			$str2write = $data_file[3] . "\n";
			$i = 4;
			while($i < 13) {
				$str2write = $str2write . $data_file[$i] . "\n";
				$i = $i + 1;
			}
			fwrite($tofile, $str2write);
			fclose($tofile);
			break;
		case "air_stop":
			$data_file[7] = $_POST["air_stop"];
			$tofile = fopen("state2.txt", "w");
			$str2write = $data_file[3] . "\n";
			$i = 4;
			while($i < 13) {
				$str2write = $str2write . $data_file[$i] . "\n";
				$i = $i + 1;
			}
			fwrite($tofile, $str2write);
			fclose($tofile);
			break;
		case "dry_mode":
			$data_file[8] = $_POST["dry_mode"];
			$tofile = fopen("state2.txt", "w");
			$str2write = $data_file[3] . "\n";
			$i = 4;
			while($i < 13) {
				$str2write = $str2write . $data_file[$i] . "\n";
				$i = $i + 1;
			}
			fwrite($tofile, $str2write);
			fclose($tofile);
			break;
		case "dry_on_off":
			$data_file[9] = $_POST["dry_on_off"];
			$tofile = fopen("state2.txt", "w");
			$str2write = $data_file[3] . "\n";
			$i = 4;
			while($i < 13) {
				$str2write = $str2write . $data_file[$i] . "\n";
				$i = $i + 1;
			}
			fwrite($tofile, $str2write);
			fclose($tofile);
			break;
		case "dry_threshold":
			$data_file[10] = $_POST["dry_threshold"];
			$tofile = fopen("state2.txt", "w");
			$str2write = $data_file[3] . "\n";
			$i = 4;
			while($i < 13) {
				$str2write = $str2write . $data_file[$i] . "\n";
				$i = $i + 1;
			}
			fwrite($tofile, $str2write);
			fclose($tofile);
			break;
		case "dry_start":
			$data_file[11] = $_POST["dry_start"];
			$tofile = fopen("state2.txt", "w");
			$str2write = $data_file[3] . "\n";
			$i = 4;
			while($i < 13) {
				$str2write = $str2write . $data_file[$i] . "\n";
				$i = $i + 1;
			}
			fwrite($tofile, $str2write);
			fclose($tofile);
			break;
		case "dry_stop":
			$data_file[12] = $_POST["dry_stop"];
			$tofile = fopen("state2.txt", "w");
			$str2write = $data_file[3] . "\n";
			$i = 4;
			while($i < 13) {
				$str2write = $str2write . $data_file[$i] . "\n";
				$i = $i + 1;
			}
			fwrite($tofile, $str2write);
			fclose($tofile);
			break;
	}
}
?>
