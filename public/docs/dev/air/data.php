<?php

$file = "/home/projects/skop.eu/public/docs/dev/air/data.json";
$json = file_get_contents('php://input');
// file_put_contents($file, json_encode($_SERVER));
file_put_contents($file, $json)

 ?>
