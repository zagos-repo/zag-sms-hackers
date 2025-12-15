<?php 
header("Content-Type: application/json");

$file ="chat_messages.json";

if(!file_exists($file)){

    file_put_contents($file, json_encode([]));
}

$message = json_decode(file_get_contents($file),true);

$user = $_POST['user'] ?? "unknown";
$test = $_POST["test"] ?? "";
$time = date("Y-m-d H:i:s");

$message[] =[

   "user" => $user,
   "test" => $test,
   "time" => $time,

];

file_put_contents($file, json_decode($message, JSON_PRETTY_PRINT));

echo json_encode(["status"=> "ok"]);