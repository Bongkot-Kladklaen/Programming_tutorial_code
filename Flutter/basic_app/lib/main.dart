import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'ExchangeRate.dart';
import "MoneyBox.dart";

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyHomePage(),
      theme: ThemeData(primarySwatch: Colors.amber),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  late ExchangeRate _dataFormAPI;
  @override
  void initState() {
    super.initState();
    getExchangeRate();

  }
  Future <ExchangeRate> getExchangeRate() async{
    var api = Uri.parse("http://api.exchangeratesapi.io/latest?access_key=d4b75efeb4df4998eab159b9e163bece&symbols=USD,THB");
    var response = await http.get(api);
    
    _dataFormAPI = exchangeRateFromJson(response.body);
    return _dataFormAPI;
  
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('อัตราแลกเปลี่ยนสกุลเงิน ')),
      body: FutureBuilder(
        future: getExchangeRate(),
        builder: (BuildContext context, AsyncSnapshot<dynamic> snapshot){
          if(snapshot.connectionState == ConnectionState.done){
            var result = snapshot.data;
            return Padding(
              padding: const EdgeInsets.all(8.0),
              child: Column(
                children: [
                  MoneyBox("สกุลเงิน (EUR)",1,Colors.lightBlue, 120),
                  SizedBox(height:10),
                  MoneyBox("THB",result.rates["THB"],Colors.lightBlue, 120),
                  SizedBox(height:10),
                  MoneyBox("USD",result.rates["USD"],Colors.lightBlue, 120),
                ],
              ),
            );
          }
          return LinearProgressIndicator();
      },)
    );
  }
}
