<x-app-layout>
    <x-slot name="header">
        <h2 class="font-semibold text-xl text-gray-800 leading-tight">
            สวัสดี ,{{Auth::user()->name}}

    </x-slot>

    <div class="py-12">
        <div class="container">
            <div class="row">
                <div class="col-md-8">
                <div class="card">
                        <div class="card-header">แบบฟอร์มแก้ไข</div>
                        <div class="card-body">
                            <form action="{{url('/department/update/'.$department->id)}}" method="post">
                                @csrf
                                <div class="form-group">
                                    <label for="department_name">ต่ำแหน่งงาน</label>
                                    <input class="form-control" type="text" name="department_name" value="{{$department->department_name}}"/>
                                </div>
                                @error('department_name')
                                <div class="text-danger my-1">
                                    <span>{{ $message }}</span>
                                </div>
                                @enderror
                                <br />
                                <input class="btn btn-primary" type="submit" value="อัพเดต" />
                            </form>
                        </div>
                    </div>
                </div>
                </div>
            </div>
        </div>
    </div>

</x-app-layout>
