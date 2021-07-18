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
                            <form action="{{url('/service/update/'.$service->id)}}" method="post" enctype="multipart/form-data">
                                @csrf
                                <div class="form-group">
                                    <label for="service_name">ชื่อบริการ</label>
                                    <input class="form-control" type="text" name="service_name" value="{{$service->service_name}}"/>
                                </div>
                                @error('service_name')
                                <div class="text-danger my-1">
                                    <span>{{ $message }}</span>
                                </div>
                                @enderror

                                <div class="form-group">
                                    <label for="service_image">ภาพประกอบ</label>
                                    <input class="form-control" type="file" name="service_image" value="{{$service->service_image}}"/>
                                </div>
                                @error('service_name')
                                <div class="text-danger my-1">
                                    <span>{{ $message }}</span>
                                </div>
                                @enderror
                                <br />
                                <input type="hidden" name="old_image" value="{{$service->service_image}}">
                                <div class="form-group">
                                    <img src="{{ asset($service->service_image)}}" alt="" width="100px" height="100px">
                                </div>
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
