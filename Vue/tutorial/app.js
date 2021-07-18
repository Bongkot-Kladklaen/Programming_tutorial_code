const app = new Vue({
    el: '#app',
    data:{
        name:"jay",
        age:20,
        url:"www.google.com",
        count: 0,
        foods:[],
        gender:"",
        job:"",
        like:false,
        product:['1','2','3'],
        employee:[
            { name:'a',age:20},
            { name:'b',age:22},
            { name:'c',age:40}
        ]
    },
    methods:{
        getName:function(){
            return this.name
        },
        setMsg:function(a){
            return this.name = a
        },
        addAge:function(){
            return this.age++
        },
        subtractAge:function() {
            return this.age--
        },
        addCount:function(){
            return this.count++
        }
    }
});