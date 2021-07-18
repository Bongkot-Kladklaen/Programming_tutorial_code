import 'package:flutter/material.dart';
import 'package:form_field_validator/form_field_validator.dart';
import 'package:tutorial/model/profile.dart';

class RegisterScreen extends StatefulWidget {
  @override
  _RegisterScreenState createState() => _RegisterScreenState();
}

class _RegisterScreenState extends State<RegisterScreen> {

  final formKey = GlobalKey<FormState>();
  Profile profile = Profile(email: '', password: '');

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Register User"),
        ),
        body: Container(
            child: Padding(
          padding: const EdgeInsets.all(10),
          child: Form(
            key: formKey,
            child: SingleChildScrollView(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
              Text("Email", style: TextStyle(fontSize: 20)),
              TextFormField(
                validator: MultiValidator(
                  [
                    RequiredValidator(errorText: "กรุณาป้อน Email"),
                    EmailValidator(errorText: 'รูปแบบ Email ไม่ถูกต้อง')
                  ]
                ),
                keyboardType: TextInputType.emailAddress,
                onSaved: (email) => profile.email = email! ,
              ),
              Text("Password", style: TextStyle(fontSize: 20)),
              TextFormField(
                validator: RequiredValidator(errorText: "กรุณาป้อน Password"),
                obscureText: true,
                onSaved: (password)=> profile.password = password!,
              ),
              SizedBox(
                  width: double.infinity,
                  child: ElevatedButton(
                    onPressed: () {
                      if(formKey.currentState!.validate()){
                        formKey.currentState!.save();
                        formKey.currentState!.reset();
                      }
                    },
                    child: Text('Rigister'),
                  ))
            ]),
          )),
        )));
  }
}
