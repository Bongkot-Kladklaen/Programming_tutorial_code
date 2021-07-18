<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\AboutController;
use App\Http\Controllers\AdminController;
use App\Http\Controllers\DepartmentController;
use App\Http\Controllers\MemberController;
use App\Http\Controllers\ServiceController;
use App\Models\User;
use Illuminate\Support\Facades\DB;
/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
})->name('home');

Route::get('/about',[AboutController::class,'index'])->name('about');
Route::get('/admin',[AdminController::class,'index'])->name('admin')->middleware('check');
Route::get('/member',[MemberController::class,'index'])->name('member');


Route::middleware(['auth:sanctum', 'verified'])->get('/dashboard', function () {
    //? ใช้ Eloquent เพื่อดึงข้อมูลจาก database มาแสดงในกรณีมี model
    // $users = User::all();

    //? ใช้ Query Builder เพื่อดึงข้อมูลจาก database มาแสดงในการณีไม่มี model
    $users = DB::table('users')->get();

    return view('dashboard',compact('users'));
})->name('dashboard');

Route::middleware(['auth:sanctum', 'verified'])->group(function(){
    //Department
    Route::get('/department/all',[DepartmentController::class,'index'])->name('department');
    Route::post('/department/add',[DepartmentController::class,'store'])->name('addDepartment');
    Route::get('/department/edit/{id}',[DepartmentController::class,'edit'])->name('edit');
    Route::post('/department/update/{id}',[DepartmentController::class,'update'])->name('update');

    Route::get('/department/softdelete/{id}',[DepartmentController::class,'softdelete'])->name('softdelete');
    Route::get('/department/restore/{id}',[DepartmentController::class,'restore'])->name('restore');
    Route::get('/department/delete/{id}',[DepartmentController::class,'delete'])->name('delete');

    //Service
    Route::get('/service/all',[ServiceController::class,'index'])->name('services');
    Route::post('/service/add',[ServiceController::class,'store'])->name('addService');
    Route::get('/service/edit/{id}',[ServiceController::class,'edit'])->name('edit');
    Route::post('/service/update/{id}',[ServiceController::class,'update'])->name('update');
    Route::get('/service/delete/{id}',[ServiceController::class,'delete'])->name('delete');




});
