// To parse this JSON data, do
//
//     final exchangeRate = exchangeRateFromJson(jsonString);

import 'dart:convert';

ExchangeRate exchangeRateFromJson(String str) => ExchangeRate.fromJson(json.decode(str));

String exchangeRateToJson(ExchangeRate data) => json.encode(data.toJson());

class ExchangeRate {
    ExchangeRate({
        required this.base,
        required this.date,
        required this.rates,
    });

    String base;
    DateTime date;
    Map<String, double> rates;

    factory ExchangeRate.fromJson(Map<String, dynamic> json) => ExchangeRate(
        base: json["base"],
        date: DateTime.parse(json["date"]),
        rates: Map.from(json["rates"]).map((k, v) => MapEntry<String, double>(k, v.toDouble())),
    );

    Map<String, dynamic> toJson() => {
        "base": base,
        "date": "${date.year.toString().padLeft(4, '0')}-${date.month.toString().padLeft(2, '0')}-${date.day.toString().padLeft(2, '0')}",
        "rates": Map.from(rates).map((k, v) => MapEntry<String, dynamic>(k, v)),
    };
}
