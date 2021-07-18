<?php

namespace App\Http\Controllers;

use App\Models\Service;
use Carbon\Carbon;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class ServiceController extends Controller
{
    public function index()
    {
        $services = Service::paginate(5);
        return view('admin.service.index',compact('services'));
    }
    public function store(Request $request)
    {
        $request->validate(
            [
                'service_name'=>'required|unique:services|max:255',
                'service_image'=>'required|mimes:jpg,jpeg,png',
            ],
            [
                'service_name.required'=>"กรุณาป้อนซื่อบริการ",
                'service_name.max'=>"ห้ามป้อมเกิน 255 ตัวอักษร",
                'service_name.unique'=>"มีบริการนี้อยู่แล้ว",
                'service_image.required'=>"กรุณาใส่ภาพประกอบ"
            ]
        );

        //? เข้ารหัสรูป
        $service_image = $request->file('service_image');
        //? แปลงชื่อเป็นตัวเลขฐาน 16
        $name_gen = hexdec(uniqid());
        //? ดึงนามสกุลไฟล์รูป
        $img_ext = strtolower($service_image->getClientOriginalExtension());
        //? เอาชื่อไปที่แปลงมาต่อกับนามสกุลไฟล์รูป
        $img_name = $name_gen.'.'.$img_ext;

        //? บันทึกข้อมูลแบบ Eloquent
        $upload_location = 'image/services/';
        $full_path = $upload_location.$img_name;
        $service_image->move($upload_location,$img_name);

        Service::insert([
            "service_name" => $request->service_name,
            "service_image" => $full_path,
            "created_at" => Carbon::now()
        ]);

        return redirect()->back()->with('success','บันทึกเรียบร้อย');
    }
    public function edit($id)
    {
        $service = Service::find($id);
        return view('admin.service.edit',compact('service'));
    }
    public function update(Request $request,$id)
    {
        $request->validate(
            [
                'service_name'=>'required|max:255',
            ],
            [
                'service_name.max'=>"ห้ามป้อมเกิน 255 ตัวอักษร",
                'service_name.required'=>"กรุณาป้อนซื่อบริการ",
            ]
        );

        $service_image = $request->file('service_image');
        if ($service_image) {
            //? แปลงชื่อเป็นตัวเลขฐาน 16
            $name_gen = hexdec(uniqid());
            //? ดึงนามสกุลไฟล์รูป
            $img_ext = strtolower($service_image->getClientOriginalExtension());
            //? เอาชื่อไปที่แปลงมาต่อกับนามสกุลไฟล์รูป
            $img_name = $name_gen.'.'.$img_ext;

            //? บันทึกข้อมูลแบบ Eloquent
            $upload_location = 'image/services/';
            $full_path = $upload_location.$img_name;


            Service::find($id)->update([
                "service_name" => $request->service_name,
                "service_image" => $full_path,
                ]);

            $old_image = $request->old_image;
            unlink($old_image);
            $service_image->move($upload_location,$img_name);

            return redirect()->route('services')->with('success','อัพเดตภาพเรียบร้อย');
        }else{
            Service::find($id)->update([
                "service_name" => $request->service_name,
                ]);
            return redirect()->route('services')->with('success','อัพเดตชื่อเรียบร้อย');
        }
    }

    public function delete($id)
    {
        //? ลบภาพ
        $img = Service::find($id)->service_image;
        unlink($img);
        //? ลบข้อมูล
        Service::find($id)->Delete();
        return redirect()->back()->with('success','ลบข้อมูลเรียบร้อย');
    }

}
