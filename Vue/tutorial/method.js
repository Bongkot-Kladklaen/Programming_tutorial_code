const app = new Vue({
    el: '#app',
    data:{
        newData:{
            empName: "",
            salary: 0
        },
        empGroup:[
            {empName:"a",salary:15000},
            {empName:"b",salary:15000}
        ]
    },
    methods:{
        addEmp:function(){
            this.empGroup.push({
                empName:this.newData.empName,
                salary:this.newData.salary
            })
            this.newData.empName = '';
            this.newData.salary = 0;
        },
        showMessage:function(){
            alert("เสร็จสิ้น");
        }

    },
    computed:{
        summation:function(){
            var sum = this.empGroup.reduce(function(value, data){
                return value + Number(data.salary);
            },0);
            return sum;
        }
    },
    watch:{
        summation:function(){
            this.showMessage();
        }
    }
});