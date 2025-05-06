
        function sendEmail() {
            let params = {
                name: document.getElementById("name").value,
                email: document.getElementById("email").value,
                subject: document.getElementById("subject").value,
                message: document.getElementById("message").value,
             };
             emailjs.send("service_b7jicsu", "template_1e7ya99", params).then(function(res){
                alert("Success! " + res.status);
            })

        }
