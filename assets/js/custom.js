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
    expSectionCtrl("research");
    //
    $(".showResearch").click(function(){
        expSectionCtrl("research");
    });
    //
    $(".showWebDev").click(function(){
        expSectionCtrl("webDev");
    });
    //
});

function expSectionCtrl(secName){
    $(".default-exp-hide").hide();
    $(".exp-tabs").hide();

    $("#" + secName).show(); //show exp target section
    $("#active-" + secName).show(); //switch exp tabs
}




