$(document).ready(function(){
  swal("Welcome to Word Counter", "ok to continue!", "info");
  $(".btn").click(function(){
    const text = $("textarea").val()
    if (text.length > 0){
      // alert("ready to ajax")
      $.ajax(
        {
          url: "count",
          data: {
            text: text,
          },
          dataType: 'json',
          success : function(data){
              // alert(`success ${data}`)
              console.log(data.most_frequent_word)
              $(".total_word").text(data.word_count)
              $(".total_character").text(data.letter_count)
              $(".most_frequent").text(data.most_frequent_word)
          }
        })
    }
    else{
      $(".total_word").text(0)
      $(".total_character").text(0)
      $(".most_frequent").text("None")
      swal("Text field is empty"," ","error")
    }
  })
});
