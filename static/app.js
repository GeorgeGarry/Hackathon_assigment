function upload_file(){
      let total_files = document.getElementById('files').files;
      if(total_files.length > 0 ){
        let form_data = new FormData();
        for (let i = 0; i < total_files.length; i++) {
          form_data.append("files[]", total_files[i]);
        };

        let xhttp = new XMLHttpRequest();
       
        xhttp.open("POST", "upload_file", true);    // set POST method and ajax file path
        
        xhttp.onreadystatechange = function() {  // check on request changes state
           if (this.readyState == 4 && this.status == 200) {
              let response = this.responseText;
              alert(response + " File uploaded.");
           };
        };
        xhttp.send(form_data);
      }else{
        alert("Please select a file");
      }
      document.getElementById("result_files").style.visibility = "visible";
}

function download_file() {
    let xhttp = new XMLHttpRequest();
    xhttp.addEventListener("load", function() {
      if (this.status == 200) {
        let file_blob = new Blob([this.response], { type: "text/csv" });
        let file_URL = URL.createObjectURL(file_blob);
        let file_link = document.createElement("a");
        file_link.href = file_URL;
        file_link.download = "formed_report.csv";
        file_link.style.display = "none";
        document.body.appendChild(file_link);
        file_link.click();
      }
    });
    xhttp.open("GET", "return_formed_file");
    xhttp.responseType = "blob";
    xhttp.send();
  }