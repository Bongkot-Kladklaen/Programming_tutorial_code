import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

// Container ต้นแบบ
class MoneyBox extends StatelessWidget {
  String title;
  double amount;
  Color color;
  double sizeContainer;

  MoneyBox(this.title,this.amount,this.color,this.sizeContainer);
  
  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(10.0),
        decoration: BoxDecoration(color: color, borderRadius: BorderRadius.circular(20)),
        height: sizeContainer,
        child: Row(
          crossAxisAlignment: CrossAxisAlignment.center,
          children:[
            Text('$title',style: TextStyle(fontSize: 25,fontWeight: FontWeight.bold)),
            Expanded(child: Text('${NumberFormat("#,###.##").format(amount)}',style: TextStyle(fontSize: 20,fontWeight: FontWeight.bold),textAlign: TextAlign.right,))
          ]
        ),
    );
  }
}