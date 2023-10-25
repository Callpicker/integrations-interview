var login_app = new Vue({
    el: '#register',
    data: {
      username: '',
    },
    methods:{
        register_request:function(){
            const csrf_token = document.querySelector('[name*="csrfmiddlewaretoken"]').value;
            let self = this;
            axios.post('/newuser', {
                username: this.username,
              },{
                headers:{"X-CSRFToken": csrf_token}
              })
              .then(function (response) {
                console.log(response);
                if (response.data.code == 200){
                    alert('User created');
                    self.username = '';
                }else{
                    alert('Error creating user!');
                }
              })
              .catch(function (error) {
                console.log(error);
              });
        }
    }
  });