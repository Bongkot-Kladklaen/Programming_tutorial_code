<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Department;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Redirect;

class DepartmentController extends Controller
{
    public function index()
    {
        $departments = Department::paginate(5);
        $traskDepartment = Department::onlyTrashed()->paginate(5);
        // $departments = DB::table('departments')->paginate(3);
        return view('admin.department.index',compact('departments','traskDepartment'));
    }
    public function store(Request $request)
    {
        $request->validate(
            [
                'department_name'=>'required|unique:departments|max:255'
            ],
            [
                'department_name.required'=>"กรุณาป้อนซื่อแผนก",
                'department_name.max'=>"ห้ามป้อมเกิน 255 ตัวอักษร",
                'department_name.unique'=>"มีแผนกนี้อยู่แล้ว",
            ]
        );

        //? บันทึกข้อมูลแบบ Eloquent
        $department = new Department;
        $department->department_name = $request->department_name;
        $department->user_id = Auth::user()->id;
        $department->save();

        //? บันึกข้อมูลแบบ Query bilder
        // $data = array();
        // $data['department_name'] = $request->department_name;
        // $data['user_id'] = Auth::user()->id;
        // DB::table('departments')->insert($data);

        return redirect()->back()->with('success','บันทึกเรียบร้อย');
    }

    public function edit($id)
    {
        $department = Department::find($id);
        return view('admin.department.edit',compact('department'));
    }
    public function update(Request $request,$id)
    {
        $request->validate(
            [
                'department_name'=>'required|unique:departments|max:255'
            ],
            [
                'department_name.required'=>"กรุณาป้อนซื่อแผนก",
                'department_name.max'=>"ห้ามป้อมเกิน 255 ตัวอักษร",
                'department_name.unique'=>"มีแผนกนี้อยู่แล้ว",
            ]
        );
        $update = Department::find($id)->update([
            'department_name' => $request->department_name,
            'user_id' => Auth::user()->id
        ]);
        return redirect()->route('department')->with('success','อัพเดตเรียบร้อย');
    }
    public function softdelete($id)
    {
        Department::find($id)->delete();
        return redirect()->back()->with('success','ลบเรียบร้อยแล้ว');
    }
    public function restore($id){
        Department::withTrashed()->find($id)->restore();
        return redirect()->back()->with('success','กูข้อมูลเรียบร้อย');
    }
    public function delete($id)
    {
        Department::onlyTrashed()->find($id)->forceDelete();
        return redirect()->back()->with('success','ลบข้อมูลถาวรเรียบร้อย');
    }
}
