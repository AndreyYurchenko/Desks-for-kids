<?php
$login = filter_var(trim($_POST['login']),
FILTER_SANITIZE_STRING);
$name = filter_var(trim($_POST['name']),
FILTER_SANITIZE_STRING);
$pass = filter_var(trim($_POST['pass']),
FILTER_SANITIZE_STRING);

 if(mb_strlen($login) < 5 || mb_strlen($login) > 50) {
     echo "Недопустимая длина логина";
     exit();
 }else if(mb_strlen($name) < 2 || mb_strlen($name) > 30) {
    echo "Недопустимая длина имени";
    exit();
}else if(mb_strlen($pass) < 3 || mb_strlen($pass) > 32) {
    echo "Недопустимая длина пароля";
    exit();}

    $pass = md5($pass."lovephpandworld12345");

    $mysqli = new mysqli('localhost','root','','register-manga');
    $mysqli ->query("INSERT INTO `users` (`login`, `pass`, `name`)
    VALUES('$login', '$pass', '$name')");

    $mysqli->close();
    $main_url = 'http://localhost/filetext/Desks-for-kids/Desks-for-kids/phpsite/mangaregistretion.html';
    header('Location: '.$main_url);   

?>
