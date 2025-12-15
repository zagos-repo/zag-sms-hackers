<?php 
header("Content-Type: application/json");


$file= "chat_message.json";

if(!file_exists($file)){

    echo json_decode([]);
    exit;

}
echo file_get_contents($file);