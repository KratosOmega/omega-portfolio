$(document).ready(function(){
    /* ############################################################# */
    /* set code block width equals to the .highlight div -> when everytime page is refreshed */

    $("td.code").css({
        'width': ($("blockquote").width() + 'px')
    });

    $("td.code pre").css({
        'width': ($("blockquote").width() + 'px')
    });

    /* ############################################################# */

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

    // ********************************************************************************************************************* click to switch exp & skill set
    $(".default-exp-hide").hide();
    $("#research").show();
    //
    $("#showResearch").click(function(){
        $(".default-exp-hide").hide();
        $("#research").show();
        //document.getElementById("#showResearch").className = "btn btn-default active";
        //document.getElementById("#showWebDev").className = "btn btn-default";
    });
    //
    $("#showWebDev").click(function(){
        $(".default-exp-hide").hide();
        $("#webDev").show();
        //document.getElementById("#showWebDev").className = "btn btn-default active";
        //document.getElementById("#showResearch").className = "btn btn-default";
    });
    //
});






