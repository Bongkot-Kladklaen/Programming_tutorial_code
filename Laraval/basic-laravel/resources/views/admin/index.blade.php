<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        $user = "bongkot";
        $arr = ["a","b","c"];
    ?>
    <h1>Admin {{ $user }}</h1>
    @if($user == "bongkot")
        <h2>เป็น admim</h2>
    @else
        <h2>ไม่เป็น admim</h2>
    @endif

    <ul>
    @foreach($arr as $item)
            <li>{{ $item }}</li>
    @endforeach
    </ul>
    @for($i = 0; $i < 10; $i++)
        <h3>{{ $i }}</h3>
    @endfor
</body>
</html>
