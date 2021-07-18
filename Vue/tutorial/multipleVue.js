const post = new Vue({
    el:'#post',
    data:{
        title:'ส่งโปรเจค',
        message:'รายละเอียด'
    }
});

const comment = new Vue({
    el:'#comment',
    data:{
        text:'คอมเม้นอาการดีมาก',
    }
});

const like = new Vue({
    el:'#like',
    data:{
        likeCount:0,
        like:false

    },
    methods:{
        changelike:function(){
            if(!this.like){
                this.like = true;
                this.likeCount++;
            }else{
                this.like = false;
                this.likeCount--;
            }
        }
    }
});