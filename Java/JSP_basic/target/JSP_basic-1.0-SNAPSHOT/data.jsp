<%--
  Created by IntelliJ IDEA.
  User: jaybong
  Date: 10/3/2021 AD
  Time: 16:06
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
<h1>First Name: <%= request.getParameter("fname")  %> </h1>
<h1>Last Name: <%= request.getParameter("lname")  %> </h1>
</body>
</html>
