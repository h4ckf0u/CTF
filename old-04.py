<?php
//10000000,99999999
$filename = "rainbow.txt";
$file = fopen($filename, "w");
$fileContent;
if($file == false){
	echo("Eror in opening new file");
	exit();
}

for ($rand=10000000; $rand<=99999999; $rand++)
{
	$hash = $rand."salt_for_you";
	$fileContent = $hash;
	for($i=0;$i<500;$i++)
		$hash = sha1($hash);
	$fileContent = $fileContent.":".$hash."\n";
	fwrite($file, $fileContent);

}
fclose($file); 

?>
