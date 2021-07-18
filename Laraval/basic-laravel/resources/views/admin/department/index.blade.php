<x-app-layout>
    <x-slot name="header">
        <h2 class="font-semibold text-xl text-gray-800 leading-tight">
            สวัสดี ,{{Auth::user()->name}}

    </x-slot>

    <div class="py-12">
        <div class="container">
            <div class="row">
                <div class="col-md-8">
                    @if(session("success"))
                        <div class="alert alert-success">{{ session('success') }}</div>
                    @endif
                    <div class="card">
                        <div class="card-header">ตารางข้อมูลแผนก</div>
                        <div class="card-body">
                            <table class="table table-bordered">
                                <thead>
                                    <tr>
                                        <th scope="col">ลำดับ</th>
                                        <th scope="col">ชื่อ</th>
                                        <th scope="col">พนักงานที่เพิ่มข้อมูล</th>
                                        <th scope="col">เริ่มใช้งานระบบ</th>
                                        <th scope="col">แก้ไขข้อมูล & ลบ</th>
                                    </tr>
                                </thead>
                                <tbody>
                                @foreach($departments as $row)
                                    <tr>
                                        <th>{{$departments->firstItem()+$loop->index}}</th>
                                        <td>{{$row->department_name}}</td>
                                        <td>{{$row->user->name}}</td>
                                        <td>
                                        @if($row->created_at == NULL)
                                            ไม่มีข้อมูล
                                        @else
                                            {{Carbon\Carbon::parse($row->created_at)->diffForHumans()}}
                                        @endif
                                        </td>
                                        <td>
                                            <a href="{{url('/department/edit/'.$row->id)}}" class="btn btn-primary">แก้ไข</a>
                                            <a href="{{url('/department/softdelete/'.$row->id)}}" class="btn btn-danger">ลบ</a>
                                        </td>
                                    </tr>
                                @endforeach
                                </tbody>
                            </table>
                            {{ $departments->links() }}
                        </div>
                    </div>

                    @if(count($traskDepartment) > 0)
                    <div class="card my-2">
                        <div class="card-header">ถังขยะ</div>
                        <div class="card-body">
                            <table class="table table-bordered">
                                <thead>
                                    <tr>
                                        <th scope="col">ลำดับ</th>
                                        <th scope="col">ชื่อ</th>
                                        <th scope="col">พนักงานที่เพิ่มข้อมูล</th>
                                        <th scope="col">เริ่มใช้งานระบบ</th>
                                        <th scope="col">กู้ข้อมูล & ลบถาวร</th>
                                    </tr>
                                </thead>
                                <tbody>
                                @foreach($traskDepartment as $row)
                                    <tr>
                                        <th>{{$traskDepartment->firstItem()+$loop->index}}</th>
                                        <td>{{$row->department_name}}</td>
                                        <td>{{$row->user->name}}</td>
                                        <td>
                                        @if($row->created_at == NULL)
                                            ไม่มีข้อมูล
                                        @else
                                            {{Carbon\Carbon::parse($row->created_at)->diffForHumans()}}
                                        @endif
                                        </td>
                                        <td>
                                            <a href="{{url('/department/restore/'.$row->id)}}" class="btn btn-primary">กู้ข้อมูล</a>
                                            <a href="{{url('/department/delete/'.$row->id)}}" class="btn btn-danger">ลบถาวร</a>
                                        </td>
                                    </tr>
                                @endforeach
                                </tbody>
                            </table>
                            {{ $traskDepartment->links() }}
                        </div>
                    </div>
                    @endif

                </div>
                <div class="col-md-4">
                <div class="card">
                        <div class="card-header">แบบฟอร์ม</div>
                        <div class="card-body">
                            <form action="{{ route('addDepartment') }}" method="post">
                                @csrf
                                <div class="form-group">
                                    <label for="department_name">ต่ำแหน่งงาน</label>
                                    <input class="form-control" type="text" name="department_name" />
                                </div>
                                @error('department_name')
                                <div class="text-danger my-1">
                                    <span>{{ $message }}</span>
                                </div>
                                @enderror
                                <br />
                                <input class="btn btn-primary" type="submit" value="บันทึก" />
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</x-app-layout>
