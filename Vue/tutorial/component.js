//Custom tag
Vue.component('kong',{
    data:function(){
        return{
            count:0
        }
    },
    template:'<button @click="count++">click: {{count}}</button>'
});

Vue.component('post',{
    props:['title'],
    template:'<h3>{{title}}</h3>'
});
Vue.component('showview',{
    props:{
        nameview:{
            type:String,
            required:true
        },
        view:{
            type:Number,
            default:0
        }
    },
    template:'<h3>{{nameview}} | {{view}}</h3>'
});

Vue.component('showcomment',{
    props:['commentpost'],
    template:'<h3>{{commentpost}}</h3>'
});

new Vue({
    el:'#vue-app',
    data:{
        newComment:'',
        comments:[
            'สวัสดีตอนเช้า','ทักทาย','ยินดีด้วย','สำบายดี'
        ]
    },
    methods:{
        addComment:function(){
            this.comments.push(this.newComment);
            this.newComment=''
        }
    }
});