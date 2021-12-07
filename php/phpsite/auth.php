<?php
$login = filter_var(trim($_POST['login']),
FILTER_SANITIZE_STRING);
$pass = filter_var(trim($_POST['pass']),
FILTER_SANITIZE_STRING);

$pass = md5($pass."lovephpandworld12345");

$mysqli = new mysqli('localhost','root','','register-manga');
$result = $mysqli->query("SELECT * FROM `users` WHERE `login` = '$login' AND `pass` = '$pass'");
$user = $result->fetch_assoc();
if(count($user) == 0) {
    echo "Пользователь не найден";
    exit();
}
print_r($user);
exit();

$mysqli->close();
$main_url = 'http://localhost/filetext/Desks-for-kids/Desks-for-kids/phpsite/mangaregistretion.html';
header('Location: '.$main_url);
?>