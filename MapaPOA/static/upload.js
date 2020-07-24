$('#input_file').change(function () {
  var res = $('#input_file').val();
  var arr = res.split("\\");
  var filename = arr.slice(-1)[0];
  filextension = filename.split(".");
  filext = "." + filextension.slice(-1)[0];
  valid = [".txt", ".cvs", ".tsv", ".xlsx"];
  if (valid.indexOf(filext.toLowerCase()) == -1) {
    $(".imgupload").hide("slow");
    $(".imgupload.ok").hide("slow");
    $(".imgupload.stop").show("slow");
    $('#namefile').css({ "color": "red", "font-weight": 700 });
    $('#namefile').html("O arquivo " + filename + " não é um arquivo de texto!");
    $("#submitbtn").hide();
    $("#fakebtn").show();
  } else {
    $(".imgupload").hide("slow");
    $(".imgupload.stop").hide("slow");
    $(".imgupload.ok").show("slow");
    $('#namefile').css({ "color": "green", "font-weight": 700 });
    $('#namefile').html(filename);
    $("#submitbtn").show();
    $("#fakebtn").hide();
  }
});

$('#submitbtn').click(function () {
    $("#submitbtn").hide();
    $("#fakebtn").show();
});
