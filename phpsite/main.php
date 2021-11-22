<!doctype html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale-1">
   <link rel="stylesheet" href="style.css">
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
   <title> БцМаршал </title>
</head>
<body>
<div class="container d-flex flex-column flex-md-row justify-content-between">
        <a class="py-2" href="#">
        <span style="letter-spacing:0.5em;">БЦ МАРШАЛ</span>
        <a class="py-2 d-none d-md-inline-block" href="#">Tour</a>
        <a class="py-2 d-none d-md-inline-block" href="#">Product</a>
        <a class="py-2 d-none d-md-inline-block" href="#">Features</a>
        <a class="py-2 d-none d-md-inline-block" href="#">Enterprise</a>
        <a class="py-2 d-none d-md-inline-block" href="#">Support</a>
        <a class="py-2 d-none d-md-inline-block" href="#">Pricing</a>
        <a class="py-2 d-none d-md-inline-block" href="#">Cart</a>
      </div>
      <div class="container mt-5">
         <h3 class="mb-5">Наши офисы</h3>
         <div class="d-flex flex-wrap">
              <?php
              for($i = 0; $i < 4; $i++):
            ?>
            <div class="card mb-4 box-shadow">
            <img alt="" src="img/<?php echo ($i + 1)?>.jpeg" class="img-thumbnail">
            <div class="card-body">
            <h1 class="card-title pricing-card-title">$0 <small class="text-muted">/ mo</small></h1>
            <ul class="list-unstyled mt-3 mb-4">
              <li>Аааааааааа</li>
              <li>Куча места налитай братані</li>
              <li>support Андрей</li>
              <li>Help Андпей</li>
            </ul>
            <button type="button" class="btn btn-lg btn-block btn-outline-primary">Sign up for free</button>
          </div>
                </div>
               <?php endfor; ?>
               </div>
            </div>
</html>
