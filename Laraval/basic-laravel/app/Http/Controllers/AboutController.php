<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class AboutController extends Controller
{
    function index(){

        $address = "123 กรุงเทพ, ประเทศไทย";
        $tel = "1234567890";
        $email = 'jayobac@gmail.com';

        //? ส่งค่าไปแสดงที่ View แบบ array
        // return view("about",['address'=>$address, 'tel'=> $tel, 'email'=>$email]);

        //? ส่งค่าไปแสดงที่ View แบบ compact()
        // return view('about',compact('address','tel','email'));

        //? ส่งค่าไปแสดงที่ View แบบ with()
        return view('about')
            ->with('address',$address)
            ->with('tel',$tel)
            ->with('email',$email)
            ->with('error','404 Not Found')
            ->with('status','success');
    }
}
