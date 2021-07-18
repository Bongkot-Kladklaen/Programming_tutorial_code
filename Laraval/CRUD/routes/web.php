<?php

use App\Http\Controllers\MailController;
use App\Http\Controllers\PaginationController;
use App\Http\Controllers\PostController;
use App\Http\Controllers\UploadController;
use App\Http\Controllers\UserController;
use Illuminate\Support\Facades\Route;
use App\PaymentGateway\Payment;

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
    // App::setLocale($locale);
    return view('welcome');
});

// Route::get('/posts',[PostController::class,'getAllPost'])->name('post.getallpost');
// Route::get('/add-post',[PostController::class,'addPost'])->name('post.add');
// Route::post('/add-post',[PostController::class,'addPostSubmit'])->name('post.addsubmit');
// Route::get('/posts/{id}',[PostController::class,'getPostById'])->name('post.getbyid');
// Route::get('/delete-post/{id}',[PostController::class,'deletPost'])->name('post.delete');
// Route::get('/edit-post/{id}',[PostController::class,'editPost'])->name('post.edit');
// Route::post('/update-post',[PostController::class,'updatePost'])->name('post.update');
// Route::get('/inner-join',[PostController::class,'innerJoinCaluse'])->name('post.innerjoin');
// Route::get('/left-join',[PostController::class,'leftJionCaluse'])->name('post.leftjoin');
// Route::get('/right-join',[PostController::class,'rightJoinClause'])->name('post.rightjoin');
// Route::get('/all-posts',[PostController::class,'getAllPostsUsingModel'])->name('post.getallpostusingmodel');
// Route::get('/users',[PaginationController::class,'allUsers']);
// Route::get('/upload',[UploadController::class,'uploadForm']);
// Route::post('/upload',[UploadController::class,'uploadFile'])->name('upload.uploadfile');

// Route::get('/payment',function(){
//     return Payment::process();
// });

// Route::get('/send-email',[MailController::class,'sendEmail']);

//Eloquent CRUD
Route::get('/add-post',[PostController::class,'addPost']);
Route::post('/create-post',[PostController::class,'createPost'])->name('post.addsubmit');
Route::get('/posts',[PostController::class,'getPost']);
Route::get('/posts/{id}',[PostController::class,'getPostById']);
Route::get('/delete-post/{id}',[PostController::class,'deletePost']);
Route::get('/edit-post/{id}',[PostController::class,'editPost']);
Route::post('/update-post',[PostController::class,'updatePost'])->name('post.update');

//Eloquent Relationship one to one
Route::get('/add-user',[UserController::class,'insertRecord']);
Route::get('/get-phone/{id}',[UserController::class,'fetchPhoneByUser']);