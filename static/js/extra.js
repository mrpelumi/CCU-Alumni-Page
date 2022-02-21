var navLinks = $('.nav-link')

var windowUrl = window.location.pathname

$('.blog-entry').on('mouseenter',function(){
    setTimeout(() => {
        $(this).addClass('pressed')
    },100)
    
})
$('.blog-entry').on('mouseleave',function(){
    setTimeout(() => {
        $(this).removeClass('pressed')
    },200)
})

for (let i in navLinks){
    var url = navLinks[i].getAttribute('href')
    if (windowUrl == url){
        navLinks[i].style.color = "#fd5f00"
        break
    }
}

$('.nav-link').on('mouseenter',function(){
    var currentUrl = $(this).attr('href')
    if (url == currentUrl){
        setTimeout(() => {
            $(this).css({"color":"fd5f00"});
        }, 50);
        console.log(currentUrl)
    }
    else{
        setTimeout(() => {
            $(this).css({"color":"#fd5f00"});
        }, 50);
    }
})

$('.nav-link').on('mouseleave',function(){
    var currentUrl = $(this).attr('href')
    if (url == currentUrl){
        $(this).css({"color":"#fd5f00"});
    }
    else {
        setTimeout(() => {
            $(this).css({"color":"white"});
        }, 50);
    }
})
