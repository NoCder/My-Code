const submit = document.getElementById("submit");

submit.onclick = function(){
    if(document.getElementById('magnus').checked) {
        document.getElementById("result").innerHTML = "You Passed Chess Test!"
        document.getElementById("result").className = "pass"
    } else {
        document.getElementById("result").innerHTML = "You Failed Chess Test!"
        document.getElementById("result").className = "fail"
    }
};