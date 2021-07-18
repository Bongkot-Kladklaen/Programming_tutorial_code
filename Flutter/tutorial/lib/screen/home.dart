import 'package:flutter/material.dart';
import 'package:tutorial/screen/login.dart';
import 'package:tutorial/screen/register.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Register/Login"),
      ),
      body: Padding(
        padding: const EdgeInsets.fromLTRB(20,50,20,0),
        child: SingleChildScrollView(
          child: Column(
            children:[
              Image.asset("assets/images/logo.png",width: 200),
              SizedBox(
                width: double.infinity,
                child: ElevatedButton.icon(
                  onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (context) => RegisterScreen())), 
                  icon: Icon(Icons.add), 
                  label: Text("สร้างบัญชีผู้ใช้",style: TextStyle(fontSize: 20))
                )
              ),
              SizedBox(
                width: double.infinity,
                child: ElevatedButton.icon(
                  onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (context) => LoginScreen())), 
                  icon: Icon(Icons.login), 
                  label: Text("เข้าสู่ระบบ",style: TextStyle(fontSize: 20))
                )
              )
            ]
          ),
        ),
      ),
    );
  }
}