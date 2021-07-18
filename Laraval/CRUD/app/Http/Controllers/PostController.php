<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use App\Models\Post;

class PostController extends Controller
{
    // public function getAllPost(){
    //     $posts = DB::table('posts')->get();
    //     return view('posts',compact('posts'));
    // }
    // public function addPost(){
    //     return view('add-post');
    // }

    // public function addPostSubmit(Request $request)
    // {
    //     DB::table('posts')->insert([
    //         'title' => $request->title,
    //         'body' => $request->body
    //     ]);
    //     return back()->with('post_created','Post has been create successfully!');
    // }

    // public function getPostById($id)
    // {
    //     $post = DB::table('posts')->where('id',$id)->first();
    //     return view('single-post',compact('post'));
    // }
    // public function deletPost($id)
    // {
    //     DB::table('posts')->where('id',$id)->delete();
    //     return back()->with('post_delete','Post has been delete successfully!');
    // }
    // public function editPost($id)
    // {
    //     $post = DB::table('posts')->where('id',$id)->first();
    //     return view('edit-post',compact('post'));
    // }
    // public function updatePost(Request $request)
    // {
    //     DB::table('posts')->where('id',$request->id)->update([
    //         'title' => $request->title,
    //         'body' => $request->body,
    //     ]);
    //     return back()->with('post_updated','Post has been updated successfully!');
    // }
    // public function innerJoinCaluse()
    // {
    //     $request = DB::table('users')
    //         ->join('posts','users.id','=','posts.user_id')
    //         ->select('users.name','posts.title','posts.body')
    //         ->get();
    //     return $request;
    // }
    // public function leftJionCaluse()
    // {
    //     $result = DB::table('users')
    //         ->leftJoin('posts','users.id','=','posts.user_id')
    //         ->get();
    //     return $result;
    // }
    // public function rightJoinClause()
    // {
    //     $result = DB::table('users')
    //         ->rightJoin('posts','users.id','=','posts.user_id')
    //         ->get();
    //     return $result;
    // }

    // public function getAllPostsUsingModel()
    // {
    //     $posts = Post::all();
    //     return $posts;
    // }

    //Eloquent CRUD 
    public function addPost()
    {
        return view('add-post');
    }
    public function createPost(Request $request)
    {
        $post = new Post();
        $post->title = $request->title;
        $post->body = $request->body;
        $post->save();
        return back()->with('post_created','Post has been created successfully!');
    }
    public function getPost()
    {
        $posts = Post::orderBy('id','DESC')->get();
        return view('posts',compact('posts'));
    }
    public function getPostById($id)
    {
        $post = Post::where('id',$id)->first();
        return view('single-post',compact('post'));
    }
    public function deletePost($id)
    {
        Post::where('id',$id)->delete();
        return back()->with('delete_post','Delete post successfully!');
    }
    public function editPost($id)       
    {
        $post = Post::find($id);
        return view('edit-post',compact('post'));
    }
    public function updatePost(Request $request)
    {
        $post = Post::find($request->id);
        $post->title = $request->title;
        $post->body = $request->body;
        $post->save();
        return back()->with('post_updated','Updated successfully!');
    }
}
