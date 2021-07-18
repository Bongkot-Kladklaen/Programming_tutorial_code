<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About</title>
</head>
<body>
    <h1>Welcome to website</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quod, nobis!</p>

    <p>ที่อยู่ : {{ $address }}</p>
    <p>เบอร์ : {{ $tel }}</p>
    <p>อีเมล : {{ $email }}</p>
    <p>{{ $error }}</p>
    <p>{{ $status }}</p>

    <a href="{{ url('/')}}">Home</a>
    <a href="{{ route('about') }}">About</a>
    <a href="{{ route('admin') }}">Admin</a>
    <a href="{{ route('member') }}">Member</a>

</body>
</html>
