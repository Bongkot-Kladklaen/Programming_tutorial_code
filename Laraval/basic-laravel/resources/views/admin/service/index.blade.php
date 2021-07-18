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
                        <div class="card-header">ตารางข้อมูลบริการ</div>
                        <div class="card-body">
                            <table class="table table-bordered">
                                <thead>
                                    <tr>
                                        <th scope="col">ลำดับ</th>
                                        <th scope="col">ภาพประกอบ</th>
                                        <th scope="col">ชื่อบริการ</th>
                                        <th scope="col">created_at</th>
                                        <th scope="col">แก้ไขข้อมูล & ลบ</th>
                                    </tr>
                                </thead>
                                <tbody>
                                @foreach($services as $row)
                                    <tr>
                                        <th>{{$services->firstItem()+$loop->index}}</th>
                                        <td>
                                            <img src="{{ asset($row->service_image) }}" alt="" width="70px" height="70">
                                        </td>
                                        <td>{{$row->service_name}}</td>
                                        <td>
                                        @if($row->created_at == NULL)
                                            ไม่มีข้อมูล
                                        @else
                                            {{Carbon\Carbon::parse($row->created_at)->diffForHumans()}}
                                        @endif
                                        </td>
                                        <td>
                                            <a href="{{url('/service/edit/'.$row->id)}}" class="btn btn-primary">แก้ไข</a>
                                            <a href="{{url('/service/delete/'.$row->id)}}" class="btn btn-danger" onclick="return confirm('ต้องการลบหรือไม่?')">ลบ</a>
                                        </td>
                                    </tr>
                                @endforeach
                                </tbody>
                            </table>
                            {{ $services->links() }}
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                <div class="card">
                        <div class="card-header">แบบฟอร์มบริการ</div>
                        <div class="card-body">
                            <form action="{{ route('addService') }}" method="post" enctype="multipart/form-data">
                                @csrf
                                <div class="form-group">
                                    <label for="service_name">ชื่อบริการ</label>
                                    <input class="form-control" type="text" name="service_name" />
                                </div>
                                @error('service_image')
                                <div class="text-danger my-1">
                                    <span>{{ $message }}</span>
                                </div>
                                @enderror

                                <div class="form-group">
                                    <label for="service_image">ภาพประกอบ</label>
                                    <input class="form-control" type="file" name="service_image" />
                                </div>
                                @error('service_image')
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
