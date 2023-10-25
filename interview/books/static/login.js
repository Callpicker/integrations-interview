var login_app = new Vue({
    el: '#login',
    data: {
      username: '',
    },
    methods:{
        login_request:function(){
            const csrf_token = document.querySelector('[name*="csrfmiddlewaretoken"]').value;
            axios.post('/checkusername', {
                username: this.username,
              },{
                headers:{"X-CSRFToken": csrf_token}
              })
              .then(function (response) {
                console.log(response);
                if (response.data.code == 200){
                    console.log('success');
                    window.location.href = "/main";
                }else{
                    alert('Error: ' + response.data.message);
                }
              })
              .catch(function (error) {
                console.log(error);
              });
        }
    }
  });