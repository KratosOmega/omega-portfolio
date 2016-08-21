$(document).ready(function(){
  // ********************************************************************************************************************* initiate the body to behide 
  $(".default-hide").hide();
  $("#main").show();
  

  // ********************************************************************************************************************* click to show the page
  $("#showMain").click(function(){
    $(".default-hide").hide();
    $("#main").show();
  });
  //
  $("#showAboutMe").click(function(){
    $(".default-hide").hide();
    $("#aboutMe").show();
  });
  //
  $("#showResume").click(function(){
    $(".default-hide").hide();
    $("#resume").show();
  });
  //
  $("#showProject").click(function(){
    $(".default-hide").hide();
    $("#project").show();
  });
  //
  $("#showBlog").click(function(){
    $(".default-hide").hide();
    $("#blog").show();
  });
  //
  $("#showContact").click(function(){
    $(".default-hide").hide();
    $("#contact").show();
  });
  //

  // ********************************************************************************************************************* click to switch skill set
  $(".default-skill-hide").hide();
  $("#backend").show();
  //
  $("#showBackend").click(function(){
    $(".default-skill-hide").hide();
    $("#backend").show();
  });
  //
  $("#showFrontend").click(function(){
    $(".default-skill-hide").hide();
    $("#frontend").show();
  });
  //
  $("#showDevelopment").click(function(){
    $(".default-skill-hide").hide();
    $("#development").show();
  });
  //
});






